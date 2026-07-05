<script setup>
const props = defineProps({
  active: { type: Number, default: 1 },
  lang: { type: String, default: "en" }
})

const labels = {
  en: [
    ["LLMs and mathematics", "Reasoning, benchmarks, olympiads"],
    ["AI for research", "Open problems and formalization"],
    ["Experience reports", "Agents, workflows, group audit"],
    ["Community impact", "Evaluation, teaching, institutions"],
  ],
  fr: [
    ["LLMs et maths", "Raisonnement, benchmarks, olympiades"],
    ["IA pour la recherche", "Problèmes ouverts et formalisation"],
    ["Retours d'expérience", "Agents, workflows, audit collectif"],
    ["Impact communauté", "Évaluation, enseignement, institutions"],
  ],
}

const snippets = [
  [
    new URL("../assets/generated/imo_2025_problem1_crop.png", import.meta.url).href,
    new URL("../assets/generated/euler_pinn_blowup_crop.png", import.meta.url).href,
    new URL("../assets/generated/sphere_packing_lean_crop.png", import.meta.url).href,
  ],
  [
    new URL("../assets/generated/unit_distance_series.png", import.meta.url).href,
    new URL("../assets/generated/unit_distance_progress.png", import.meta.url).href,
    new URL("../assets/arxiv_2602_01372_p1.png", import.meta.url).href,
  ],
  [
    new URL("../assets/generated/noogram_flow_matching_site.png", import.meta.url).href,
    new URL("../assets/generated/noogram_flow_matching_github.png", import.meta.url).href,
    new URL("../assets/generated/codex_gabriel_page4_crop.png", import.meta.url).href,
  ],
  [
    new URL("../assets/generated/paperreview_ai_screenshot.png", import.meta.url).href,
    new URL("../assets/generated/aissai_logo.png", import.meta.url).href,
    new URL("../assets/generated/noogram_flow_matching_site.png", import.meta.url).href,
  ],
]

const palette = ["blue", "teal", "amber", "violet"]
const items = labels[props.lang] ?? labels.en
</script>

<template>
  <div class="roadmap">
    <div
      v-for="(item, i) in items"
      :key="item[0]"
      class="roadmap-card"
      :class="[palette[i], { active: active === i + 1 }]"
    >
      <div class="roadmap-patchwork">
        <div
          v-for="(image, j) in snippets[i]"
          :key="image"
          class="roadmap-snippet"
          :class="`snippet-${j + 1}`"
        >
          <img :src="image" alt="" />
        </div>
      </div>
      <div class="roadmap-kicker">0{{ i + 1 }}</div>
      <h3>{{ item[0] }}</h3>
      <p>{{ item[1] }}</p>
    </div>
  </div>
</template>

<style scoped>
.roadmap {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  grid-template-rows: repeat(2, minmax(0, 1fr));
  gap: 16px 22px;
  width: 100%;
  height: 392px;
  align-content: start;
}

.roadmap-card {
  position: relative;
  min-height: 0;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #d8dee8;
  background: #ffffff;
  box-shadow: none;
  display: grid;
  grid-template-rows: 96px auto auto auto;
  transform: scale(0.985);
  opacity: 0.32;
  transition: 200ms ease;
}

.roadmap-card.active {
  transform: scale(1);
  opacity: 1;
  box-shadow: none;
}

.roadmap-card.blue { border-left: 5px solid var(--blue); }
.roadmap-card.teal { border-left: 5px solid var(--teal); }
.roadmap-card.amber { border-left: 5px solid var(--amber); }
.roadmap-card.violet { border-left: 5px solid var(--violet); }

.roadmap-card::before {
  content: none;
}

.roadmap-patchwork {
  position: relative;
  height: 96px;
  display: grid;
  grid-template-columns: 1.28fr 0.72fr;
  grid-template-rows: 1fr 1fr;
  gap: 5px;
  padding: 7px;
  border-bottom: 1px solid #d8dee8;
  overflow: hidden;
  background: #f7f9fc;
}

.roadmap-snippet {
  min-width: 0;
  min-height: 0;
  overflow: hidden;
  border: 1px solid #d8dee8;
  border-radius: 5px;
  background: #ffffff;
}

.roadmap-snippet.snippet-1 {
  grid-row: 1 / 3;
}

.roadmap-snippet img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: saturate(0.92) contrast(1.02);
}

.roadmap-card:not(.active) .roadmap-snippet img {
  filter: saturate(0.42) contrast(0.96) brightness(0.96);
}

.roadmap-kicker,
.roadmap-card h3,
.roadmap-card p {
  position: relative;
  margin-left: 22px;
  margin-right: 22px;
}

.roadmap-kicker {
  margin-top: 8px;
  font-size: 0.64rem;
  color: var(--blue);
  font-weight: 820;
  letter-spacing: 0.16em;
}

.roadmap-card h3 {
  margin-top: 4px;
  margin-bottom: 3px;
  color: var(--ink);
  font-size: 1.02rem;
  line-height: 1.05;
}

.roadmap-card p {
  color: var(--muted);
  font-size: 0.66rem;
  line-height: 1.2;
  max-width: 92%;
  margin-bottom: 8px;
}
</style>
