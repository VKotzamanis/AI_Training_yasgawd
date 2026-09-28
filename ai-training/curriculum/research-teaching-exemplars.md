# How good explainers teach LLMs to technical non-CS audiences

Evidence for rebuilding the 19-chapter course after the verdict "beginners are lost, experts
gain 0 information". Six sources, chosen for quality over coverage. All were fetched and read;
ordering claims trace to headings, character offsets, or LaTeX source. Fetches are logged in
`SOURCE-LOG.md`.

---

## The three direct answers

### Is there a consensus opening sequence?

**Partial; the split is by audience.**

*General audiences* open on an artefact the reader already owns: Alammar on a phone
keyboard's suggestion strip; Wolfram on "ChatGPT produces text that reads human — how?",
reframed at once as *producing a reasonable continuation*; the FT on a **generated story about
a dog**, read before any mechanism; 3Blue1Brown on expanding G-P-T word by word.

*Trained mathematical audiences* name the object first. Carpenter's slide 1 is "What is a
language model?", defining a finite token set and declaring language a **stochastic process**.
Douglas declares the reader's assumed background, then gives language models as probability
distributions.

Your audience is the second kind of reader with the first kind of exposure: the mathematics is
there, artefact-level familiarity is not. **No source here opens on a rhetorical question about
an undefined subject.**

### Token before or after the prediction loop?

**Genuinely split, predictable from format.**

| Token **before** the loop | Token **after** the loop |
|---|---|
| FT — step 1, "translate words into a language they understand" | Wolfram — loop is §1; token ~6,800 chars in |
| Transformer Explainer — first stage of Embedding | 3Blue1Brown — pipeline preview, then rewind to tokenization |
| Carpenter — slide 1, bullet 1; Douglas — first term defined | Alammar — keyboard first, BPE deferred to one late sentence |

**Sources walking the data path put token first, because that is where it starts. Sources
walking the motivation put the loop first, because nothing motivates tokenization until you
know the model must emit something repeatedly.**

**The finding that matters most: none of these defines "token" by negation.**

- Wolfram: "it's adding a 'token', which could be just a part of a word, which is why it
  can sometimes 'make up new words'."
- FT: "basic units that can be encoded. Tokens often represent fractions of words, but
  we'll turn each full word into a token."
- Douglas: "supersymmetrization … breaks up into 'super,' 'symmetry' and 'ization,'
  pieces which appear in many words and which are called tokens."

Wolfram's pairs the definition with an **observable consequence**, so it earns its place by
explaining something already seen.

### Next-token prediction without sounding trivial or mystical

**State the objective plainly, then break it.**

- **Wolfram** makes it banal — scan billions of pages, count what follows, take the ranked
  list — then shows that always picking the top word gives flat, repetitive text. The gap
  between trivial algorithm and observed behaviour *is* the lesson. Where the reason is
  unknown he says so ("for some reason — that maybe one day we'll have a scientific-style
  understanding of"): he labels the mystery instead of performing it.
- **FT** states it flatly — "LLMs are not search engines looking up facts; they are
  pattern-spotting engines that guess the next best option in a sequence" — then shows greedy
  search producing a locally plausible, globally wrong phrase. The failure does the teaching.
- **Carpenter and Douglas** write cross-entropy over an autoregressive factorisation. For a
  statistically trained reader the objective is *already familiar*, so it cannot sound mystical.
  Carpenter routes it through Shannon (1948) and compression.

The mystical register appears once: the FT's closing Aidan Gomez quote, "That is the magical
part of the story" — placed last, after the mechanism is shown.

---

## The six sources

### 1. Stephen Wolfram — "What Is ChatGPT Doing … and Why Does It Work?"
Writings, 14 Feb 2023. ~20,900 words, **109 images**.
<https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/>

**Order.** Adding One Word at a Time → Where Do the Probabilities Come From? → **What Is a
Model?** → Models for Human-Like Tasks → Neural Nets → Training → Embeddings → Inside ChatGPT
→ The Training of ChatGPT. **The loop is §1, "model" §3, "training" §6; attention appears only
~two-thirds through.** He earns "model" by first fitting a curve through data, then
generalising.

**Opening.** States the phenomenon, states scope honestly ("a rough outline… I won't get
deeply into [engineering details]"), then a worked example on real text ("The best thing
about AI is its ability to →") with a ranked word list and probabilities.

**Diagrams.** A figure every ~190 words: ranked word-probability bars; one sentence
continued at several temperatures; handwritten-digit arrays carrying the "what is a model"
argument; embedding projections.

**Steal:** the **parenthetical deferral**. He writes "adding a word" for a whole section,
then *"(More precisely, as I'll explain, it's adding a 'token', which could be just a part
of a word…)"* — precision on the record without the comprehension cost up front, the debt
flagged so experts aren't offended. One move, both halves of your reviewer's complaint.

### 2. Financial Times — "Generative AI exists because of the transformer"
Madhumita Murgia with Dan Clark, Sam Learner, Irene de la Torre Arenas, Sam Joiner, Eade
Hemingway, Oliver Hawkins. 12 Sep 2023. <https://ig.ft.com/generative-ai/>

**Order.** Tokens → training data → **word embedding** → 2-D projection → self-attention
(with RNN contrast) → *then* next-word prediction → greedy search and its failure → beam
search → hallucination. **The exact inverse of Wolfram**; scrollytelling makes it work.

**Opening.** LLM-*generated* prose first (a dog named Rex, red collar), then the stakes in one
sentence: "the advent of the large language model, or LLM." **The acronym is expanded in the
first sentence it appears in.**

**Diagrams.** One concept each: words breaking into token blocks; a token becoming a list of
numbers; embeddings collapsed to a 2-D scatter (real GloVe 6B 50D, UMAP — method published);
attention lines from "interest" to its disambiguating context, redrawn live when the sentence
is edited; a beam-search tree showing a branch greedy search misses.

**Steal:** the **house analogy for embeddings** — "Just as you might describe a house by
its characteristics — type, location, bedrooms, bathrooms, storeys — the values in an
embedding quantify a word's linguistic features." It hands your audience a feature vector
without saying "vector space"; take the honesty that follows too: "we don't know exactly
what each value represents."

### 3. Michael R. Douglas — "Large Language Models"
Harvard CMSA / Stony Brook. arXiv:2307.05782, v2 6 Oct 2023.
<https://arxiv.org/abs/2307.05782>

**Closest audience match** — "written for readers with a background in mathematics or physics."

**Order.** Introduction → Symbolic and connectionist AI → Language models → Phenomenology →
Simpler language models → **Recipe for an LLM** → Internal workings. Terms:
**token → embedding → model → parameters → training → attention → inference.**

**Opening.** States the event (ChatGPT, Nov 2022), then explicitly declares audience and
assumed background. Do this on your page 1.

**Diagrams. Only two, its main weakness** — a Minerva question-answer pair, and loss vs model
size/dataset/compute. Take the ordering, not the figure budget.

**Steal:** the **domain-native token example**. Douglas picks *supersymmetrization*, a word his
physicists use. Your equivalents are better: *hydrodynamic*, *overtopping*, *poroelasticity*,
*geosynthetic*. A student sees the subword split instantly in a word that is theirs.

### 4. Bob Carpenter — "Language models for statisticians: from *n*-grams to transformers to chatbots"
Flatiron Institute, July 2023. <https://github.com/bob-carpenter/talks/tree/master/llm2023>

**Order (21 slides).** What is a language model? → *N*-grams (Shannon 1948) → Shannon's models
→ Shannon's fit → Entropy → Entropy and compression → GPT-3 → Top-level architecture →
Attention architecture → GPT in 40 lines of pseudocode → Multi-head attention → GPT-3 sizes →
From LLM to Chatbot → RLHF → Caveats → Scaling → GPT-4 → References.

**The first six slides — nearly a third — are *n*-grams and entropy, before "transformer"
appears.** The audience reaches attention already owning the objective, so attention is a
better estimator of a familiar distribution, not a new mystery.

**Text per slide** (measured from LaTeX source, excluding the code slide): median **62 words**,
range 15–130, **4–9 bullets** including sub-bullets. The deliberate outliers are the pseudocode
slide (227) and references (149).

**Diagrams.** Five, each full-bleed at `height=\textheight` or `0.6\textheight`: transformer
architecture, attention, accuracy vs tokens/size, loss vs model/dataset size, Chinchilla FLOPs.
**Figure slides carry a figure and nothing else.**

**Steal:** **reach the transformer through the reader's own discipline**. For statisticians the
bridge is *n*-grams → entropy → compression; for civil and environmental engineers it is
regression / system identification — a model is a parameterised function fitted to data by
minimising a loss, which your students have done.

### 5. 3Blue1Brown — "But what is a GPT? Visual intro to transformers" (Ch. 5)
Grant Sanderson, 1 Apr 2024. <https://www.3blue1brown.com/lessons/gpt>

**Order.** Expand the acronym → the model predicts what comes next → repeated sampling turns
prediction into generation → **whole-pipeline preview** → tokenization → embeddings → attention
→ MLP → layers → final distribution. Then it *rewinds* and revisits each stage in depth.

**The preview-then-zoom structure is the thing to copy** — the reader sees the whole data path
before any stage is explained, so every later detail has somewhere to attach. It is the best
structural answer to "beginners lost, experts bored": beginners get the map, experts see where
the depth is coming.

**Diagrams.** Text splitting into token blocks; each token becoming a column of numbers;
vectors as arrows in reduced 3-D; king−man+woman≈queen as an actual displacement; a softmax
bar chart with temperature altering the bars.

**Steal:** expand every acronym in the sentence that introduces it, and give the whole pipeline
before any part of it.

### 6. Andrej Karpathy — "[1hr Talk] Intro to Large Language Models"
23 Nov 2023, recorded from an AI Security Summit talk.
<https://archive.org/details/youtube-zjkBMFhNj_g>

**Order.** LLM inference → LLM training → how they work / "dreams" → finetuning into an
assistant → scaling laws → tool use → multimodality → security. **Note the unusual and effective
choice: inference before training.** He shows what the artefact *does* before where it came
from; most courses reverse this and lose the audience in optimisation before anyone knows what
is being optimised.

**Opening / first diagram.** **An LLM is two files on disk** — a parameters file and a small run
file that executes it, shown as a directory listing.

**Steal:** the **two-files framing**. It makes "model" a concrete artefact — a large array of
numbers plus the code that evaluates it — before it is a concept. That is exactly the definition
your course was accused of skipping, and it costs one slide.

---

## Runners-up

**Transformer Explainer**, Polo Club, Georgia Tech (CHI 2026,
<https://poloclub.github.io/transformer-explainer/>) — a live GPT-2 (small) in-browser; linked
views carry prompt → tokenization → embedding → positional encoding → Q/K/V → masked attention
heat map → ranked logits. Same order as the FT, and interactive-only, which this project bars
for load-bearing content. **Steal its temperature slider as a static figure:** one prompt at
three temperatures, side by side — teaching sampling, distribution, and why "the model is
deterministic" is wrong.

**Jay Alammar, "The Illustrated GPT-2"** (2019, <https://jalammar.github.io/illustrated-gpt2/>)
— opens on a phone-keyboard screenshot, so nothing is defined the reader has not already used.
Worth it for one figure: the **masking triangle**, future cells greyed, which explains at once
why the model cannot see ahead and why training parallelises but generation cannot. Excluded
as ML-literate and dated.

**NPFL140, Charles University** (<https://ufal.mff.cuni.cz/courses/npfl140>, CC BY-SA 4.0) —
Lecture 2's outcome is literally *"Explain the building blocks of the Transformer architecture
to a non-technical person"*: transferable explanation made assessable.

---

## What I could not find, and what is unverified

1. **Nothing aimed at engineers.** No LLM teaching material written for a civil,
   environmental, mechanical or structural engineering audience. The nearest matches are for
   **mathematicians/physicists** (Douglas) and **statisticians** (Carpenter). Carpenter shows
   the *shape* of the discipline bridge, not its content.

2. **Searches return mostly junk**, as you suspected — predominantly LinkedIn reposts, Medium
   listicles, vendor pages (Elastic, Cornell professional-education marketing), SEO content and
   patent filings. What worked instead: searching named authors and institutions, then going to
   arXiv, course pages and GitHub directly.

3. **Retrieval problems and unverified items**, flagged so they don't harden into fact:
   - **FT** — WebFetch blocked, curl returns only the shell. Text was recovered verbatim from
     the JavaScript bundle, so wording and order are sound, but I have **not seen the rendered
     graphics**; those descriptions come from captions and the method note.
   - **Carpenter** — the announcing blog post 403s; I read the LaTeX source from GitHub
     instead, which is stronger evidence.
   - **Karpathy** — order is from his own chapter markers; the 42 MB slide PDF was not opened,
     so **slide text density is unmeasured**.
   - **Douglas** — the figure count of two is from the HTML of v2, not the PDF.
   - **Wolfram** — fetched with certificate verification disabled (incomplete chain, curl
     error 60); content is from the live site, chain unvalidated.
   - **3Blue1Brown Ch. 6** was not examined, only Ch. 5. No video transcript watched in full.

4. **Not checked:** figure-reuse licensing; only NPFL140 (CC BY-SA 4.0) was confirmed.
