<div align="center">

<a href="https://sair.foundation/u/25789315" title="Amey Thakur on the SAIR Foundation"><img src="assets/sair-header.png" alt="SAIR Foundation, links to Amey Thakur's SAIR profile" width="700"/></a>

# SAIR Foundation

### Open Science Competitions · Research Index

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Foundation](https://img.shields.io/badge/Foundation-SAIR-340825.svg)](https://sair.foundation/)
[![Research](https://img.shields.io/badge/Research-Open%20Problems-BF3989.svg)](#the-challenges)
[![Author](https://img.shields.io/badge/Author-Amey%20Thakur-0969DA.svg)](https://github.com/Amey-Thakur)

**A single index to every SAIR Foundation challenge I have entered: what each one asks, where the work lives, and what came of it.**

---

[❖ Author](#author) &nbsp;·&nbsp; [ⓘ Overview](#overview) &nbsp;·&nbsp; [◎ Motivation](#motivation) &nbsp;·&nbsp; [☰ Challenges](#the-challenges) &nbsp;·&nbsp; [★ Results](#results) &nbsp;·&nbsp; [◬ Reading Order](#reading-order) &nbsp;·&nbsp; [☷ Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [© License](#license) &nbsp;·&nbsp; [⌬ About](#about-this-repository) &nbsp;·&nbsp; [✦ Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  <a name="author"></a>
  ## Author

| <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![SAIR](https://img.shields.io/badge/SAIR-ID%2025789315-340825.svg)](https://sair.foundation/u/25789315)<br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-A6CE39.svg)](https://orcid.org/0000-0001-5644-1575) |
| :---: |

</div>

---

## Overview

The [SAIR Foundation](https://sair.foundation/) runs open competitions on unsolved
problems in mathematics and computation. Each one takes a question that is
genuinely open, gives everybody the same statement of it, and publishes what
comes back. Every one I have entered has its own repository holding the
method, the code, and an honest account of where it stopped.

This repository is the index to them. It exists so that there is one address
to remember instead of one per competition, and so that the relationship
between them is written down somewhere rather than inferred.

My entrant profile on the Foundation is [ID 25789315](https://sair.foundation/u/25789315), which the
header above also links to.

**Purpose**: To provide organized access to every SAIR Foundation challenge in one place, with the question each one asks, the repository holding the work, the dates that govern it, and what the method actually reached.

**Target Audience**: Competitors, researchers, students, and reviewers looking for the statement of an open problem, a verifier they can run, or an honest account of how far a method got before it stopped.

---

## Motivation

I keep entering these because they are the rare case where the honest answer is
allowed to be no.

Most of the work I am asked to show has a shape agreed in advance. There is a
known technique, a known result, and the exercise is to arrive at it neatly. An
open problem does not offer that. You bring a method, the method either reaches
something or it does not, and nobody can tell you in advance which it will be.
That is uncomfortable, and it is the only condition under which I learn
anything I could not have looked up.

What I have taken from them, more than any single result, is a habit
about negative findings. In the Inverse Galois competition my search hit the
known record exactly nine times, and I spent a day reading that as success
before understanding it as the end of the road: my method had rediscovered what
was already known and could go no further. That was the most useful thing the
whole run produced, and it is only useful because it was measured rather than
felt.

**Why this index exists:**

- **Single Entry Point**: To let you reach any challenge without knowing which competition it belonged to, which repository holds it, or whether it is still open.
- **Honest Reporting**: To say what each method actually reached, including the runs that reached nothing, so you can judge an approach before spending a week on it.
- **Verifiable Figures**: To keep every number traceable to the competition that published it or the repository that measured it, so you can check it rather than take my word for it.
- **Open Contribution**: To share the verifiers, the analyses, and the negative results freely, believing that knowledge grows when freely exchanged.

> [!NOTE]
> Every figure in this index is either published by the competition or measured
> by the repository it links to. Where a competition has not published a
> standing, this says so rather than filling the gap.

---

## The Challenges

Newest first. Status reflects the competition, not my progress; my own
results are in [Results](#results).

| Challenge | The question it asks | Repository | Status |
|:----------|:---------------------|:----------:|:------:|
| **Andrews–Curtis Conjecture** | Can every balanced presentation of the trivial group be reduced to the standard one by three elementary moves? | [Repository](https://github.com/Amey-Thakur/SAIR-ANDREWS-CURTIS-CHALLENGE) | Open |
| **Lean Kernel** *(Stage 1)* | How cheaply can Lean's kernel verify a computation that has been proved correct? | [Repository](https://github.com/Amey-Thakur/SAIR-LEAN-KERNEL-CHALLENGE) | Open |
| **Mathematics Distillation** *(Equational Theories)* | Which implications between equational theories can be decided, and can a machine certify them? | [Repository](https://github.com/Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE) | Closed |
| **Inverse Galois Problem** *(IGP24)* | Which finite groups occur as Galois groups of degree 24 polynomials over the rationals? | [Repository](https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24) | Closed |
| **Modular Arithmetic** | Can a neural network compute an exact modular product of numbers hundreds of digits long? | [Repository](https://github.com/Amey-Thakur/SAIR-MODULAR-ARITHMETIC-CHALLENGE) | Closed |

> [!TIP]
> If you are choosing where to start, start with the **Andrews–Curtis**
> repository. Its question is the easiest to state in full, the moves are three
> lines of definition, and the verifier is small enough to read in one sitting.

### What each repository holds

| Repository | What is in it |
|:-----------|:--------------|
| [Andrews–Curtis](https://github.com/Amey-Thakur/SAIR-ANDREWS-CURTIS-CHALLENGE) | The five Andrews-Curtis moves, a verifier that replays a submitted move sequence and refuses one it cannot finish, and a measured baseline search |
| [Lean Kernel](https://github.com/Amey-Thakur/SAIR-LEAN-KERNEL-CHALLENGE) | The Stage 1 submission skeleton in Lean 4, an audit that refuses an unproved goal or one settled outside the kernel, and an independent proof checker kept for a separate benchmark |
| [Mathematics Distillation](https://github.com/Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE) | Stage 1 cheatsheets and prompt work, and the Stage 2 solver that emits Lean certificates, with the experiment ledger that records what each change measured |
| [Inverse Galois Problem](https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24) | The search and construction code, every submission batch kept as it was sent, and the analysis of why the method stopped where it did |
| [Modular Arithmetic](https://github.com/Amey-Thakur/SAIR-MODULAR-ARITHMETIC-CHALLENGE) | The architectures, the tokenisation that carries place value, the curriculum data, and the sandbox that rehearses the judge |

---

## Results

What my own work reached. Published standings where a competition published
one, and measurements from the repositories where it did not.

| Challenge | Result | Source |
|:----------|:-------|:------:|
| **Inverse Galois Problem** | Rank **54**, score **2.3559**, 10,180 scoreable pairs, as team AVATAR | Competition leaderboard |
| **Andrews–Curtis** | Baseline search trivialises `AK(2)` in **18 verified moves**; `AK(3)` and stable `AK(2)` are not reached inside 60,000 nodes | Repository, reproducible |
| **Lean Kernel** | The Stage 1 artifact builds and its proof depends on `propext` and `Quot.sound` only. The separate checker rejects both of the arena's exports that prove `False` | Repository CI |
| **Mathematics Distillation** | Stage 2 solver submitted, deterministic on both tracks | Repository |
| **Modular Arithmetic** | Model published, submission recorded. The competition did not publish a leaderboard | Competition API |

> [!NOTE]
> The Inverse Galois standing is final: that competition finished on
> 15 August 2026. The repository records the date its figures were read.

### The one finding worth carrying between them

> Your choice of construction method decides the outcome, and you can test it
> in a day. One approach put 57% of its output in useful territory. Another
> managed 1.6%.

That came out of the Inverse Galois run, and it has held up in every challenge
since. Measure the method before scaling it, and drop whatever manufactures
easy answers.

---

## Reading Order

If you want the reasoning rather than the code, each repository carries its own
documentation and they are written to be read in this order.

1. **The problem**, in the repository README. What is actually being asked, without the competition framing.
2. **The competition analysis**, under `docs/competition/`. What is submitted, what is measured, and what disqualifies an entry.
3. **The method**, under `src/`. Every repository keeps the part that decides an answer separate from the part that searches for one.
4. **The open questions**, under `docs/research/`. What is unfinished, and what a failed run does and does not prove.

> [!NOTE]
> Every repository states its gaps in its own documentation. That is deliberate:
> a repository that only lists what works is not a record of research, it is
> advertising.

---

## Usage Guidelines

**For Competitors**  
The verifiers and audits in these repositories are the reusable parts. Checking a submission locally costs nothing, and in every one of these competitions an entry that does not replay is worth exactly zero.

**For Educators**  
Each repository states an open problem in full and then shows a method reaching its limit. That combination is difficult to find in teaching material, where problems usually come with known answers.

**For Researchers**  
The negative results are the honest contribution. Where a search stopped, the repositories record the budget it stopped at, so the measurement can be repeated rather than taken on trust.

---

## License

This repository and the indexed work are made available under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

Copyright © 2026 Amey Thakur

---

## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur)

This repository is the index to my work on the SAIR Foundation's open competitions. It holds no method of its own. Each challenge keeps its own code, its own documentation and its own account of where it stopped, and this index exists to make that set navigable and to keep the dates and standings in one place as competitions open and close.

**Connect:** [GitHub](https://github.com/Amey-Thakur) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/amey-thakur) &nbsp;·&nbsp; [ORCID](https://orcid.org/0000-0001-5644-1575) &nbsp;·&nbsp; [SAIR](https://sair.foundation/u/25789315)

### Acknowledgments

**Foundation**: [SAIR Foundation](https://sair.foundation/), Foundation for Science and AI Research  
**Co-organising institutions**: Caltech · Lean FRO  
**Period**: 2026

Grateful acknowledgment to the **SAIR Foundation** for running these competitions in the open, and for publishing the results and the data afterwards. Posing genuinely unsolved problems to anybody who wants to try them, and then releasing what comes back, is a rarer thing than it should be.

Grateful acknowledgment to the **co-organisers** of the individual challenges, named in the table above, whose problem statements are precise enough that a wrong answer is recognisably wrong. That precision is what makes an open competition possible at all.

Grateful acknowledgment to the **participants** whose entries crowded the leaderboards I was working against. The most useful measurement in the Inverse Galois run was how many teams had already reached the targets I was reaching, and that number is a collective product.

---

<!-- FOOTER -->
<div align="center">

  [↑ Back to Top](#sair-foundation)

  [❖ Author](#author) &nbsp;·&nbsp; [ⓘ Overview](#overview) &nbsp;·&nbsp; [◎ Motivation](#motivation) &nbsp;·&nbsp; [☰ Challenges](#the-challenges) &nbsp;·&nbsp; [★ Results](#results) &nbsp;·&nbsp; [◬ Reading Order](#reading-order) &nbsp;·&nbsp; [☷ Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [© License](#license) &nbsp;·&nbsp; [⌬ About](#about-this-repository) &nbsp;·&nbsp; [✦ Acknowledgments](#acknowledgments)

</div>

---

<div align="center">

**◈ The competitions:** [Andrews–Curtis](https://github.com/Amey-Thakur/SAIR-ANDREWS-CURTIS-CHALLENGE) &nbsp;·&nbsp; [Lean Kernel](https://github.com/Amey-Thakur/SAIR-LEAN-KERNEL-CHALLENGE) &nbsp;·&nbsp; [Mathematics Distillation](https://github.com/Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE) &nbsp;·&nbsp; [Inverse Galois](https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24) &nbsp;·&nbsp; [Modular Arithmetic](https://github.com/Amey-Thakur/SAIR-MODULAR-ARITHMETIC-CHALLENGE)

---

### ⌬ [SAIR Foundation](https://sair.foundation/)

**Open competitions on unsolved problems in mathematics and computation**

*An index of the questions asked, the methods brought to them, and the point at which each one stopped.*

</div>
