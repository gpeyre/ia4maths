Here is a copy/paste-ready executive summary for a slide-generation agent.

Executive summary: Evolution of First Proof / 1stProof as a benchmark for AI in mathematics

First Proof, also written 1stProof, is an initiative designed to evaluate whether frontier AI systems can autonomously produce rigorous proofs for genuine research-level mathematical problems. The key idea is to move beyond final-answer math benchmarks and test the part of mathematics where the output is a proof that must satisfy expert standards of correctness, clarity, and scholarly attribution. First Proof focuses on the “last-mile” phase of research: a question is already well specified and the mathematical framework is known; the task is to find and write a correct proof. It does not claim to evaluate whether AI can choose important problems, invent new theories, or build entire research programs.  

The initiative evolved in three stages.

First, the February 2026 First Batch was an open pilot. It released 10 unpublished research-level problems with known human solutions of roughly five pages or less. The problems came from active mathematical work and covered fields including stochastic analysis, representation theory, algebraic combinatorics, spectral graph theory, algebraic topology, symplectic geometry, lattices in Lie groups, tensor analysis, and numerical linear algebra. This first stage was exploratory: the community could test AI models, discuss outputs, and compare them later with released human solutions, but First Proof did not yet provide a formal grading protocol or a controlled autonomy guarantee. The later solutions-and-comments document nevertheless gives a useful informal signal: about two answers were described as clearly correct or essentially correct (Questions 9 and 10), with additional near/partial cases such as Questions 5 and 8 depending on how strictly one counts repairable gaps.  

Second, the March–June 2026 Second Batch converted the idea into a formal benchmark. Mathematicians submitted unpublished problems with known human proofs of at most eight pages. Candidate problems were screened for novelty, clarity, and resistance to simple literature lookup. First Proof selected 10 benchmark problems plus a separate set for community experimentation. The formal problems covered computability theory, discrete geometry, discrete probability, metric geometry, stochastic PDE, lattice theory, combinatorial topology, matroids and tropical geometry, algebraic combinatorics, and von Neumann algebras.  

The Second Batch methodology was much more controlled. First Proof itself ran the AI systems, rather than relying on participants’ reports. Each system received the same LaTeX problem inputs and had one shot per problem, with no additional human interaction. The systems had to run as reproducible API-based harnesses, log inputs and outputs, and allow publication of code, logs, outputs, and costs. Four systems were tested: IMProofBench ProofCouncil, UCLA Moonshot Harness, OpenAI ChatGPT 5.5 Pro, and Princeton Momus.  

The grading process was modeled on mathematical journal refereeing. Thirty expert mathematicians reviewed anonymized AI solutions. Each submission received at least two referee reports and was rated as “essentially flawless,” “minor revisions,” “major revisions,” or “reject.” Passing meant essentially flawless or minor revisions. This is important: First Proof did not rely on automatic grading or surface plausibility; it used expert mathematical review.  

The main Second Batch result was mixed but significant. Across the four systems, 7 out of 10 problems received at least one passing AI-generated solution. At submission level, 17 of 39 graded AI outputs passed, where passing meant “essentially flawless” or “minor revisions” after anonymized expert review. The reported ten-problem system runs cost roughly from $117 to $4,799 in API usage, with about $1,014 and $3,186 for the two other systems (System D imputed from token logs; System A missing problem 6 after an API issue). One stochastic PDE problem was solved by an AI system using a novel approach different from the human solution. At the same time, one metric geometry problem saw no substantial progress, and two other problems had only major-revision-level attempts, meaning the approach might be repairable but would still require substantial expert work.  

The failure modes are as important as the successes. Referees found that AI systems often handled routine parts of proofs in great detail while skipping the genuinely difficult step, sometimes hiding a gap behind phrases such as “standard arguments.” Citation quality was also a major weakness: systems sometimes cited papers that did not contain the needed result, or reused nearby literature without proper attribution. The benchmark therefore shows both growing proof capability and the continuing need for expert verification.  

Third, the June–July 2026 Community Experiment reopened the process to public experimentation, but on a separate set of problems. This part is informal: participants can try different models, prompting strategies, and agentic workflows, but they are asked to preserve complete transcripts, model choices, number of attempts, human involvement, token usage, cost, and wall-clock time. Week 1 included problems in online learning and enriched category theory. Week 2, released July 1, included problems in gauge theory/Yang–Mills flow and random graph geometry.  

The take-home message for a presentation on AI for mathematics is this: First Proof shows that frontier LLMs are no longer limited to school or contest-style math; they can sometimes produce serious, referee-passable proofs for real research-level problems. However, the benchmark also shows that mathematical trust is still the bottleneck. A proof-like text can be impressive and still wrong, under-cited, or missing the hard lemma. The most realistic near-term role of AI in mathematics is therefore not “replace mathematicians,” but “accelerate parts of proof search and drafting under expert supervision.” The decisive standard is not whether the model sounds convincing, but whether a specialist can verify the proof.

Suggested slide storyline:

Slide 1: What is First Proof?
A benchmark initiative for AI-generated research-level mathematical proofs, using unpublished problems with known human solutions.

Slide 2: Why it matters
Research mathematics is not just final answers. It requires long arguments, correct use of literature, and expert validation.

Slide 3: Evolution
First Batch: open pilot, public experimentation, no formal grading; informal signal around two clear successes plus near/partial cases.
Second Batch: controlled formal benchmark, one-shot AI systems, expert refereeing.
Community Experiment: public testing space for workflows, transcripts, costs, and discussion.
Third Batch: planned continuation with similar formal methodology.

Slide 4: Problem content
First Batch covered diverse fields such as stochastic analysis, representation theory, algebraic combinatorics, topology, geometry, graph theory, tensors, and numerical linear algebra.
Second Batch covered computability, discrete geometry, probability, metric geometry, stochastic PDE, lattice theory, combinatorial topology, matroids/tropical geometry, algebraic combinatorics, and von Neumann algebras.
Community problems extended to online learning, enriched category theory, gauge theory, and random graph geometry.

Slide 5: Results
In the formal Second Batch, 17 of 39 graded submissions passed, and 7 of 10 problems received at least one passing AI solution. Some outputs were essentially publishable; others failed completely or required major expert repair. Total system-run costs ranged from about $117 to $4,799 for the ten-problem batch. The strongest result was a stochastic PDE proof using a novel approach.

Slide 6: Take-home message
AI is becoming useful for serious proof production, but verification, attribution, and expert judgment remain central. First Proof is valuable because it measures proof quality under realistic mathematical standards, not just answer accuracy.

Resource links to include in slide notes:

Official First Proof homepage
https://1stproof.org/

First Batch page
https://1stproof.org/first-batch.html

First Batch arXiv paper
https://arxiv.org/abs/2602.05192

First Batch solutions and commentary
https://1stproof.org/documents/FirstProofSolutionsComments.pdf

Second Batch benchmark page
https://1stproof.org/second-batch.html

Second Batch formal benchmark report
https://1stproof.org/assets/docs/report.pdf

Second Batch GitHub repository
https://github.com/1stproof/batch-2

Second Batch human solutions
https://github.com/1stproof/batch-2/tree/main/batch-2-human-solution

Second Batch raw input problems
https://github.com/1stproof/batch-2/blob/main/batch-2-raw-outputs/Batch2Problems/problems.json

Second Batch AI-generated solutions
https://github.com/1stproof/batch-2/tree/main/batch-2-AI-solutions

Second Batch referee reports
https://github.com/1stproof/batch-2/tree/main/batch-2-reviews

Second Batch logs and raw outputs
https://github.com/1stproof/batch-2/tree/main/batch-2-raw-outputs

Community Experiment page
https://1stproof.org/community-experiment.html

Community Experiment Week 1 problems
https://1stproof.org/assets/docs/batch2-community-week1.pdf

Community Experiment Week 2 problems
https://1stproof.org/assets/docs/batch2-community-week2.pdf
