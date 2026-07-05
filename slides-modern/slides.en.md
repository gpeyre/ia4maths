---
theme: default
title: AI for Theory
info: State of the art, uses and actions for the mathematical community
transition: slide-left
drawings:
  persist: false
lineNumbers: false
mdc: true
---

<div class="deck-cover">
  <div>
    <div class="eyebrow">IA4Maths · 2026</div>
    <div class="cover-title">AI for<br>Theory</div>
    <div class="cover-subtitle">State of the art, uses and actions for the mathematical community</div>
    <div class="cover-meta">
      <strong>Gabriel Peyré</strong><br>
      CNRS and ENS, Université PSL<br><br>
      July 2, 2026 · <a href="https://github.com/gpeyre/ia4maths">github.com/gpeyre/ia4maths</a>
    </div>
  </div>
  <div class="cover-visual diagram">
    <img src="./assets/generated/unit_distance_series.png" />
  </div>
</div>

---

# Talk Roadmap

<Roadmap :active="1" lang="en" />

---

# AI for Mathematics

<div class="split">
  <div class="panel amber">
    <h3>AI for scientific discovery</h3>
    <div class="image-frame" style="height: 300px">
      <img src="./assets/generated/euler_pinn_blowup_crop.png" />
    </div>
    <p class="mini-caption">PINNs to explore PDEs: Navier-Stokes / Euler, instabilities, counterexamples.</p>
  </div>
  <div class="panel teal">
    <h3>AI for theorem proving</h3>
    <div class="image-frame" style="height: 300px">
      <img src="./assets/generated/sphere_packing_lean_crop.png" />
    </div>
    <p class="mini-caption">Lean: verified proof; Viazovska's optimal E8 packing.</p>
  </div>
</div>

<div class="panel blue compact" style="margin-top: 18px">
  <strong>Focus:</strong> mathematical reasoning, from informal search to formal certification.
</div>

<div class="source">Wang--Lai--Gomez-Serrano--Buckmaster, arXiv:2201.06780; Hariharan et al., arXiv:2604.23468.</div>

---

# LLMs for Reasoning and Mathematics

<div class="timeline">
  <div class="time-node"><div class="year">2017</div><div class="name">Transformer</div><p>architecture</p></div>
  <div class="time-node"><div class="year">2020</div><div class="name">GPT-3</div><p>scale</p></div>
  <div class="time-node"><div class="year">2022</div><div class="name">ChatGPT</div><p>mass adoption</p></div>
  <div class="time-node"><div class="year">2024</div><div class="name">o1</div><p>reasoning</p></div>
  <div class="time-node"><div class="year">2025</div><div class="name">o3 / DeepSeek-R1</div><p>RL reasoning</p></div>
  <div class="time-node"><div class="year">2025</div><div class="name">Gemini Deep Think</div><p>IMO-level</p></div>
  <div class="time-node"><div class="year">2026</div><div class="name">Agentic code</div><p>Codex, Claude Code, OpenClaws</p></div>
</div>

<div class="layout-grid" style="margin-top: 38px">
  <div class="panel blue compact">
    <h3>Reasoning models</h3>
    <div class="pill-row">
      <span class="pill">o1 / o3</span><span class="pill">DeepSeek-R1</span><span class="pill">Gemini Deep Think</span><span class="pill">Claude reasoning</span>
    </div>
  </div>
  <div class="panel teal compact">
    <h3>Agentic systems</h3>
    <div class="pill-row">
      <span class="pill">Codex</span><span class="pill">Claude Code</span><span class="pill">Mistral tools</span><span class="pill">OpenClaws</span>
    </div>
  </div>
</div>

---

# Why Mathematics Became Central for LLMs

<div class="panel blue">
  <h3>Mathematics is a testbed for reasoning</h3>
  <ul class="key-list">
    <li><strong>Training</strong><span>Next-token prediction, then evaluation pressure toward reasoning.</span></li>
    <li><strong>Benchmarks</strong><span>GSM8K, MATH, AIME / IMO-style tasks as strategic signals.</span></li>
    <li><strong>Reasoning</strong><span>Reinforcement learning and rewards attached to mathematical correctness.</span></li>
  </ul>
</div>

<div class="layout-grid" style="margin-top: 18px">
  <div class="panel compact">
    <h3>Benchmark snippets</h3>
    <ul class="key-list">
      <li><strong>GSM8K</strong><span>word arithmetic: "Alice buys 3 notebooks..."</span></li>
      <li><strong>MATH</strong><span>contest algebra, geometry, analysis, structured solutions.</span></li>
      <li><strong>AIME / IMO</strong><span>short statement, long search: determine, optimize, prove.</span></li>
    </ul>
  </div>
  <div class="panel amber compact">
    <h3>Takeaway</h3>
    <p>Agentic AI moves from local answers to a full pipeline: plan, code, verify, write.</p>
  </div>
</div>

<div class="source">Cobbe et al. 2021; Hendrycks et al. 2021; OpenAI Codex 2025/2026.</div>

---

# Simple Problems: Mathematical Olympiads

<div class="metric-row compact-metrics">
  <div class="metric"><div class="value">28/42</div><div class="label">2024 · AlphaProof + AlphaGeometry 2, formal pipeline</div></div>
  <div class="metric"><div class="value">35/42</div><div class="label">2025 · Gemini Deep Think, informal proofs</div></div>
  <div class="metric"><div class="value">IMO</div><div class="label">Small statements, long proof search, high signal</div></div>
</div>

<div class="image-frame olympiad-frame">
  <img src="./assets/generated/imo_2025_problem1_crop.png" />
</div>

<div class="source">DeepMind 25/07/2024 and 21/07/2025; official IMO 2025 PDF.</div>

---

# Talk Roadmap

<Roadmap :active="2" lang="en" />

---

# Research Level: First Proof

<div class="panel blue compact">
  <h3>Problem</h3>
  <p>Reproducible measurement of research-level proving: unseen problems, human solutions available, full write-up, anonymized acceptance.</p>
</div>

<div class="layout-grid" style="margin-top: 18px">
  <div class="panel teal">
    <h3>First Batch · 02/2026</h3>
    <ul class="key-list">
      <li><strong>Signal</strong><span>About <strong>2</strong> clear successes (Q9, Q10).</span></li>
      <li><strong>Gray zone</strong><span>Q5/Q8 close or repairable; no formal review.</span></li>
    </ul>
  </div>
  <div class="panel teal">
    <h3>Second Batch · 03-06/2026</h3>
    <ul class="key-list">
      <li><strong>OK</strong><span><strong>17/39</strong> submissions passed.</span></li>
      <li><strong>Coverage</strong><span><strong>7/10</strong> problems had at least one OK solution.</span></li>
      <li><strong>Criterion</strong><span>Flawless or minor revisions after anonymized expert review.</span></li>
    </ul>
  </div>
</div>

<div class="panel amber compact" style="margin-top: 18px">
  <strong>Takeaway:</strong> serious proofs are possible on nontrivial problems, but expert review remains the bottleneck.
</div>

<div class="source">ressources/first-proof-summary.md; 1stProof; arXiv:2602.05192; arXiv:2606.18119.</div>

---

# Research Level: Unit Distance Conjecture

<div class="split reverse unit-intro">
  <div>
    <div class="panel blue compact">
      <h3>Problem</h3>
      <p><em>u(n)</em>: maximum number of unit-distance pairs among <em>n</em> planar points.</p>
    </div>
    <div class="panel compact" style="margin-top: 12px">
      <h3>OpenAI challenge</h3>
      <p>Resolve Erdos's planar unit-distance problem completely: prove the near-grid upper bound, or build counterexamples to it. <strong>No partial progress.</strong></p>
    </div>
    <table class="unit-table">
      <thead><tr><th>Construction</th><th>Exponent</th></tr></thead>
      <tbody>
        <tr><td>Classical</td><td>1+o(1)</td></tr>
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
    <div class="source">OpenAI proof PDF p.3; Alon et al. 2605.20695; Sawin 2605.20579; Emmerich 2606.03419.</div>
  </div>
</div>

---

# Unit Distance: Four Constructions

<div class="unit-showcase">
  <div class="image-frame unit-progress-frame">
    <img src="./assets/generated/unit_distance_progress.png" />
  </div>
  <div class="method-strip">
    <div class="method-chip amber"><span>A</span><strong>Grid</strong><em>1+o(1)</em></div>
    <div class="method-chip blue"><span>B</span><strong>OpenAI</strong><em>&gt;1</em></div>
    <div class="method-chip teal"><span>C</span><strong>Sawin</strong><em>1.014</em></div>
    <div class="method-chip violet"><span>D</span><strong>Emmerich</strong><em>1.0152</em></div>
  </div>
</div>

<div class="source">Erdos 1946; OpenAI proof PDF; Alon et al. 2605.20695; Sawin 2605.20579; Emmerich 2606.03419.</div>

---

# Formal Mathematics: Viazovska Theorem in Lean

<div class="layout-grid">
  <div class="panel blue">
    <h3>Problem</h3>
    <ul class="key-list">
      <li><strong>Object</strong><span>Optimal packing in dimension 8, extension to dimension 24.</span></li>
      <li><strong>Stakes</strong><span>Transfer a very high-level proof into Lean.</span></li>
    </ul>
  </div>
  <div class="panel teal">
    <h3>Repository signal</h3>
    <ul class="key-list">
      <li><strong>Status</strong><span>Public, massive Lean project around E8 / Leech packing.</span></li>
      <li><strong>Size</strong><span><strong>830</strong> files, <strong>180,661</strong> Lean lines.</span></li>
      <li><strong>Reference</strong><span>FLT Lean: 117 files, 15,411 lines.</span></li>
    </ul>
  </div>
</div>

<div class="panel amber compact" style="margin-top: 18px">
  <strong>Governance point:</strong> academic to private transfer was controversial; formal mathematics raises questions of credit, maintenance and infrastructure.
</div>

<div class="source">GitHub repositories; Hariharan et al., arXiv:2604.23468; local count 09/03/2026.</div>

---

# Formal Mathematics: Analysis / PDEs in Lean

<div class="split">
  <div>
    <div class="panel blue compact">
      <h3>Problem</h3>
      <p>Formalize modern analysis, still sparsely covered by <code>mathlib</code>.</p>
      <p>Use case: math expert, not Lean specialist, guided by LLM + formal checking.</p>
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
      <p>Harnack, Holder and reusable analysis foundations in <code>scottnarmstrong/DeGiorgi</code>.</p>
      <div class="pill-row" style="margin-top: 16px">
        <span class="pill">Sobolev</span><span class="pill">Weak Harnack</span><span class="pill">Harnack</span><span class="pill">Holder</span>
      </div>
    </div>
    <div class="panel amber compact" style="margin-top: 16px">
      <ul class="key-list">
        <li><strong>Feasible</strong><span>with Claude/Codex pro accounts.</span></li>
        <li><strong>Expertise</strong><span>math guidance essential.</span></li>
        <li><strong>Cost</strong><span>many tokens, manageable with a blueprint.</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="source">Armstrong--Kempe, arXiv:2604.05984; scottnarmstrong/DeGiorgi; Armstrong blog post 07/04/2026.</div>

---

# Talk Roadmap

<Roadmap :active="3" lang="en" />

---

# My Research Experience

<div class="split reverse">
  <div>
    <div class="panel blue compact">
      <h3>Problem</h3>
      <p>Make progress on a well-scoped problem where one is stuck; use Lean as a non-specialist.</p>
    </div>
    <div class="panel teal" style="margin-top: 14px">
      <h3>Personal report</h3>
      <ul class="key-list">
        <li><strong>Unlock</strong><span>open problem solved in <strong>2 weeks</strong> through intensive GPT-5 prompting.</span></li>
        <li><strong>Preprint</strong><span><a href="https://arxiv.org/abs/2602.01372">arXiv:2602.01372</a></span></li>
        <li><strong>Agents</strong><span>Codex / Claude Code in daily use.</span></li>
        <li><strong>Library</strong><span><a href="https://github.com/gpeyre/flow-sinkhorn">github.com/gpeyre/flow-sinkhorn</a></span></li>
      </ul>
    </div>
    <div class="panel amber compact" style="margin-top: 14px">
      <strong>Takeaway:</strong> informal reasoning can unlock ideas; Lean certification works but costs roughly 10x more tokens.
    </div>
  </div>
  <div class="image-frame" style="height: 520px">
    <img src="./assets/arxiv_2602_01372_p1.png" />
  </div>
</div>

<div class="source">Personal experience + arXiv/GitHub, accessed 09/03/2026.</div>

---

# Group Experience Report

<div class="split">
  <div>
    <div class="panel blue compact">
      <h3>Collective evaluation at CSD, ENS</h3>
      <ul class="key-list">
        <li><strong>Protocol</strong><span>same prompt, multiple answers.</span></li>
        <li><strong>Task</strong><span>semi-open question, notebook, code, paper, formalization.</span></li>
        <li><strong>Audit</strong><span>submissions evaluated across several criteria.</span></li>
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
    <div class="source">Snapshot: paper page from the codex-gabriel submission.</div>
  </div>
</div>

<div class="source">ressources/agentic-benchs/todo.md; comparative report 18/06/2026.</div>

---

# Group Experience Report: Results

<div class="split reverse">
  <div class="panel">
    <h3>LLM-as-judge aggregation</h3>
    <table class="score-table">
      <thead><tr><th>Submission</th><th>Math</th><th>Code</th><th>Overall</th></tr></thead>
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
      <h3>Robust signals</h3>
      <ul class="key-list">
        <li><strong>Math</strong><span>Codex &gt;&gt; Claude &gt;&gt; rest.</span></li>
        <li><strong>Code</strong><span>Claude &gt;&gt; Codex &gt;&gt; rest.</span></li>
        <li><strong>Budget</strong><span>performance approximately tracks tokens.</span></li>
      </ul>
    </div>
    <div class="panel amber compact" style="margin-top: 16px">
      <h3>Token budget effect</h3>
      <ul class="key-list">
        <li><strong>Small</strong><span>incorrect proof.</span></li>
        <li><strong>Medium</strong><span>proof OK, statement imperfect.</span></li>
        <li><strong>Large</strong><span>complete solution.</span></li>
        <li><strong>Huge</strong><span>Lean viable.</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="source">CSD experiment; audit ressources/agentic-benchs/report.</div>

---

# Zoom: Emmanuel Sérié / Noogram

<div class="split">
  <div>
    <div class="panel blue compact">
      <h3>CSD prompt to full scientific artifact</h3>
      <p>A complete chain: generate, test, refute, publish.</p>
    </div>
    <div class="panel teal" style="margin-top: 14px">
      <h3>Noogram contribution</h3>
      <ul class="key-list">
        <li><strong>Theorem</strong><span>Gaussian FM = OT iff covariances commute.</span></li>
        <li><strong>Artifacts</strong><span>site, code, paper, figures, Lean, report.</span></li>
        <li><strong>Audit</strong><span>false proof found and fixed; score <strong>9.1</strong>.</span></li>
      </ul>
    </div>
    <div class="panel amber compact" style="margin-top: 14px">
      <strong>Takeaway:</strong> agent harnessing for science needs rigor, expert review and auditable cost.
    </div>
  </div>
  <div>
    <div class="image-frame" style="height: 248px"><img src="./assets/generated/noogram_flow_matching_site.png" /></div>
    <div class="image-frame" style="height: 218px; margin-top: 18px"><img src="./assets/generated/noogram_flow_matching_github.png" /></div>
  </div>
</div>

<div class="source">Noogram site; GitHub noogram-labs/flow-matching-gaussians; CSD audit.</div>

---

# Talk Roadmap

<Roadmap :active="4" lang="en" />

---

# Impact on Evaluation and Teaching

<div class="impact-layout">
  <div class="impact-hero">
    <h3>Reviewing: AI as first reader</h3>
    <div class="image-frame">
      <img src="./assets/generated/paperreview_ai_screenshot.png" />
    </div>
    <div class="impact-tags">
      <span>first report</span>
      <span>local flaws</span>
      <span>suggestions</span>
      <span>weak signal</span>
    </div>
  </div>
  <div class="guardrails">
    <h3>Teaching: preserve human training</h3>
    <div class="guardrail"><span>01</span><strong>Train before delegating</strong><em>PhD-level writing, code, local critique.</em></div>
    <div class="guardrail"><span>02</span><strong>Evaluate understanding</strong><em>oral exams and proof critique.</em></div>
    <div class="guardrail"><span>03</span><strong>Keep humans in the loop</strong><em>validity, novelty and taste remain human responsibilities.</em></div>
    <div class="guardrail"><span>04</span><strong>Audit the tools</strong><em>AI reports are triage, not scientific validation.</em></div>
  </div>
</div>

<div class="source">PaperReview.ai, Stanford ML Group, screenshot 02/07/2026; qualitative synthesis.</div>

---

# Actions for the Community

<div class="actions-board">
  <div class="action-primary">
    <div class="eyebrow">Institutional layer</div>
    <h3>Structure the community</h3>
    <p>Build a shared space between AI, mathematics, formalization and computer science.</p>
    <div class="action-logo-row">
      <div><strong>CNRS RT</strong><span>national coordination</span></div>
      <div><strong>AISSAI</strong><span>"AI for mathematics" quarter</span></div>
      <img src="./assets/generated/aissai_logo.png" />
    </div>
    <div class="action-outcome">
      <span>Target</span>
      <strong>shared benchmarks, reproducible audits, model access</strong>
    </div>
  </div>
  <div class="action-card blue">
    <span>01</span>
    <h3>Open access to models</h3>
    <p>Academic repositories connected to controllable, auditable models.</p>
  </div>
  <div class="action-card violet">
    <span>02</span>
    <h3>Dialogue with industry</h3>
    <p>Postdoc programs, shared tools, and channels for scientific feedback.</p>
  </div>
  <div class="action-card amber">
    <span>03</span>
    <h3>Do not forget training</h3>
    <p>Faculty design the tasks; evaluators preserve the human path to expertise.</p>
  </div>
</div>

---

# Conclusion

<div class="layout-grid">
  <div class="panel blue">
    <h3>1. Acceleration already visible</h3>
    <ul class="key-list">
      <li><strong>Performance</strong><span>very fast progress.</span></li>
      <li><strong>Workflows</strong><span>code, verify, write.</span></li>
    </ul>
  </div>
  <div class="panel teal">
    <h3>2. Concrete scientific impact</h3>
    <ul class="key-list">
      <li><strong>Informal</strong><span>open problems unlocked.</span></li>
      <li><strong>Formal</strong><span>Lean progressing, high token cost.</span></li>
    </ul>
  </div>
  <div class="panel violet">
    <h3>3. Human role displaced</h3>
    <ul class="key-list">
      <li><strong>Positioning</strong><span>augment, not replace.</span></li>
      <li><strong>Role</strong><span>researcher to judge of proof quality.</span></li>
    </ul>
  </div>
  <div class="panel amber">
    <h3>4. Collective stakes</h3>
    <ul class="key-list">
      <li><strong>Access</strong><span>controllable and auditable models.</span></li>
      <li><strong>Tension</strong><span>academic-industry exchanges.</span></li>
      <li><strong>Sovereignty</strong><span>scientific and institutional framing.</span></li>
    </ul>
  </div>
</div>
