#!/usr/bin/env python3
"""Pull GPT-2 small's real wte/wpe tables and write a small .mat for the MATLAB animation.

No torch, no transformers, no huggingface_hub. Two HTTP range requests against the
safetensors file (157.5 MB of 548.1 MB). Offsets are re-derived from the file header every
run, never hard-coded, because the repo could be re-uploaded.

Verified on this machine 2026-09-10: HF serves HTTP 206 for byte ranges.
"""
import json, pathlib, struct, subprocess, sys
import numpy as np
import scipy.io as sio
import tiktoken

URL = "https://huggingface.co/openai-community/gpt2/resolve/main/model.safetensors"
HERE = pathlib.Path(__file__).resolve().parent
CACHE = pathlib.Path.home() / ".cache" / "gpt2-slice"
CACHE.mkdir(parents=True, exist_ok=True)

SENTENCE = "The beam is made of steel"
EXPECT_IDS = [464, 15584, 318, 925, 286, 7771]   # locked; verified with tiktoken 2026-09-10
ACTIVE = 5                                        # 0-based index of ' steel'
ROWS = 700                                        # display rows for the 50257-row table


def curl_range(a, nbytes, dest):
    """One HTTP range request -> dest. curl, not urllib: urllib stalls on HF redirect+Range."""
    if dest.exists() and dest.stat().st_size == nbytes:
        print(f"  cached  {dest.name}  ({nbytes:,} B)")
        return dest
    print(f"  fetching {dest.name}  ({nbytes:,} B) ...", flush=True)
    subprocess.run(["curl", "-sL", "--fail", "--max-time", "900",
                    "-r", f"{a}-{a + nbytes - 1}", "-o", str(dest), URL], check=True)
    got = dest.stat().st_size
    if got != nbytes:
        sys.exit(f"FAIL {dest.name}: got {got:,} B, expected {nbytes:,} B")
    return dest


# ---- header ------------------------------------------------------------------
subprocess.run(["curl", "-sL", "--fail", "-r", "0-7", "-o", str(CACHE / "len.bin"), URL], check=True)
hlen = struct.unpack("<Q", (CACHE / "len.bin").read_bytes())[0]
subprocess.run(["curl", "-sL", "--fail", "-r", f"8-{8 + hlen - 1}",
                "-o", str(CACHE / "hdr.json"), URL], check=True)
meta = json.loads((CACHE / "hdr.json").read_bytes()[:hlen])
BASE = 8 + hlen
print(f"safetensors header: {hlen:,} B, {len([k for k in meta if k != '__metadata__'])} tensors")


def tensor(name):
    m = meta[name]
    if m["dtype"] != "F32":
        sys.exit(f"FAIL {name}: dtype {m['dtype']}, expected F32")
    a, b = m["data_offsets"]
    f = curl_range(BASE + a, b - a, CACHE / f"{name}.f32")
    return np.fromfile(f, dtype="<f4").reshape(m["shape"])


wte = tensor("wte.weight")    # (50257, 768)  token  embeddings
wpe = tensor("wpe.weight")    # ( 1024, 768)  position embeddings
print(f"wte {wte.shape}  wpe {wpe.shape}")

# ---- tokens ------------------------------------------------------------------
enc = tiktoken.get_encoding("gpt2")
ids = enc.encode(SENTENCE)
strs = [enc.decode([i]) for i in ids]
if ids != EXPECT_IDS:
    sys.exit(f"FAIL tokenization drifted: {ids} != {EXPECT_IDS}")
print(f"tokens {strs}\nids    {ids}")

# ---- display arrays ----------------------------------------------------------
blk = wte.shape[0] // ROWS                                   # 71 rows per display row
wte_img = wte[:ROWS * blk].reshape(ROWS, blk, 768).mean(axis=1)   # block MEAN, an honest average

# ---- numeric readout ---------------------------------------------------------
# Six of 768 dimensions are shown as numbers. SELECTION RULE, stated so it is
# reproducible and not cherry-picking: the six with the largest |h0|. Their real
# indices are drawn on screen, so the viewer sees they are scattered across 768.
# Dimensions 1..6 would be a table of -0.004s and teach nothing.
e_full = wte[ids[ACTIVE]].astype("float64")
p_full = wpe[ACTIVE].astype("float64")
h_full = e_full + p_full
dims   = np.sort(np.argsort(-np.abs(h_full))[:6])          # 0-based, ascending

# Rows sampled along each marker's travel, so the readout changes while scanning.
SCAN = 48
scan_wte_ids = np.linspace(0, ids[ACTIVE], SCAN).round().astype(int)
scan_wte     = wte[scan_wte_ids][:, dims]
scan_wpe     = wpe[:48][:, dims]

print("\ndisplay dims (1-based):", (dims+1).tolist())
print("  e :", np.round(e_full[dims],2).tolist())
print("  p :", np.round(p_full[dims],2).tolist())
print("  h0:", np.round(h_full[dims],2).tolist())
mism = int(sum(abs(round(e_full[d],2)+round(p_full[d],2)-round(h_full[d],2))>1e-9 for d in dims))
print(f"  columns where the 2dp values do not visibly add: {mism}/6 (rounding, not error)")

sio.savemat(str(HERE / "gpt2_slice.mat"), {
    "disp_dims":    (dims+1).astype(float),
    "e_disp":       e_full[dims], "p_disp": p_full[dims], "h0_disp": h_full[dims],
    "scan_wte":     scan_wte.astype("float32"),
    "scan_wte_ids": scan_wte_ids.astype(float),
    "scan_wpe":     scan_wpe.astype("float32"),
    "wte_img":    wte_img.astype("float32"),
    "wpe_img":    wpe.astype("float32"),
    "e_row":      wte[ids[ACTIVE]].astype("float32"),   # the real row for ' steel'
    "p_row":      wpe[ACTIVE].astype("float32"),        # the real row for slot 5
    "h0_row":    (wte[ids[ACTIVE]] + wpe[ACTIVE]).astype("float32"),
    "token_ids":  np.array(ids, dtype=float),
    "token_strs": "|".join(strs),                       # split on '|' in MATLAB
    "active":     float(ACTIVE + 1),                    # 1-based for MATLAB
    "n_vocab": float(wte.shape[0]), "n_pos": float(wpe.shape[0]), "d_model": 768.0,
    "wte_block": float(blk), "sentence": SENTENCE,
}, do_compression=True)

out = HERE / "gpt2_slice.mat"
print(f"\nwrote {out}  ({out.stat().st_size/1e6:.1f} MB)")
print(f"  e_row  range [{wte[ids[ACTIVE]].min():+.3f}, {wte[ids[ACTIVE]].max():+.3f}]")
print(f"  p_row  range [{wpe[ACTIVE].min():+.3f}, {wpe[ACTIVE].max():+.3f}]")
print(f"  h0_row range [{(wte[ids[ACTIVE]]+wpe[ACTIVE]).min():+.3f}, "
      f"{(wte[ids[ACTIVE]]+wpe[ACTIVE]).max():+.3f}]")
