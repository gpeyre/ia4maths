---
theme: default
title: IA pour la théorie
info: État de l'art, usages et actions pour la communauté mathématique
transition: slide-left
drawings:
  persist: false
lineNumbers: false
mdc: true
---

<div class="deck-cover">
  <div>
    <div class="eyebrow">IA4Maths · 2026</div>
    <div class="cover-title">IA pour<br>la théorie</div>
    <div class="cover-subtitle">État de l'art, usages et actions pour la communauté mathématique</div>
    <div class="cover-meta">
      <strong>Gabriel Peyré</strong><br>
      CNRS et ENS, Université PSL<br><br>
      2 juillet 2026 · <a href="https://github.com/gpeyre/ia4maths">github.com/gpeyre/ia4maths</a>
    </div>
  </div>
  <div class="cover-visual diagram">
    <img src="./assets/generated/unit_distance_series.png" />
  </div>
</div>

---

# Plan de l'exposé

<Roadmap :active="1" lang="fr" />

---

# IA pour les maths

<div class="split">
  <div class="panel amber">
    <h3>IA pour la découverte scientifique</h3>
    <div class="image-frame" style="height: 300px">
      <img src="./assets/generated/euler_pinn_blowup_crop.png" />
    </div>
    <p class="mini-caption">PINNs pour explorer des EDP : Navier-Stokes / Euler, instabilités, contre-exemples.</p>
  </div>
  <div class="panel teal">
    <h3>IA pour la preuve de théorèmes</h3>
    <div class="image-frame" style="height: 300px">
      <img src="./assets/generated/sphere_packing_lean_crop.png" />
    </div>
    <p class="mini-caption">Lean : preuve vérifiée ; Viazovska, empilement optimal de E8.</p>
  </div>
</div>

<div class="panel blue compact" style="margin-top: 18px">
  <strong>Focus :</strong> raisonnement mathématique, de la recherche informelle à la certification formelle.
</div>

<div class="source">Wang--Lai--Gomez-Serrano--Buckmaster, arXiv:2201.06780 ; Hariharan et al., arXiv:2604.23468.</div>

---

# LLMs pour le raisonnement et les maths

<div class="timeline">
  <div class="time-node"><div class="year">2017</div><div class="name">Transformer</div><p>architecture</p></div>
  <div class="time-node"><div class="year">2020</div><div class="name">GPT-3</div><p>passage à l'échelle</p></div>
  <div class="time-node"><div class="year">2022</div><div class="name">ChatGPT</div><p>usage massif</p></div>
  <div class="time-node"><div class="year">2024</div><div class="name">o1</div><p>raisonnement</p></div>
  <div class="time-node"><div class="year">2025</div><div class="name">o3 / DeepSeek-R1</div><p>RL raisonnement</p></div>
  <div class="time-node"><div class="year">2025</div><div class="name">Gemini Deep Think</div><p>niveau IMO</p></div>
  <div class="time-node"><div class="year">2026</div><div class="name">Agents de code</div><p>Codex, Claude Code, OpenClaws</p></div>
</div>

<div class="layout-grid" style="margin-top: 38px">
  <div class="panel blue compact">
    <h3>Modèles de raisonnement</h3>
    <div class="pill-row">
      <span class="pill">o1 / o3</span><span class="pill">DeepSeek-R1</span><span class="pill">Gemini Deep Think</span><span class="pill">Claude reasoning</span>
    </div>
  </div>
  <div class="panel teal compact">
    <h3>Systèmes agentiques</h3>
    <div class="pill-row">
      <span class="pill">Codex</span><span class="pill">Claude Code</span><span class="pill">outils Mistral</span><span class="pill">OpenClaws</span>
    </div>
  </div>
</div>

---

# Pourquoi les maths sont devenues centrales

<div class="panel blue">
  <h3>Les maths comme banc d'essai du raisonnement</h3>
  <ul class="key-list">
    <li><strong>Entraînement</strong><span>Next-token prediction, puis pression d'évaluation vers le raisonnement.</span></li>
    <li><strong>Benchmarks</strong><span>GSM8K, MATH, AIME / IMO-style comme signaux stratégiques.</span></li>
    <li><strong>Raisonnement</strong><span>Reinforcement learning et récompenses liées à la correction mathématique.</span></li>
  </ul>
</div>

<div class="layout-grid" style="margin-top: 18px">
  <div class="panel compact">
    <h3>Snippets de benchmark</h3>
    <ul class="key-list">
      <li><strong>GSM8K</strong><span>arithmétique verbale : « Alice achète 3 carnets... »</span></li>
      <li><strong>MATH</strong><span>algèbre, géométrie, analyse, solutions structurées.</span></li>
      <li><strong>AIME / IMO</strong><span>énoncé court, recherche longue : déterminer, optimiser, prouver.</span></li>
    </ul>
  </div>
  <div class="panel amber compact">
    <h3>Takeaway</h3>
    <p>L'IA agentique passe de réponses locales à un pipeline complet : planifier, coder, vérifier, rédiger.</p>
  </div>
</div>

<div class="source">Cobbe et al. 2021 ; Hendrycks et al. 2021 ; OpenAI Codex 2025/2026.</div>

---

# Problèmes simples : Olympiade de maths

<div class="metric-row compact-metrics">
  <div class="metric"><div class="value">28/42</div><div class="label">2024 · AlphaProof + AlphaGeometry 2, pipeline formel</div></div>
  <div class="metric"><div class="value">35/42</div><div class="label">2025 · Gemini Deep Think, preuves informelles</div></div>
  <div class="metric"><div class="value">IMO</div><div class="label">Énoncés courts, recherche longue, signal fort</div></div>
</div>

<div class="image-frame olympiad-frame">
  <img src="./assets/generated/imo_2025_problem1_crop.png" />
</div>

<div class="source">DeepMind 25/07/2024 et 21/07/2025 ; PDF officiel IMO 2025.</div>

---

# Plan de l'exposé

<Roadmap :active="2" lang="fr" />

---

# Niveau recherche : First Proof

<div class="panel blue compact">
  <h3>Problème</h3>
  <p>Mesurer de façon reproductible la preuve de recherche : problèmes inédits, solutions humaines disponibles, rédaction complète, acceptation anonymisée.</p>
</div>

<div class="layout-grid" style="margin-top: 18px">
  <div class="panel teal">
    <h3>First Batch · 02/2026</h3>
    <ul class="key-list">
      <li><strong>Signal</strong><span>environ <strong>2</strong> succès nets (Q9, Q10).</span></li>
      <li><strong>Zone grise</strong><span>Q5/Q8 proches ou réparables ; pas de revue formelle.</span></li>
    </ul>
  </div>
  <div class="panel teal">
    <h3>Second Batch · 03-06/2026</h3>
    <ul class="key-list">
      <li><strong>OK</strong><span><strong>17/39</strong> soumissions acceptées.</span></li>
      <li><strong>Couverture</strong><span><strong>7/10</strong> problèmes avec au moins une solution OK.</span></li>
      <li><strong>Critère</strong><span>flawless ou minor revisions après revue experte anonymisée.</span></li>
    </ul>
  </div>
</div>

<div class="panel amber compact" style="margin-top: 18px">
  <strong>Takeaway :</strong> des preuves sérieuses deviennent possibles, mais la revue experte reste le goulet d'étranglement.
</div>

<div class="source">ressources/first-proof-summary.md ; 1stProof ; arXiv:2602.05192 ; arXiv:2606.18119.</div>

---

# Niveau recherche : unit distance conjecture

<div class="split reverse unit-intro">
  <div>
    <div class="panel blue compact">
      <h3>Problème</h3>
      <p><em>u(n)</em> : maximum de paires à distance 1 parmi <em>n</em> points plans.</p>
    </div>
    <div class="panel compact" style="margin-top: 12px">
      <h3>Défi OpenAI</h3>
      <p>Résoudre complètement le problème planaire d'Erdos : prouver la borne quasi-grille, ou construire des contre-exemples. <strong>Pas de progrès partiel.</strong></p>
    </div>
    <table class="unit-table">
      <thead><tr><th>Construction</th><th>Exposant</th></tr></thead>
      <tbody>
        <tr><td>Classique</td><td>1+o(1)</td></tr>
        <tr><td>OpenAI</td><td>&gt;1</td></tr>
        <tr><td>Sawin</td><td>1.014</td></tr>
        <tr><td>Emmerich</td><td><strong>1.0152</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div>
    <div class="image-frame" style="height: 425px">
      <img src="./assets/generated/unit_distance_series.png" />
    </div>
    <div class="source">OpenAI, preuve PDF p.3 ; Alon et al. 2605.20695 ; Sawin 2605.20579 ; Emmerich 2606.03419.</div>
  </div>
</div>

---

# Unit distance : quatre constructions

<div class="unit-showcase">
  <div class="image-frame unit-progress-frame">
    <img src="./assets/generated/unit_distance_progress.png" />
  </div>
  <div class="method-strip">
    <div class="method-chip amber"><span>A</span><strong>Grille</strong><em>1+o(1)</em></div>
    <div class="method-chip blue"><span>B</span><strong>OpenAI</strong><em>&gt;1</em></div>
    <div class="method-chip teal"><span>C</span><strong>Sawin</strong><em>1.014</em></div>
    <div class="method-chip violet"><span>D</span><strong>Emmerich</strong><em>1.0152</em></div>
  </div>
</div>

<div class="source">Erdos 1946 ; OpenAI, preuve PDF ; Alon et al. 2605.20695 ; Sawin 2605.20579 ; Emmerich 2606.03419.</div>

---

# Maths formelles : théorème de Viazovska

<div class="layout-grid">
  <div class="panel blue">
    <h3>Problème</h3>
    <ul class="key-list">
      <li><strong>Objet</strong><span>empilement optimal en dimension 8, extension en dimension 24.</span></li>
      <li><strong>Enjeu</strong><span>transférer une preuve de très haut niveau dans Lean.</span></li>
    </ul>
  </div>
  <div class="panel teal">
    <h3>Signal dépôt</h3>
    <ul class="key-list">
      <li><strong>Statut</strong><span>projet Lean public massif autour de E8 / Leech.</span></li>
      <li><strong>Taille</strong><span><strong>830</strong> fichiers, <strong>180 661</strong> lignes Lean.</span></li>
      <li><strong>Référence</strong><span>FLT Lean : 117 fichiers, 15 411 lignes.</span></li>
    </ul>
  </div>
</div>

<div class="panel amber compact" style="margin-top: 18px">
  <strong>Point de gouvernance :</strong> le transfert académique vers le privé a été controversé ; la formalisation pose des questions de crédit, maintenance et infrastructure.
</div>

<div class="source">Dépôts GitHub ; Hariharan et al., arXiv:2604.23468 ; comptage local 09/03/2026.</div>

---

# Maths formelles : analyse / EDP dans Lean

<div class="split">
  <div>
    <div class="panel blue compact">
      <h3>Problème</h3>
      <p>Formaliser l'analyse moderne, encore peu couverte par <code>mathlib</code>.</p>
      <p>Cas d'usage : expert maths non spécialiste Lean, guidé par LLM + vérification formelle.</p>
    </div>
    <div class="code-panel" style="margin-top: 16px">
theorem harnack
  (A : NormalizedEllipticCoeff d (ball 0 1))
  (hsol : IsSolution A.1 u) :
  essSup u μ_1/2 ≤
    exp(C_harnack d * A.1.Λ^1/2) * essInf u μ_1/2 := by ...
    </div>
  </div>
  <div>
    <div class="panel teal">
      <h3>Scott Armstrong + Julia Kempe</h3>
      <p>Harnack, Hölder et bases d'analyse réutilisables dans <code>scottnarmstrong/DeGiorgi</code>.</p>
      <div class="pill-row" style="margin-top: 16px">
        <span class="pill">Sobolev</span><span class="pill">Harnack faible</span><span class="pill">Harnack</span><span class="pill">Hölder</span>
      </div>
    </div>
    <div class="panel amber compact" style="margin-top: 16px">
      <ul class="key-list">
        <li><strong>Faisable</strong><span>avec comptes Claude/Codex pro.</span></li>
        <li><strong>Expertise</strong><span>guidage maths indispensable.</span></li>
        <li><strong>Coût</strong><span>beaucoup de tokens, supportable avec blueprint.</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="source">Armstrong--Kempe, arXiv:2604.05984 ; scottnarmstrong/DeGiorgi ; billet Armstrong 07/04/2026.</div>

---

# Plan de l'exposé

<Roadmap :active="3" lang="fr" />

---

# Mon retour d'expérience

<div class="split reverse">
  <div>
    <div class="panel blue compact">
      <h3>Problème</h3>
      <p>Avancer sur un problème assez bien circonscrit où l'on bloque ; faire du Lean en non spécialiste.</p>
    </div>
    <div class="panel teal" style="margin-top: 14px">
      <h3>Retour personnel</h3>
      <ul class="key-list">
        <li><strong>Déblocage</strong><span>problème ouvert résolu en <strong>2 semaines</strong> via prompts GPT-5 intensifs.</span></li>
        <li><strong>Prépublication</strong><span><a href="https://arxiv.org/abs/2602.01372">arXiv:2602.01372</a></span></li>
        <li><strong>Agents</strong><span>Codex / Claude Code en usage quotidien.</span></li>
        <li><strong>Bibliothèque</strong><span><a href="https://github.com/gpeyre/flow-sinkhorn">github.com/gpeyre/flow-sinkhorn</a></span></li>
      </ul>
    </div>
    <div class="panel amber compact" style="margin-top: 14px">
      <strong>Takeaway :</strong> l'informel débloque les idées ; Lean certifie mais coûte environ 10x plus de tokens.
    </div>
  </div>
  <div class="image-frame" style="height: 520px">
    <img src="./assets/arxiv_2602_01372_p1.png" />
  </div>
</div>

<div class="source">Retour d'expérience + arXiv/GitHub, consulté le 09/03/2026.</div>

---

# Retour d'expérience d'un groupe

<div class="split">
  <div>
    <div class="panel blue compact">
      <h3>Évaluation collective au CSD, ENS</h3>
      <ul class="key-list">
        <li><strong>Protocole</strong><span>même prompt, réponses multiples.</span></li>
        <li><strong>Tâche</strong><span>question semi-ouverte, notebook, code, article, formalisation.</span></li>
        <li><strong>Audit</strong><span>rendus évalués selon plusieurs critères.</span></li>
      </ul>
    </div>
    <div class="code-panel" style="margin-top: 16px">
Consider flow matching with a stochastic interpolant a(t)*X0+b(t)*X1.
In python/ do an indepth numerical simulation ... X0 sim N(0,Id),
X1 is a mixture of three Dirac. In paper/ write a detailed LaTeX article ...
compute in closed form Sigma_t and the flow map T_t.
    </div>
  </div>
  <div>
    <div class="image-frame" style="height: 500px">
      <img src="./assets/generated/codex_gabriel_page4_crop.png" />
    </div>
    <div class="source">Page d'article issue de la soumission codex-gabriel.</div>
  </div>
</div>

<div class="source">ressources/agentic-benchs/todo.md ; rapport comparatif 18/06/2026.</div>

---

# Retour d'expérience : résultats

<div class="split reverse">
  <div class="panel">
    <h3>Agrégation par LLM-juge</h3>
    <table class="score-table">
      <thead><tr><th>Soumission</th><th>Maths</th><th>Code</th><th>Global</th></tr></thead>
      <tbody>
        <tr class="good"><td>emmanuel</td><td>9.3</td><td>8.8</td><td>9.1</td></tr>
        <tr class="good"><td>codex-gabriel</td><td>9.0</td><td>9.0</td><td>8.8</td></tr>
        <tr><td>openclaw</td><td>8.2</td><td>8.6</td><td>8.2</td></tr>
        <tr><td>hermes</td><td>7.8</td><td>8.0</td><td>7.7</td></tr>
        <tr><td>claude-gabriel</td><td>6.5</td><td>7.5</td><td>7.1</td></tr>
        <tr><td>codex-kimia</td><td>7.0</td><td>7.0</td><td>7.0</td></tr>
        <tr><td>codex-clement</td><td>7.0</td><td>5.5</td><td>6.2</td></tr>
        <tr><td>antigravity-a.</td><td>5.8</td><td>6.0</td><td>5.8</td></tr>
        <tr><td>antigravity-o.</td><td>5.5</td><td>5.0</td><td>5.4</td></tr>
      </tbody>
    </table>
  </div>
  <div>
    <div class="panel teal">
      <h3>Signaux robustes</h3>
      <ul class="key-list">
        <li><strong>Maths</strong><span>Codex &gt;&gt; Claude &gt;&gt; reste.</span></li>
        <li><strong>Code</strong><span>Claude &gt;&gt; Codex &gt;&gt; reste.</span></li>
        <li><strong>Budget</strong><span>performance approximativement proportionnelle aux tokens.</span></li>
      </ul>
    </div>
    <div class="panel amber compact" style="margin-top: 16px">
      <h3>Effet du budget tokens</h3>
      <ul class="key-list">
        <li><strong>Petit</strong><span>preuve incorrecte.</span></li>
        <li><strong>Moyen</strong><span>preuve OK, énoncé perfectible.</span></li>
        <li><strong>Gros</strong><span>solution complète.</span></li>
        <li><strong>Énorme</strong><span>Lean viable.</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="source">Expérience CSD ; audit ressources/agentic-benchs/report.</div>

---

# Zoom : Emmanuel Sérié / Noogram

<div class="split">
  <div>
    <div class="panel blue compact">
      <h3>Du prompt CSD à un artefact scientifique complet</h3>
      <p>Une chaîne complète : générer, tester, réfuter, publier.</p>
    </div>
    <div class="panel teal" style="margin-top: 14px">
      <h3>Contribution Noogram</h3>
      <ul class="key-list">
        <li><strong>Théorème</strong><span>FM gaussien = OT ssi covariances commutent.</span></li>
        <li><strong>Artefacts</strong><span>site, code, article, figures, Lean, rapport.</span></li>
        <li><strong>Audit</strong><span>preuve fausse détectée puis corrigée ; score <strong>9.1</strong>.</span></li>
      </ul>
    </div>
    <div class="panel amber compact" style="margin-top: 14px">
      <strong>Takeaway :</strong> harnessing d'agents pour la science : rigueur, revue experte et coût auditable.
    </div>
  </div>
  <div>
    <div class="image-frame" style="height: 248px"><img src="./assets/generated/noogram_flow_matching_site.png" /></div>
    <div class="image-frame" style="height: 218px; margin-top: 18px"><img src="./assets/generated/noogram_flow_matching_github.png" /></div>
  </div>
</div>

<div class="source">Site Noogram ; GitHub noogram-labs/flow-matching-gaussians ; audit CSD.</div>

---

# Plan de l'exposé

<Roadmap :active="4" lang="fr" />

---

# Impact sur l'évaluation et l'enseignement

<div class="impact-layout">
  <div class="impact-hero">
    <h3>Reviewing : l'IA comme premier lecteur</h3>
    <div class="image-frame">
      <img src="./assets/generated/paperreview_ai_screenshot.png" />
    </div>
    <div class="impact-tags">
      <span>premier rapport</span>
      <span>failles locales</span>
      <span>suggestions</span>
      <span>signal faible</span>
    </div>
  </div>
  <div class="guardrails">
    <h3>Enseignement : préserver la formation humaine</h3>
    <div class="guardrail"><span>01</span><strong>Former avant de déléguer</strong><em>rédaction, code, critique locale.</em></div>
    <div class="guardrail"><span>02</span><strong>Évaluer la compréhension</strong><em>oraux et critique de preuves.</em></div>
    <div class="guardrail"><span>03</span><strong>Garder l'humain dans la boucle</strong><em>validité, nouveauté et goût restent humains.</em></div>
    <div class="guardrail"><span>04</span><strong>Auditer les outils</strong><em>les rapports IA trient, ils ne valident pas.</em></div>
  </div>
</div>

<div class="source">PaperReview.ai, Stanford ML Group, capture 02/07/2026 ; synthèse qualitative.</div>

---

# Actions pour la communauté

<div class="actions-board">
  <div class="action-primary">
    <div class="eyebrow">Couche institutionnelle</div>
    <h3>Structurer la communauté</h3>
    <p>Créer un espace partagé entre IA, mathématiques, formalisation et informatique.</p>
    <div class="action-logo-row">
      <div><strong>CNRS RT</strong><span>coordination nationale</span></div>
      <div><strong>AISSAI</strong><span>trimestre « IA pour les maths »</span></div>
      <img src="./assets/generated/aissai_logo.png" />
    </div>
    <div class="action-outcome">
      <span>Cible</span>
      <strong>benchmarks partagés, audits reproductibles, accès modèles</strong>
    </div>
  </div>
  <div class="action-card blue">
    <span>01</span>
    <h3>Ouvrir l'accès aux modèles</h3>
    <p>Dépôts académiques connectés à des modèles contrôlables et auditables.</p>
  </div>
  <div class="action-card violet">
    <span>02</span>
    <h3>Dialogue avec l'industrie</h3>
    <p>Programmes postdoc, outils partagés et canaux de retour scientifique.</p>
  </div>
  <div class="action-card amber">
    <span>03</span>
    <h3>Ne pas oublier la formation</h3>
    <p>Les enseignants conçoivent les tâches ; les évaluateurs préservent l'expertise humaine.</p>
  </div>
</div>

---

# Conclusion

<div class="layout-grid">
  <div class="panel blue">
    <h3>1. Accélération déjà visible</h3>
    <ul class="key-list">
      <li><strong>Performance</strong><span>progrès très rapides.</span></li>
      <li><strong>Workflows</strong><span>coder, vérifier, rédiger.</span></li>
    </ul>
  </div>
  <div class="panel teal">
    <h3>2. Impact scientifique concret</h3>
    <ul class="key-list">
      <li><strong>Informel</strong><span>problèmes ouverts débloqués.</span></li>
      <li><strong>Formel</strong><span>Lean en progrès, coût tokens élevé.</span></li>
    </ul>
  </div>
  <div class="panel violet">
    <h3>3. Rôle humain déplacé</h3>
    <ul class="key-list">
      <li><strong>Positionnement</strong><span>augmenter, pas remplacer.</span></li>
      <li><strong>Rôle</strong><span>chercheur vers juge de qualité des preuves.</span></li>
    </ul>
  </div>
  <div class="panel amber">
    <h3>4. Enjeux collectifs</h3>
    <ul class="key-list">
      <li><strong>Accès</strong><span>modèles contrôlables et auditables.</span></li>
      <li><strong>Tension</strong><span>échanges académie-industrie.</span></li>
      <li><strong>Souveraineté</strong><span>cadre scientifique et institutionnel.</span></li>
    </ul>
  </div>
</div>
