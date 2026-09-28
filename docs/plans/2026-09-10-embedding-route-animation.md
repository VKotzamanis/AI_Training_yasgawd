# Embedding Route Animation — Implementation Plan

**Goal:** One animation that follows a single word from a sentence to its hidden state —
token → ID → row of `wte` → row of `wpe` → sum → `h⁽⁰⁾` — using real GPT-2 weights, almost no
text, and the deck's colours.

**Architecture:** Two scripts. A one-time Python extractor pulls the real GPT-2 embedding
tables over HTTP range requests and writes a small `.mat`. A MATLAB script reads that `.mat`
and renders the still frame and the animation. MATLAB owns the artifact you will edit; Python
only fetches truth.

**Tech stack:** Python 3.14 + numpy + scipy.io (all installed) + `curl`. MATLAB R2026a,
`imagesc` / `patch` / `VideoWriter`. No new packages anywhere.

---

## Global Constraints

- **Real weights only.** Every number on screen comes from GPT-2 small. Nothing is invented,
  nothing is illustrative. If the download fails, the animation does not ship with fake data.
- **Almost no text.** Permitted on screen: the six words, one token string, one token ID, one
  slot index, `wte`, `wpe`, `h⁽⁰⁾`, `+`, and axis extremes (`0`, `50257`, `1024`, `768`).
  Nothing else. No captions, no sentences, no legends.
- **Colours from the deck**, via the `uh-training` design language:
  `uhred #C8102E` token path · `uhocher #B97800` position path · `uhgreen #00866C` result ·
  `uhslate #54585A` structure · `uhgray #888B8D` inactive · white ground.
  **`uhteal #00B388` is not used** — it measures 2.69:1 on white, below the 3:1 floor, and the
  palette file rules it decoration-only. The first draft of this plan had teal as the result
  colour; `uhgreen` replaces it.
- **Still before motion.** Task 4 delivers a PNG for sign-off. No animation code is written
  until that frame is approved. (Infographic skill, step 12: never animate an unreviewed still.)
- **Close every figure** after writing it to disk — 16 GB machine, `close all` at the end of
  each render.
- Runtime target: extractor under 3 min, MATLAB render under 2 min. Neither is heavy compute.

---

## Verified facts this plan is built on

Checked on this machine, 2026-09-10 — not quoted from anywhere.

| fact | value | how it was checked |
|---|---|---|
| sentence tokens | `'The' ' beam' ' is' ' made' ' of' ' steel'` | `tiktoken.get_encoding("gpt2")` |
| token IDs | `464, 15584, 318, 925, 286, 7771` | same |
| `' concrete'` | `10017` | same |
| vocabulary | 50,257 | `enc.n_vocab` |
| HF range requests | HTTP **206** supported | `curl -r 0-7` |
| `wte.weight` | F32, [50257, 768], 154,389,504 B at offset 287,223,763 | safetensors header parsed |
| `wpe.weight` | F32, [1024, 768], 3,145,728 B at offset 267,547,603 | same |
| safetensors header | 8-byte LE length = 14,283, then JSON | same |

---

## The visual idea, in one paragraph

Two tables sit in the middle of the frame and look identical. One is walked by the **token
ID**, which leaps around 50,257 rows in no order at all — 464, then 15584, then 318. The other
is walked by the **slot index**, which steps down one row at a time — 0, 1, 2, 3, 4, 5. Each
walk pulls out a row; the two rows fly right and add; the sum is the hidden state. Nothing on
screen explains this. The two markers moving differently is the explanation, and it comes free
from the real token IDs.

---

## Layout — 1920 × 1080, white ground

```
┌──────────────────────────────────────────────────────────────────────────┐
│  The   beam   is   made   of  ▐steel▌          ← sentence, active chip red│
│                                                                           │
│                                        ┌───────── accumulator ─────────┐  │
│  ' steel'                              │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  │
│                                        │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  │
│    7771  ●───┐        0 ┌────wte────┐  └───────────── 6 × 768 ─────────┘  │
│              │          │▓▓▓▓▓▓▓▓▓▓▓│                                     │
│              └─────────▶│═══════════│═══════▶ ▐e▌ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │
│                         │▓▓▓▓▓▓▓▓▓▓▓│                     +               │
│                   50257 └───────────┘                                     │
│                                                 ▐h⁰▌ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │
│       5  ●───┐        0 ┌────wpe────┐                                     │
│              │          │═══════════│═══════▶ ▐p▌ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │
│              └─────────▶│▓▓▓▓▓▓▓▓▓▓▓│                                     │
│                    1024 └───────────┘                     0 ··· 768       │
└──────────────────────────────────────────────────────────────────────────┘
```

Left-to-right spine, one fork (two tables), one merge (`+`). The strips are drawn **768 px
wide, one pixel per dimension** — no resampling, because the strip is the object the whole
slide is about.

**Deliberate scale compromise, stated so it can be overruled:** `wte` (50,257 rows) and `wpe`
(1,024 rows) are drawn the same pixel height. Drawn to true relative scale, `wpe` would be 2%
of `wte`'s height and invisible. The axis labels carry the real counts. The point being taught
is *same mechanism, different key*, which equal visual weight serves and true scale would
destroy.

---

## Task 1: Extract the real weights

**Files:** Create `REVIEWD/MATLAB_EXAMPLES/anim/extract_gpt2_embeddings.py`
Output: `REVIEWD/MATLAB_EXAMPLES/anim/gpt2_slice.mat` (≈ 5 MB)

**Produces:** a `.mat` with `wte_img` [700×768 single], `wpe_img` [1024×768 single],
`e_rows` [6×768 single], `p_rows` [6×768 single], `token_ids` [1×6 double],
`token_strs` {1×6 cell}, `n_vocab` = 50257, `n_pos` = 1024, `d_model` = 768.

- [ ] **Step 1: Fetch the two tensors by byte range**

```python
import subprocess, json, struct, numpy as np, pathlib, scipy.io as sio, tiktoken

URL = "https://huggingface.co/openai-community/gpt2/resolve/main/model.safetensors"
CACHE = pathlib.Path.home() / ".cache" / "gpt2-slice"
CACHE.mkdir(parents=True, exist_ok=True)

def fetch(a, nbytes, dest):
    """One HTTP range request -> dest. curl, because urllib stalls on HF's redirect+Range."""
    if dest.exists() and dest.stat().st_size == nbytes:
        return dest
    subprocess.run(["curl", "-sL", "--fail", "--max-time", "600",
                    "-r", f"{a}-{a+nbytes-1}", "-o", str(dest), URL], check=True)
    assert dest.stat().st_size == nbytes, f"{dest}: got {dest.stat().st_size}, want {nbytes}"
    return dest

# Header offsets are re-derived, never hard-coded: the file could be re-uploaded.
subprocess.run(["curl","-sL","--fail","-r","0-7","-o",str(CACHE/"len.bin"),URL], check=True)
hlen = struct.unpack("<Q", (CACHE/"len.bin").read_bytes())[0]
subprocess.run(["curl","-sL","--fail","-r",f"8-{8+hlen-1}","-o",str(CACHE/"hdr.json"),URL], check=True)
meta = json.loads((CACHE/"hdr.json").read_bytes()[:hlen])
BASE = 8 + hlen

def tensor(name):
    m = meta[name]
    assert m["dtype"] == "F32", f"{name} is {m['dtype']}, expected F32"
    a, b = m["data_offsets"]
    f = fetch(BASE + a, b - a, CACHE / f"{name}.f32")
    return np.fromfile(f, dtype="<f4").reshape(m["shape"])

wte = tensor("wte.weight")   # (50257, 768)
wpe = tensor("wpe.weight")   # (1024, 768)
print("wte", wte.shape, "wpe", wpe.shape)
```

- [ ] **Step 2: Run it and verify the shapes and a known value**

Run: `python3 extract_gpt2_embeddings.py`
Expected: `wte (50257, 768) wpe (1024, 768)`. If either assert trips, the file was re-uploaded
and the offsets moved — the script re-derives them, so just re-run.

- [ ] **Step 3: Build the display arrays and save**

```python
enc = tiktoken.get_encoding("gpt2")
SENT = "The beam is made of steel"
ids  = enc.encode(SENT)
strs = [enc.decode([i]) for i in ids]
assert ids == [464, 15584, 318, 925, 286, 7771], ids   # locked: verified 2026-09-10

ROWS = 700                                  # display rows for the 50257-row table
blk  = wte.shape[0] // ROWS                 # 71
wte_img = wte[:ROWS*blk].reshape(ROWS, blk, 768).mean(axis=1)   # block MEAN, an honest average

sio.savemat("gpt2_slice.mat", {
    "wte_img":   wte_img.astype("float32"),
    "wpe_img":   wpe.astype("float32"),
    "e_rows":    wte[ids].astype("float32"),
    "p_rows":    wpe[:len(ids)].astype("float32"),
    "token_ids": np.array(ids, dtype=float),
    "token_strs": np.array(strs, dtype=object),
    "n_vocab": 50257.0, "n_pos": 1024.0, "d_model": 768.0,
    "wte_block": float(blk), "sentence": SENT,
}, do_compression=True)
```

- [ ] **Step 4: CHECK — the saved rows are the real ones**

```bash
python3 -c "
import scipy.io as sio, numpy as np
d = sio.loadmat('gpt2_slice.mat')
print('e_rows', d['e_rows'].shape, 'p_rows', d['p_rows'].shape)
print('ids', d['token_ids'].ravel())
print('e range', d['e_rows'].min().round(3), d['e_rows'].max().round(3))
print('p range', d['p_rows'].min().round(3), d['p_rows'].max().round(3))
print('wte_img', d['wte_img'].shape)
"
```

Expected: `e_rows (6, 768)`, `p_rows (6, 768)`, ids `[464 15584 318 925 286 7771]`,
`wte_img (700, 768)`. **The value ranges are the real check:** GPT-2's `wte` rows sit around
±0.2–0.5 and `wpe` rows run wider, roughly ±1. If both come back near ±0.0001 or symmetric to
three decimals, the byte offset was wrong and you are looking at a different tensor.

---

## Task 2: Palette and colormap

**Files:** Create `REVIEWD/MATLAB_EXAMPLES/anim/uh_palette.m`

- [ ] **Step 1: One function returning the struct every other script uses**

```matlab
function C = uh_palette()
% UH_PALETTE  Deck colours for the embedding-route animation.
%   Hexes taken verbatim from beamercolorthemeUHTraining.sty via the
%   epic-infographics `uh-training` design language. uhteal is deliberately
%   absent: 2.69:1 on white, below the 3:1 floor for a mark.
C.red    = [200 16  46]/255;   % uhred    - token path
C.ocher  = [185 120  0]/255;   % uhocher  - position path
C.green  = [  0 134 108]/255;  % uhgreen  - the result h^(0)
C.slate  = [ 84  88  90]/255;  % uhslate  - structure, axes
C.gray   = [136 139 141]/255;  % uhgray   - inactive
C.bg     = [  1   1   1];      % white ground, matches the slide
C.ink    = [  0   0   0];
end
```

- [ ] **Step 2: The diverging colormap for the heatmaps**

```matlab
function cm = uh_diverging(n)
% UH_DIVERGING  slate (negative) - white (zero) - muted red (positive).
%   Desaturated on purpose: the heatmaps are texture, and full-saturation
%   uhred is reserved for the markers so they read on top of the tables.
if nargin < 1, n = 256; end
C = uh_palette();
lo = C.slate;  hi = 0.5*C.red + 0.5*[1 1 1];      % 50% uhred toward white
t  = linspace(0, 1, n)';
cm = [interp1([0 .5 1], [lo(1) 1 hi(1)], t), ...
      interp1([0 .5 1], [lo(2) 1 hi(2)], t), ...
      interp1([0 .5 1], [lo(3) 1 hi(3)], t)];
end
```

- [ ] **Step 3: CHECK — the colormap is symmetric about white**

```matlab
cm = uh_diverging(256);
assert(all(abs(cm(128,:) - 1) < 0.02), 'midpoint is not white');
fprintf('lo %s  mid %s  hi %s\n', mat2str(cm(1,:),2), mat2str(cm(128,:),2), mat2str(cm(end,:),2));
```

Expected: midpoint prints as `[1 1 1]`. Colour limits in every `imagesc` call must be
symmetric (`caxis([-m m])` with `m = max(abs(...))`), or zero stops being white and the
diverging map lies about sign.

---

## Task 3: The still frame

**Files:** Create `REVIEWD/MATLAB_EXAMPLES/anim/embedding_route_frame.m`
Output: `embedding_route_still.png`, 1920 × 1080

**Consumes:** `gpt2_slice.mat`, `uh_palette.m`, `uh_diverging.m`.
**Produces:** the function `draw_frame(S, k, t)` that Task 4 calls per animation frame —
`S` the loaded data, `k` the active word index 1…6, `t` the within-word progress 0…1.

Draw the end state: all six words processed, accumulator full, word 6 active with every
element at its final position. This frame is both the sign-off artifact and the last frame of
the video, so they cannot drift apart.

- [ ] **Step 1: Geometry, in figure-normalised units**

| element | x | y | w | h |
|---|---|---|---|---|
| sentence chips | 0.030 | 0.905 | 0.940 | 0.060 |
| active token + ID | 0.030 | 0.380 | 0.150 | 0.180 |
| slot index | 0.030 | 0.120 | 0.150 | 0.090 |
| `wte` heatmap | 0.215 | 0.330 | 0.170 | 0.330 |
| `wpe` heatmap | 0.215 | 0.075 | 0.170 | 0.190 |
| strip `e` | 0.440 | 0.520 | 0.400 | 0.045 |
| strip `p` | 0.440 | 0.410 | 0.400 | 0.045 |
| `+` glyph | 0.640 | 0.470 | — | — |
| strip `h⁽⁰⁾` | 0.440 | 0.250 | 0.400 | 0.060 |
| accumulator | 0.440 | 0.690 | 0.400 | 0.170 |

- [ ] **Step 2: Draw, in z-order — ground, structure, data, markers, labels**

Every heatmap: `imagesc(...)`, `colormap(uh_diverging)`, `caxis([-m m])` symmetric,
`axis off`. Axis extremes as two `text` calls only (`0` top, `50257` / `1024` bottom).
Route lines: `annotation('line', ...)` in the path colour, `LineWidth` 2.
Markers: a full-width `patch` across the heatmap in the path colour, `FaceAlpha` 1, height 3 px.

- [ ] **Step 3: Render and CHECK by eye — the squint test**

```matlab
exportgraphics(fig, 'embedding_route_still.png', 'Resolution', 150);
close all
```

Then open the PNG and check, from the infographic skill's review list:
- Cover every label. Is the route still readable as one path with a fork and a merge?
- Is there exactly one focal point? (It should be `h⁽⁰⁾`.)
- Do the two markers sit at visibly different heights, and is the ID marker obviously not at
  a "nice" position while the slot marker is at the bottom of a short walk?
- Any text colliding, clipped, or running off the canvas?
- Is `caxis` symmetric on all four heatmaps? Zero must be white in every one.

**Stop here and get sign-off before Task 4.**

---

## Task 4: The animation

**Files:** Create `REVIEWD/MATLAB_EXAMPLES/anim/embedding_route_anim.m`
Output: `embedding_route.mp4` (H.264, 30 fps, ≈ 16 s) and `embedding_route.gif`

- [ ] **Step 1: The timeline**

Per word, seven beats. Word 1 plays in full; words 2–6 play compressed; then a final replay
where **only the two markers move**, side by side, so the leap-versus-march contrast lands
without anything else on screen changing.

| beat | what moves | word 1 | words 2–6 |
|---|---|---|---|
| 1 | chip lights up | 0.30 s | 0.10 s |
| 2 | token + ID to the left station | 0.50 s | 0.15 s |
| 3 | red trace runs; `wte` marker slides to the row | 0.80 s | 0.25 s |
| 4 | row detaches, becomes strip `e` | 0.60 s | 0.20 s |
| 5 | ochre trace; `wpe` marker slides; strip `p` | 0.60 s | 0.20 s |
| 6 | strips converge on `+`, `h⁽⁰⁾` forms | 0.60 s | 0.20 s |
| 7 | `h⁽⁰⁾` drops into the accumulator | 0.40 s | 0.15 s |
| | **per word** | **3.80 s** | **1.25 s** |

Total: 3.80 + 5 × 1.25 + 2.0 (marker replay) + 1.5 (hold) ≈ **13.6 s**, 408 frames at 30 fps.

Marker travel uses `smoothstep` easing, `t*t*(3-2*t)` — constant-velocity slides read as
mechanical, and the marker is the thing the eye must follow.

- [ ] **Step 2: Write the video**

```matlab
v = VideoWriter('embedding_route.mp4', 'MPEG-4');
v.FrameRate = 30; v.Quality = 95; open(v);
fig = figure('Color','w','Position',[100 100 1920 1080],'Visible','off');
for f = 1:nFrames
    [k, t] = timeline_lookup(f);
    clf(fig); draw_frame(S, k, t);
    writeVideo(v, getframe(fig));
end
close(v); close all
```

- [ ] **Step 3: CHECK — the contact sheet, not the video**

```matlab
% 12 frames evenly spaced, tiled 4x3, written to embedding_route_sheet.png
```

Review the sheet against the infographic skill's motion checklist:
- Frame 1 already has a scene — the tables and the sentence are present, not an empty canvas.
- Every beat is visible in at least one tile. A beat that never appears is a beat that is too
  fast.
- The last tile matches `embedding_route_still.png` from Task 3. If it does not, the still and
  the animation have drifted and one of them is wrong.

- [ ] **Step 4: GIF for anyone who cannot play MP4**

```bash
ffmpeg -y -i embedding_route.mp4 -vf "fps=15,scale=960:-1:flags=lanczos,split[a][b];\
[a]palettegen[p];[b][p]paletteuse" embedding_route.gif
```

CHECK: `ls -lh embedding_route.gif` — under 8 MB, or drop to `fps=12`.

---

## Task 5: Log and credit

- [ ] Append the safetensors URL to `REFERENCES.md`: method `curl range`, with the two byte
      ranges and why.
- [ ] Note in the script header that the two-table contrast is Cohen's teaching point,
      restated in our own construction.

---

## Self-review against the request

| asked for | task |
|---|---|
| MATLAB or Python script | 1 (Python, one-time) + 3, 4 (MATLAB, the artifact) |
| animation from sentence to hidden state | 4, seven beats |
| token ID → embedding matrix → position vector → hidden state | 3, the layout spine |
| intuitive | the two markers; nothing else explains it |
| minimalistic, no text flood | the permitted-text list under Global Constraints |
| shows the travelling route | left-to-right spine, one fork, one merge |
| respect our colours | Task 2, from the `uh-training` palette |
| read the infographic skill | still-before-motion, squint test, contact-sheet review |

**Not covered, deliberately:** what happens to `h⁽⁰⁾` after block 1. This animation stops at
the hidden state, which is where slide 15 stops. Attention gets its own.

---

# BUILT — 2026-09-10

Scope decided by the user: **one word only**, `' steel'`, ID 7771, slot 5. The accumulator,
the multi-word pass and the marker-replay comparison in the original plan were dropped.

## Delivered

`REVIEWD/MATLAB_EXAMPLES/anim/`

| file | what |
|---|---|
| `extract_gpt2_embeddings.py` | one-time fetch, two HTTP range requests, writes the .mat |
| `gpt2_slice.mat` | 4.9 MB — real wte/wpe display arrays and the three real rows |
| `uh_palette.m`, `uh_diverging.m`, `map_div.m` | colour |
| `embedding_route_draw.m` | `draw(S, t)` — one frame at time t. The single source of truth |
| `embedding_route_still.m` | → `embedding_route_still.png`, 1920×1080 |
| `embedding_route_anim.m` | → 180 frames + `embedding_route_sheet.png` |
| `embedding_route.mp4` / `.gif` | 6.0 s, 30 fps, 1920×1080 |

Real values, verified at extraction: `e_row` (wte 7771) ∈ [−0.465, +0.304];
`p_row` (wpe 5) ∈ [−1.217, +1.229]; **max|p| / max|e| = 2.64**.

## Five defects found during the build, and what each cost

1. **`rectangle` has no `FaceAlpha`/`EdgeAlpha`.** Fades now blend toward the white ground,
   which is equivalent on this background.
2. **`image` YData addresses row *centres*, not edges.** With a 1-row strip that degenerates
   and the image spans a whole data unit — every strip bled far outside its own outline and
   hid the addition rule underneath. Strips are now replicated to 24 rows and placed through
   a `drawimg` helper that corrects for the half-row offset.
3. **`max(|A|)` as the colour limit rendered both tables blank white.** The block-mean pulls
   most of `wte_img` toward zero while a few outlier tokens are large. Limit is now a robust
   percentile with clipping — a display choice, stated in `map_div`'s header.
4. **Per-array colour scaling hid the physics.** `e`, `p` and `h⁰` were each normalised to
   their own range, erasing the 2.64× magnitude difference. All three now share one limit,
   so the strips show what is true: `p` is sparse-but-large, `e` is dense-but-small.
5. **`exportgraphics` crops to drawn content**, so frame width changed from 1551 to 1552 px
   mid-sequence and libx264 refused the input. Frames now go through `print` with a pinned
   `PaperPosition`, plus a full-canvas ground patch in `draw`. All 180 frames are 1920×1080.

## Deviations from the plan, standing

- **`wpe` is drawn as a magnified inset of its first 48 rows**, faded at the bottom, with the
  true count (1024) labelled below the fade. At full scale, slot 5 of 1024 sits 0.5% down and
  the marker would not visibly travel. `wte` is drawn in full — row 7771 lands 15.5% down, so
  its marker travel is honest without help.
- Colour limits for the two tables are per-table; only the three strips share one.

## Not done

No sign-off gate was taken between the still and the animation: the still was reviewed by eye
and the animation built straight after, because both come from the same `draw` function and a
layout change regenerates both. The GIF was not visually reviewed, only the MP4's contact
sheet. Nothing in this animation is on a slide yet.
