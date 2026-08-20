<script setup>
import sources from '../sources.json'
// k accepts one key or several, comma-separated: k="kaplan2020,hoffmann2022".
// Several slides draw on more than one source and previously cited only the first,
// which attributed claims to a paper that did not make them.
const props = defineProps({ k: { type: String, required: true } })
const keys = props.k.split(',').map(s => s.trim()).filter(Boolean)
const entries = keys.map(key => ({ key, s: sources[key] }))
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
.kind, .coi { font-weight: 600; margin-left: .35rem; }
.missing { color: #b3261e; font-weight: 700; }
</style>
