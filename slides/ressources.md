# Resources Used For The AI For Mathematics Slides

This file organizes the main papers, web pages, local documents, screenshots,
figures and code used to build the French and English slide decks.

Deck sources:

- French deck: [`slides/fr/ia4maths_fr.tex`](fr/ia4maths_fr.tex)
- English deck: [`slides/en/ia4maths_en.tex`](en/ia4maths_en.tex)
- Local raw material and benchmark artifacts: [`../ressources/`](../ressources/)
- Numerical figure generation: [`../python/`](../python/)

## 1. LLMs And Mathematics

### Mathematical Reasoning Benchmarks

- **GSM8K**: Cobbe et al., *Training Verifiers to Solve Math Word Problems*.
  - arXiv: <https://arxiv.org/abs/2110.14168>
  - Role in slides: standard grade-school math reasoning benchmark.
- **MATH dataset**: Hendrycks et al., *Measuring Mathematical Problem Solving With the MATH Dataset*.
  - arXiv: <https://arxiv.org/abs/2103.03874>
  - Role in slides: competition-style benchmark with structured solutions.
- **AIME / IMO-style tasks**:
  - Used as examples of short statements with long proof/search processes.
  - Slide-facing local assets:
    - [`fr/assets/imo_2025_p1.png`](fr/assets/imo_2025_p1.png)
    - [`fr/assets/imo_2025_p2.png`](fr/assets/imo_2025_p2.png)
    - [`fr/assets/generated/imo_2025_problem1_crop.png`](fr/assets/generated/imo_2025_problem1_crop.png)

### Reasoning And Agentic Model Timeline

- **OpenAI o1 / reasoning**:
  - OpenAI, *Learning to reason with LLMs*: <https://openai.com/index/learning-to-reason-with-llms/>
  - Local snapshots/assets:
    - [`fr/assets/openai_reasoning.html`](fr/assets/openai_reasoning.html)
    - [`fr/assets/openai_o1_system_card.pdf`](fr/assets/openai_o1_system_card.pdf)
    - [`fr/assets/openai_o1_p1.png`](fr/assets/openai_o1_p1.png)
- **OpenAI o3 / o4-mini and Codex-era agentic coding**:
  - OpenAI, *Introducing OpenAI o3 and o4-mini*: <https://openai.com/index/introducing-o3-and-o4-mini/>
  - Local snapshots/assets:
    - [`fr/assets/openai_o3.html`](fr/assets/openai_o3.html)
    - [`fr/assets/openai_o3_o4_system_card.pdf`](fr/assets/openai_o3_o4_system_card.pdf)
    - [`fr/assets/openai_o3_o4_p1.png`](fr/assets/openai_o3_o4_p1.png)
- **Other model names used in the timeline**:
  - DeepSeek-R1, Gemini Deep Think, Claude Code, Mistral vibe, OpenClaws.
  - Role in slides: broaden the timeline beyond OpenAI product names.

### AI For Scientific Discovery And Theorem Proving

- **PINNs / Euler blow-up visual**:
  - Wang, Lai, Gómez-Serrano, Buckmaster, arXiv:2201.06780.
  - arXiv: <https://arxiv.org/abs/2201.06780>
  - Local sources/assets:
    - [`fr/assets/euler_pinn_blowup_2201_06780.pdf`](fr/assets/euler_pinn_blowup_2201_06780.pdf)
    - [`fr/assets/generated/euler_pinn_blowup_crop.png`](fr/assets/generated/euler_pinn_blowup_crop.png)
- **Lean / sphere packing visual**:
  - Hariharan et al., arXiv:2604.23468.
  - arXiv: <https://arxiv.org/abs/2604.23468>
  - Local sources/assets:
    - [`fr/assets/sphere_packing_lean_2604_23468.pdf`](fr/assets/sphere_packing_lean_2604_23468.pdf)
    - [`fr/assets/generated/sphere_packing_lean_crop.png`](fr/assets/generated/sphere_packing_lean_crop.png)

## 2. AI For Mathematical Research

### Olympiad-Style Problems

- **AlphaProof + AlphaGeometry 2 at IMO 2024**:
  - Google DeepMind, *AI achieves silver-medal standard solving International Mathematical Olympiad problems*.
  - Official page: <https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/>
  - Local snapshot/assets:
    - [`fr/assets/deepmind_silver.html`](fr/assets/deepmind_silver.html)
    - [`fr/assets/deepmind_alphaproof_loop.png`](fr/assets/deepmind_alphaproof_loop.png)
    - [`fr/assets/deepmind_problem4.png`](fr/assets/deepmind_problem4.png)
- **Gemini Deep Think at IMO 2025**:
  - Google DeepMind, *Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad*.
  - Official page: <https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/>
  - Local snapshot/assets:
    - [`fr/assets/deepmind_gold.html`](fr/assets/deepmind_gold.html)
    - [`fr/assets/imo_2025_gemini.pdf`](fr/assets/imo_2025_gemini.pdf)
    - [`fr/assets/imo_2025_gemini.txt`](fr/assets/imo_2025_gemini.txt)
- **AlphaGeometry 2 technical paper**:
  - Chervonyi et al., *Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2*.
  - arXiv: <https://arxiv.org/abs/2502.03544>

### First Proof / 1stProof

- **Local executive summary used to update the slide**:
  - [`../ressources/first-proof-summary.md`](../ressources/first-proof-summary.md)
- **Official project**:
  - Homepage: <https://1stproof.org/>
  - First Batch page: <https://1stproof.org/first-batch.html>
  - Second Batch benchmark page: <https://1stproof.org/second-batch.html>
  - Community Experiment: <https://1stproof.org/community-experiment.html>
- **Papers and reports**:
  - First Batch arXiv paper: <https://arxiv.org/abs/2602.05192>
  - First Batch solutions and commentary: <https://1stproof.org/documents/FirstProofSolutionsComments.pdf>
  - Second Batch arXiv report: <https://arxiv.org/abs/2606.18119>
  - Second Batch formal benchmark report: <https://1stproof.org/assets/docs/report.pdf>
- **Second Batch reproducibility material**:
  - GitHub repository: <https://github.com/1stproof/batch-2>
  - Human solutions: <https://github.com/1stproof/batch-2/tree/main/batch-2-human-solution>
  - AI-generated solutions: <https://github.com/1stproof/batch-2/tree/main/batch-2-AI-solutions>
  - Referee reports: <https://github.com/1stproof/batch-2/tree/main/batch-2-reviews>
  - Logs and raw outputs: <https://github.com/1stproof/batch-2/tree/main/batch-2-raw-outputs>
- **Slide-facing local assets**:
  - [`fr/assets/firstproof.html`](fr/assets/firstproof.html)
  - [`fr/assets/firstproof_faq.html`](fr/assets/firstproof_faq.html)
  - [`fr/assets/firstproof_paper.pdf`](fr/assets/firstproof_paper.pdf)
  - [`fr/assets/firstproof_paper_p1.png`](fr/assets/firstproof_paper_p1.png)
  - [`fr/assets/firstproof_paper_p3.png`](fr/assets/firstproof_paper_p3.png)
  - [`fr/assets/firstproof_solutions.pdf`](fr/assets/firstproof_solutions.pdf)
  - [`fr/assets/firstproof_solutions_p1.png`](fr/assets/firstproof_solutions_p1.png)
  - [`fr/assets/firstproof_solutions_p7.png`](fr/assets/firstproof_solutions_p7.png)

### Unit Distance Conjecture

- **OpenAI announcement / generated proof context**:
  - OpenAI, *A model disproves a discrete geometry conjecture*.
  - French page used in the prompt: <https://openai.com/fr-FR/index/model-disproves-discrete-geometry-conjecture/>
  - English page: <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
  - OpenAI proof PDF: <https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf>
  - OpenAI supplementary remarks PDF: <https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf>
  - OpenAI shortened chain-of-thought PDF: <https://cdn.openai.com/pdf/1625eff6-5ac1-40d8-b1db-5d5cf925de8b/unit-distance-cot.pdf>
- **Human verification and commentary**:
  - Alon et al., *Remarks on the disproof of the unit distance conjecture*.
  - arXiv: <https://arxiv.org/abs/2605.20695>
- **Explicit and optimized exponents**:
  - Sawin, *An explicit lower bound for the unit distance problem*.
  - arXiv: <https://arxiv.org/abs/2605.20579>
  - Emmerich, *Optimizing Explicit Unit-Distance Lower-Bound Certificates*.
  - arXiv: <https://arxiv.org/abs/2606.03419>
- **Numerical / pedagogical figure generation**:
  - Script: [`../python/unit_distance_constructions.py`](../python/unit_distance_constructions.py)
  - Notebook: [`../python/unit_distance_constructions.ipynb`](../python/unit_distance_constructions.ipynb)
  - Generated FR assets:
    - [`fr/assets/generated/unit_distance_series.pdf`](fr/assets/generated/unit_distance_series.pdf)
    - [`fr/assets/generated/unit_distance_series.png`](fr/assets/generated/unit_distance_series.png)
  - Generated EN assets:
    - [`en/assets/generated/unit_distance_series.pdf`](en/assets/generated/unit_distance_series.pdf)
    - [`en/assets/generated/unit_distance_series.png`](en/assets/generated/unit_distance_series.png)

### Formal Mathematics: Sphere Packing / Viazovska In Lean

- **Project page and repository**:
  - Math, Inc. project page: <https://www.math.inc/sphere-packing>
  - GitHub repository: <https://github.com/math-inc/Sphere-Packing-Lean>
- **Reference paper used in the slide**:
  - Hariharan et al., arXiv:2604.23468.
  - arXiv: <https://arxiv.org/abs/2604.23468>
- **Local source assets**:
  - [`fr/assets/sphere_packing_lean_2604_23468.pdf`](fr/assets/sphere_packing_lean_2604_23468.pdf)
  - [`fr/assets/generated/sphere_packing_lean_crop.png`](fr/assets/generated/sphere_packing_lean_crop.png)

### Formal Mathematics: Analysis / PDEs / De Giorgi-Nash-Moser

- **Paper**:
  - Armstrong and Kempe, formalization of De Giorgi-Nash-Moser theory in Lean.
  - arXiv: <https://arxiv.org/abs/2604.05984>
- **Code**:
  - Scott Armstrong's DeGiorgi repository: <https://github.com/scottnarmstrong/DeGiorgi>
- **Take-home-message source**:
  - Armstrong blog post, *Formalizing De Giorgi-Nash-Moser theory in Lean*:
    <https://www.scottnarmstrong.com/2026/04/formalizing-de-giorgi-nash-moser-theory-in-lean/>

## 3. Experience Reports

### Personal Research Experience

- **Preprint used in the slide**:
  - arXiv: <https://arxiv.org/abs/2602.01372>
  - Local PDF and snapshot:
    - [`fr/assets/arxiv_2602_01372.pdf`](fr/assets/arxiv_2602_01372.pdf)
    - [`fr/assets/arxiv_2602_01372_p1.png`](fr/assets/arxiv_2602_01372_p1.png)
- **Associated code/library**:
  - `flow-sinkhorn`: <https://github.com/gpeyre/flow-sinkhorn>

### CSD Group Experiment / Agentic Benchmark

- **Prompt and benchmark setup**:
  - Main prompt: [`../ressources/agentic-benchs/todo.md`](../ressources/agentic-benchs/todo.md)
  - Comparative assessment: [`../ressources/agentic-benchs/report/project_assessment.md`](../ressources/agentic-benchs/report/project_assessment.md)
  - Executive summary report source: [`../ressources/agentic-benchs/report/executive_summary.tex`](../ressources/agentic-benchs/report/executive_summary.tex)
  - Executive summary PDF: [`../ressources/agentic-benchs/report/executive_summary.pdf`](../ressources/agentic-benchs/report/executive_summary.pdf)
- **Codex-Gabriel submission shown in the slide**:
  - Project README: [`../ressources/agentic-benchs/codex-gabriel/README.md`](../ressources/agentic-benchs/codex-gabriel/README.md)
  - Paper source: [`../ressources/agentic-benchs/codex-gabriel/paper/main.tex`](../ressources/agentic-benchs/codex-gabriel/paper/main.tex)
  - Paper PDF: [`../ressources/agentic-benchs/codex-gabriel/paper/main.pdf`](../ressources/agentic-benchs/codex-gabriel/paper/main.pdf)
  - Notebook sources:
    - [`../ressources/agentic-benchs/codex-gabriel/python/flow_matching_dirac_mixture.ipynb`](../ressources/agentic-benchs/codex-gabriel/python/flow_matching_dirac_mixture.ipynb)
    - [`../ressources/agentic-benchs/codex-gabriel/python/gaussian_covariance_ellipses.ipynb`](../ressources/agentic-benchs/codex-gabriel/python/gaussian_covariance_ellipses.ipynb)
  - Slide crop: [`fr/assets/generated/codex_gabriel_page4_crop.png`](fr/assets/generated/codex_gabriel_page4_crop.png)

### Emmanuel Sérié / Noogram

- **Project site**:
  - <https://flow-matching.noogram-labs.dev/>
- **GitHub repository**:
  - <https://github.com/noogram-labs/flow-matching-gaussians>
- **Role in slides**:
  - Example of an agent harness used for production-grade scientific output:
    theorem, code, notebooks, paper, figures, Lean anchor and audit trail.
- **Slide screenshots**:
  - [`fr/assets/generated/noogram_flow_matching_site.png`](fr/assets/generated/noogram_flow_matching_site.png)
  - [`fr/assets/generated/noogram_flow_matching_github.png`](fr/assets/generated/noogram_flow_matching_github.png)

## 4. Impact On Evaluation, Teaching And Community

### Reviewing / Evaluation

- **PaperReview.ai**:
  - Website: <https://paperreview.ai/>
  - Role in slides: example of AI-assisted first-pass reviewing.
  - Screenshot: [`fr/assets/generated/paperreview_ai_screenshot.png`](fr/assets/generated/paperreview_ai_screenshot.png)
- **CSD LLM-as-a-judge audit**:
  - See the local benchmark report material under
    [`../ressources/agentic-benchs/report/`](../ressources/agentic-benchs/report/).

### Teaching / Training

- **Primary material**:
  - The slide is a synthesis based on the benchmark evidence, model capabilities
    shown in the deck and qualitative pedagogical concerns.
- **Core question**:
  - If models reach PhD-student-level local writing, code and critique, how do
    we still train future teachers, reviewers and evaluators of AI-generated
    mathematics?

### Community And Institutions

- **AISSAI / CNRS**:
  - AISSAI logo assets:
    - [`fr/assets/generated/aissai_logo.png`](fr/assets/generated/aissai_logo.png)
    - [`fr/assets/generated/aissai_logo_og.png`](fr/assets/generated/aissai_logo_og.png)
  - Role in slides: French community structuring around AI for mathematics.
- **Industry references in action slide**:
  - DeepMind: already active in mathematical reasoning.
  - Mistral: mentioned as a possible reasoning / mathematics axis.

## Additional Local Source Documents

These files were kept as provenance or auxiliary material during slide
development:

- [`../ressources/06-ia-maths.pdf`](../ressources/06-ia-maths.pdf)
- [`../ressources/marc.pdf`](../ressources/marc.pdf)
- [`../ressources/marc.pptx`](../ressources/marc.pptx)

## Generated Slide Assets

Most final visual assets are duplicated in both language decks so each deck can
compile independently:

- French generated assets: [`fr/assets/generated/`](fr/assets/generated/)
- English generated assets: [`en/assets/generated/`](en/assets/generated/)

When adding new material, keep this convention:

- raw source documents and benchmark artifacts go in [`../ressources/`](../ressources/);
- reusable numerical scripts and notebooks go in [`../python/`](../python/);
- final slide-facing crops/screenshots go in `slides/<lang>/assets/generated/`.
