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

const images = [
  new URL("../assets/generated/imo_2025_problem1_crop.png", import.meta.url).href,
  new URL("../assets/generated/unit_distance_series.png", import.meta.url).href,
  new URL("../assets/generated/noogram_flow_matching_site.png", import.meta.url).href,
  new URL("../assets/generated/paperreview_ai_screenshot.png", import.meta.url).href,
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
      <div class="roadmap-image">
        <img :src="images[i]" alt="" />
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
  grid-template-rows: 82px auto auto auto;
  transform: scale(0.985);
  transition: 200ms ease;
}

.roadmap-card.active {
  transform: scale(1);
  box-shadow: none;
}

.roadmap-card.blue { border-left: 5px solid var(--blue); }
.roadmap-card.teal { border-left: 5px solid var(--teal); }
.roadmap-card.amber { border-left: 5px solid var(--amber); }
.roadmap-card.violet { border-left: 5px solid var(--violet); }

.roadmap-card::before {
  content: none;
}

.roadmap-image {
  position: relative;
  height: 82px;
  border-bottom: 1px solid #d8dee8;
  overflow: hidden;
}

.roadmap-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: saturate(0.92) contrast(1.02);
}

.roadmap-card:not(.active) .roadmap-image img {
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
  margin-top: 10px;
  font-size: 0.64rem;
  color: var(--blue);
  font-weight: 820;
  letter-spacing: 0.16em;
}

.roadmap-card h3 {
  margin-top: 5px;
  margin-bottom: 4px;
  color: var(--ink);
  font-size: 1.02rem;
  line-height: 1.05;
}

.roadmap-card p {
  color: var(--muted);
  font-size: 0.68rem;
  line-height: 1.2;
  max-width: 92%;
  margin-bottom: 8px;
}
</style>
