<script setup>
import sources from '../sources.json'
const props = defineProps({ k: { type: String, required: true } })
const s = sources[props.k]
</script>

<template>
  <footer class="cite" v-if="s">
    <span class="tag" :class="'tag-' + s.tag">[{{ s.tag }}]</span>
    <span class="body">
      {{ s.author }}, {{ s.year }}. <em>{{ s.venue }}</em><template v-if="s.id">, {{ s.id }}</template>.
      <span v-if="s.kind === 'testimony'" class="kind">Expert testimony, not a primary source.</span>
      <span v-if="s.coi" class="coi">COI declared.</span>
    </span>
  </footer>
  <footer class="cite cite-missing" v-else>
    Unresolved citation key "{{ props.k }}"
  </footer>
</template>

<style scoped>
.cite {
  position: absolute; left: 2rem; right: 2rem; bottom: 1rem;
  display: flex; gap: .5rem; align-items: baseline;
  font-size: .62rem; line-height: 1.35; opacity: .78;
  border-top: 1px solid currentColor; padding-top: .4rem;
}
.tag { font-family: ui-monospace, monospace; font-weight: 700; }
.tag-V { color: #2f7d3a; } .tag-P { color: #9a6b12; }
.tag-U, .tag-X { color: #b3261e; }
.kind, .coi { font-weight: 600; margin-left: .35rem; }
.cite-missing { color: #b3261e; font-weight: 700; }
</style>
