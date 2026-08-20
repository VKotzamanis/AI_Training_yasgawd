<script setup>
import sources from '../sources.json'
// Every slide carries a footer. Ruled 2026-08-20 — no exceptions.
//
// A slide either rests on an external source, or it does not. Both cases get a footer,
// because a reader needs to know which. Inventing a citation to satisfy the rule would be
// the exact failure this course spends three sessions warning against, so slides that make
// no external claim declare their provenance instead.
//
//   <Cite k="vaswani2017" />                     one key, or several comma-separated
//   <Cite own="definition" />                    a term this course introduces
//   <Cite own="derived" note="slides 4 to 7" />  follows from what is already on the board
//   <Cite own="computed" />                      arithmetic checkable in this repository
//   <Cite own="observation" />                   established by running it, not by reading it
//   <Cite own="schematic" />                     a drawn figure, values illustrative
//   <Cite own="none" />                          no claim is made on this slide
const props = defineProps({
  k: { type: String, default: '' },
  own: { type: String, default: '' },
  note: { type: String, default: '' },
})

const PROVENANCE = {
  definition: 'Definition — this term is introduced by the course. No external source.',
  derived: 'Follows from earlier slides in this chapter. No external source.',
  computed: 'Computed in this repository — see assets/figures/gen-figures.py. No external source.',
  observation: 'Direct observation, made by running it. No external source.',
  schematic: 'Schematic drawn for this course. Values illustrative and labelled on the figure.',
  none: 'No claim is made on this slide.',
}

const keys = props.k.split(',').map(s => s.trim()).filter(Boolean)
const entries = keys.map(key => ({ key, s: sources[key] }))
// An unrecognised provenance word is an error, not a silent pass — same treatment as a bad key.
const prov = props.own ? (PROVENANCE[props.own] || null) : null
</script>

<template>
  <footer class="cite" :class="{ 'cite-multi': entries.length > 1 }">
    <div v-for="e in entries" :key="e.key" class="row">
      <template v-if="e.s">
        <span class="tag" :class="'tag-' + e.s.tag">[{{ e.s.tag }}]</span>
        <span class="body">
          {{ e.s.author }}, {{ e.s.year }}. <em>{{ e.s.venue }}</em><template v-if="e.s.id">, {{ e.s.id }}</template>.
          <span v-if="e.s.kind === 'testimony'" class="kind">Expert testimony, not a primary source.</span>
          <span v-if="e.s.coi" class="coi">COI declared.</span>
        </span>
      </template>
      <span v-else class="missing">Unresolved citation key "{{ e.key }}"</span>
    </div>
    <div v-if="own" class="row">
      <template v-if="prov">
        <span class="tag tag-own">[—]</span>
        <span class="body prov">{{ prov }}<template v-if="note"> {{ note }}</template></span>
      </template>
      <span v-else class="missing">Unknown provenance "{{ own }}"</span>
    </div>
  </footer>
</template>

<style scoped>
.cite {
  position: absolute; left: 2rem; right: 2rem; bottom: 1rem;
  font-size: .62rem; line-height: 1.35; opacity: .78;
  border-top: 1px solid currentColor; padding-top: .4rem;
}
.cite-multi { font-size: .56rem; line-height: 1.3; }
.row { display: flex; gap: .5rem; align-items: baseline; }
.row + .row { margin-top: .15rem; }
.tag { font-family: ui-monospace, monospace; font-weight: 700; }
.tag-V { color: #2f7d3a; } .tag-P { color: #9a6b12; }
.tag-U, .tag-X { color: #b3261e; }
.tag-own { color: #6b7a7a; }
.prov { font-style: italic; }
.kind, .coi { font-weight: 600; margin-left: .35rem; }
.missing { color: #b3261e; font-weight: 700; }
</style>
