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
  gap: 22px;
  width: 100%;
  height: 100%;
  align-content: center;
}

.roadmap-card {
  position: relative;
  min-height: 235px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: rgba(255, 255, 255, 0.78);
  box-shadow: 0 12px 44px rgba(15, 23, 42, 0.06);
  opacity: 0.48;
  transform: scale(0.985);
  transition: 200ms ease;
}

.roadmap-card.active {
  opacity: 1;
  transform: scale(1);
  box-shadow: 0 22px 70px rgba(24, 42, 73, 0.13);
}

.roadmap-card.active {
  border-color: rgba(37, 95, 146, 0.36);
}

.roadmap-card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(16,24,40,0.72));
  z-index: 1;
}

.roadmap-image {
  position: absolute;
  inset: 0;
}

.roadmap-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: saturate(0.92) contrast(1.02);
}

.roadmap-kicker,
.roadmap-card h3,
.roadmap-card p {
  position: relative;
  z-index: 2;
  margin-left: 22px;
  margin-right: 22px;
}

.roadmap-kicker {
  margin-top: 112px;
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.78);
  font-weight: 820;
  letter-spacing: 0.16em;
}

.roadmap-card h3 {
  margin-top: 10px;
  margin-bottom: 7px;
  color: #fff;
  font-size: 1.46rem;
  line-height: 1.05;
}

.roadmap-card p {
  color: rgba(255, 255, 255, 0.78);
  font-size: 0.86rem;
  max-width: 78%;
}
</style>
