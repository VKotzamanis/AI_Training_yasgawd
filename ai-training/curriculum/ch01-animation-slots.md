# Chapter 1 — animation slots

Written 2026-08-20. The deck reserves labelled empty boxes; the animations drop into them.

## Why a slot rather than an embedded animation

The deck exports to PDF and then to PPTX, where **every slide becomes a page image**. An animation
cannot be layered onto a picture of a slide without covering whatever is printed underneath. So the
deck leaves a box of known size with a caption, which reads sensibly in the PDF — *"animation: the
answer arrives a piece at a time"* — and gives a clean rectangle in PowerPoint to drop media into.

The PDF stays complete and self-explanatory. The PPTX gets the motion. Neither is a degraded copy
of the other.

## Geometry

Beamer at `aspectratio=169` gives a 160 mm × 90 mm canvas. The UH theme spends 8 mm on the logo
band, up to 14.5 mm on a two-line frame title, and 9.4 mm on the footline, leaving **58 mm of
content height and 148 mm of width**. Three slot sizes fit inside that, with margin.

| Slot | Author at | Aspect | On the slide | Use |
|---|---|---|---|---|
| **F** — full | **1600 × 422 px** | 3.79 : 1 | 144 × 38 mm | The animation is the slide |
| **W** — wide | **1600 × 333 px** | 4.80 : 1 | 144 × 30 mm | A short banner |
| **H** — half | **760 × 500 px** | 1.52 : 1 | 70 × 46 mm | Animation beside a text column |

**Corrected 2026-08-20.** The first version of these numbers was derived from the theme's content
height without allowing for the citation footer, which takes about 6 mm. Every slot slide
overflowed its frame. The build now gates on overfull vboxes, which is what caught it.

**These are letterbox, and that is the theme's chrome talking.** The logo band takes 8 mm, a
two-line frame title up to 14.5 mm, the footline 9.4 mm and the footer 6 mm, out of 90 mm. If a
taller slot is wanted, the lever is a title-less animation frame carrying its assertion as a
caption beneath the slot instead, which buys back about 14 mm. Not built; ask if you want it.

Author at those pixel dimensions exactly. The slot scales to fit, so anything at the right aspect
ratio works, but authoring at the stated size means no resampling.

## Authoring constraints

- **Format.** MP4 (H.264, yuv420p) preferred — smaller, sharper, and it does not loop unless told
  to. GIF as a fallback where PowerPoint refuses the codec.
- **Frame rate.** 12–15 fps. Higher buys nothing for a diagram and triples the file.
- **Duration.** 6–10 s, looping. Long enough to read, short enough to talk over.
- **File size.** Under 5 MB each. PowerPoint becomes sluggish past that with several on one deck.
- **Ground.** `#FFFFFF` for general slides. `#1E2224` for console slides.
- **Type.** Times New Roman, to match the deck. Nothing smaller than 28 px at authoring size —
  that is roughly 10 pt projected, which is the floor for a room of six.
- **Motion.** Ease in and out, no bounce. A diagram that overshoots reads as decorative.
- **Every slot's first frame must stand alone**, because that frame is what the PDF shows.

## Colour coding for the four kinds of number

The chapter shows four different sorts of number and the review found they are conflated. Each
gets a fixed colour, used identically in the slides, the figures and the animations.

| What | Colour | Why that one |
|---|---|---|
| **Token ID** | Slate `#54585A` | Deliberately neutral. A token ID is a label with no magnitude |
| **Parameter / weight** | Ocher `#B97800` | The material the model is made of |
| **Logit / raw score** | Teal `#00B388` | What comes out of the network |
| **Probability** | UH Red `#C8102E` | The brand primary, on the quantity the chapter builds toward |

**Colour is a redundant cue and never the only one.** Every coloured number also carries its word —
"token ID 42928", not a lone orange number — and every keyword is bold on first use. A slide that
depends on hue alone fails for a colour-blind reader and fails again in a bad projector.

## The running example

One sentence for the whole chapter:

> **The beam failed in shear because the stirrups were ▁▁▁**

Four candidates, illustrative, used wherever a distribution is drawn:

| Token | Probability |
|---|---|
| ` absent` | 0.41 |
| ` corroded` | 0.27 |
| ` undersized` | 0.19 |
| ` blue` | 0.02 |

**These do not sum to one, and that is the point.** The remaining 0.11 is spread across the tens of
thousands of other entries in the vocabulary. Say so — it is the fastest way to convey that the
distribution covers every token, not four.

Where exact arithmetic is needed, restrict to **two** candidates so the denominator is checkable:
`absent` at a raw score of 2.0 and `corroded` at 1.0. Those give p = 0.881 at T = 0.5, 0.731 at
T = 1.0, and 0.622 at T = 2.0 — already computed in `assets/figures/gen-figures.py`, so the slide,
the figure and the animation cannot drift apart. State on the slide that the example is restricted
to two candidates so the sum can be checked by hand.

---

## The slots

Four are load-bearing. Three are worth having and work as static panels if you would rather not
build them.

### A1 — The answer arrives a piece at a time · **Slot F** (1600 × 422) · ESSENTIAL · real capture

**Contains.** A screen recording of a real session: the question typed, then the reply appearing
left to right at natural speed. No editing, no speed-up — the pace is the point.

**Why a recording rather than a drawing.** It is the opening slide and its whole job is *you have
already seen this*. A drawn imitation of a chat window undercuts that in the first thirty seconds.

**Capture note.** Record at 1600 × 600 or crop to it. Include the model name and the date in frame
if the interface shows them.

### A2 — One sentence becomes tokens · **Slot W** (1600 × 333) · optional

**Contains.** The running sentence in plain text. Vertical cuts fall between tokens one at a time,
left to right. Each piece lifts slightly into its own block. Then the integer **token ID** flips in
beneath each block, in Slate.

**Ends on.** Nine or so blocks with IDs beneath. Caption: *"the model is handed the bottom row."*

**Must show.** A leading space belonging to its token — ` stirrups` not `stirrups`. It is the
detail that makes token counts make sense later.

### A3 — Which earlier words the next one leans on · **Slot F** (1600 × 422) · ESSENTIAL

**Contains.** The running sentence with a boxed `?` at the end. Arcs grow one at a time from
`beam`, `shear` and `stirrups` to the `?`, thickening in proportion to weight, while `The`, `in`,
`because` and `the` stay hairline. Then the four candidates fade in at the right with their
probabilities in UH Red, `absent` at the top.

**This is the jackpot idea, done honestly.** The candidates are visibly *ranked*, not spinning
uniformly. A slot machine's reels are independent and even; this distribution is neither, and if
the animation implies otherwise the room concludes the output is noise.

**Ends on.** Arcs at full weight, candidates listed, `absent` highlighted.

### A4 — The distribution, and the draw · **Slot F** (1600 × 422) · ESSENTIAL — this is the one that matters

**Contains.** Three beats.

1. The four candidate bars rise to their probabilities. Hold. Caption: *"computed from the frozen
   numbers. Same input, same bars, every time."*
2. A marker sweeps the bars and lands on one, weighted by width. `absent` is taken. Caption:
   *"one is drawn."*
3. The bars reset **identically**, the marker sweeps again, and lands somewhere else — `corroded`.
   Repeat five times, showing the same bars producing different picks.

**Why it carries the chapter.** It is the deterministic-to-probabilistic jump made visible: the
bars never change, the pick does. Everything about run-to-run variation, Chapter 4's repeat-run
baseline and Chapter 5's calibration rests on the room seeing that once.

**Must not show.** The bars changing between draws. If they move, the animation teaches that the
model is unstable, which is the opposite of the lesson.

### A5 — Temperature reshapes the distribution · **Slot W** (1600 × 333) · optional

**Contains.** The same four bars with a temperature scale beneath running 0.2 to 2.0. As it moves
right the bars flatten toward even; as it moves left `absent` grows until it takes almost
everything. The word `blue` is visible throughout so the tail can be seen appearing and vanishing.

**Ends on.** T = 1.0, the bars at their stated values.

### A6 — Always taking the top · **Slot F** (1600 × 422) · ESSENTIAL · real capture

**Contains.** A screen recording at temperature zero, run long enough that the output visibly falls
into a repeating phrase. Let it run past the point where the loop is obvious.

**Why this one above all.** The slide currently argues from the mechanism that greedy selection
loops, and never shows it. It was the one slide in the review marked *"confusing, what are you
trying to explain."* This recording is the evidence the slide is missing.

**If it does not loop.** Some models resist repetition. That is a result, not a failed take —
record it anyway and we narrate the difference between *it was patched* and *it is fixed*, which is
the policy Chapter 6 already uses for its demo.

**Capture note.** Model ID and date in frame or in the filename. Both go on the slide.

### A7 — Append and run again · **Slot W** (1600 × 333) · optional

**Contains.** The sentence growing one token at a time. On each pass a small bar chart at the right
recomputes and a token is taken. Four passes.

**Must show.** The parameter block, in Ocher, sitting unchanged beneath every pass. The whole point
is that the only thing growing is the input.

---

## Production

**Do not generate frames with an image model.** Four reasons, and any one is disqualifying:

1. **No frame-to-frame consistency.** Generative image models do not hold a scene steady across
   frames. Positions drift, colours shift, and the result flickers.
2. **Every frame here contains text and numbers** — `stirrups`, `0.41`, token IDs. Rendering legible
   correct text is the weakest thing these models do.
3. **The numbers have to match the slides.** A4's bars must agree with the softmax arithmetic
   printed beside them. A generated image cannot guarantee that; a script can.
4. **The repository forbids it.** The slide specification says generated imagery is not needed and
   should not be used, and every figure in the course is currently computed or drawn by a committed
   script.

**Build the synthetic ones with matplotlib**, in `assets/figures/gen-figures.py`, which already
produces every static figure. `FuncAnimation` writes MP4 through ffmpeg and GIF through pillow —
both verified present. That gives reproducibility, exact numbers, and a diff when something changes.
A2, A3, A4, A5 and A7 are all straightforward that way.

**Record the two real ones yourself.** A1 and A6 show actual tool output, and a drawing of tool
output is worth less than the thing itself — particularly A6, whose entire job is to be evidence.

**Inkscape is installed** if a slot ever needs hand-drawn artwork, but nothing on this list does.
