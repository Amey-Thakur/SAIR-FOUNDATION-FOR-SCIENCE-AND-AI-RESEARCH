# viXra submission brief

One copy block per form field, in the order the form presents them.
Generated from the manuscripts, so nothing here is retyped and the brief
cannot drift from the paper.

**Submit in this order: II first, on its own.** It is the most conventional
mathematics paper of the five and the cleanest category fit, so it is the best
probe of whether the account, the category and the PDF layout are accepted.
Let it appear before sending the rest; on ai.viXra.org no confirmation within
48 hours means the submission was not accepted, and one listing already
carries the admin note "Further repetition will not be accepted!", so firing
five at once from a fresh account is an avoidable risk. Then I, III, IV, V.

## Which archive

viXra's front page states it plainly: "viXra.org only accepts scholarly
articles written without AI assistance. Please go to ai.viXra.org to submit new
scholarly article written with AI assistance". The form repeats it and the
moderators enforce it, stamping November 2026 listings with that redirect.
These manuscripts were drafted with substantial AI assistance, so on the
archive's own rule they go to **ai.viXra.org**
(`fs23.formsite.com/viXra/ai_submit`), whose only extra requirement is a list
of scientific references in the PDF. Every paper here has a bibliography, and
the largest PDF is 0.37 MB against a 5 MB cap.

## Fields that are the same every time

- **PDF submission method:** Upload.
- **Your e-mail address:** the same address for all five. Replacements and
  withdrawals are only accepted from the address that made the original
  submission, and ai.viXra.org allows four replacements, then none.
- **Author(s):** `Amey Thakur`. There is no affiliation field.
- **Other instructions:** blank.
- Upload the **PDF only**. viXra requires one self-contained PDF and rejects
  extra files, so never the `arxiv-submission.tar.gz`.
- **One category, final at submission.** There is no cross-listing; the
  moderators may move a paper they judge misfiled.
- **No DOI.** You get `viXra:YYMM.NNNN` and the abstract page URL is the
  citable reference.

---


## Paper II - Inverse Galois (IGP24)

**PDF to upload:** `papers/II-inverse-galois.pdf` (?, ? pages). Source `SAIR-INVERSE-GALOIS-ARXIV/main.tex`, was bound for arXiv `math.NT`.

**Science Category** - select from the dropdown, one only:

```
Mathematics - Number Theory
```

**Title of Paper**

```
Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra
```

**Author(s)**

```
Amey Thakur
```

**Abstract** - 286 words, limit 400. Plain text; paragraph breaks are discarded by viXra, so paste as one block.

```
Naming the Galois group of a degree-24 integer polynomial ordinarily demands resolvent computations inside a computer algebra system. This paper presents a statistical alternative that needs only polynomial factorisation modulo small primes, and evaluates it against 576,682 polynomials whose groups the SAIR IGP24 evaluation server computed independently in Magma. The method reads the multiset of Frobenius cycle types at 60 primes as a sample from the group's own cycle-type distribution, which the Chebotarev density theorem licenses, then scores that sample against empirical profiles of candidate groups drawn by product-replacement sampling. Within its domain the classifier reaches 69.0% top-1 and 88.7% top-3 accuracy at 53 ms per polynomial. Its practical value rests on a calibrated abstention rule: required to beat the runner-up by a log-likelihood margin of 8, the classifier commits on 12.7% of inputs and answers correctly on 76 of 76 commitments, a 95% Wilson lower bound of 95.2% on precision. A separability bound explains these figures instead of merely reporting them. The Bhattacharyya coefficient between the cycle-type distributions of two groups caps the accuracy of every possible method at a given number of primes, and group theory alone computes it, before any polynomial is factored. It predicts two things and measurement confirms both: accuracy falls from 100% to 23.5% as a group's nearest competitor closes in, respecting that cap in every band, and 60 primes is too few, since accuracy is still climbing there. Two further limitations get the same treatment. Profiles cover 24T_1 through 24T_8000, and only 9.4% of the labelled corpus falls in that range, so coverage rather than accuracy binds deployment. Novelty counted in fingerprints overstates novelty in groups by more than an order of magnitude. All code and data are public.
```

**Number of pages**

```
?
```

**Comment**

```
? pages, 5 figures, 7 tables
```

**Other instructions** - leave blank.

---

## Paper I - Modular Arithmetic

**PDF to upload:** `papers/I-modular-arithmetic.pdf` (?, ? pages). Source `SAIR-MODULAR-ARITHMETIC-ARXIV/main.tex`, was bound for arXiv `cs.LG`.

**Science Category** - select from the dropdown, one only:

```
Computational Science - Artificial Intelligence
```

**Title of Paper**

```
Place Value, Not Position: Length Generalisation Limits in Neural Modular Arithmetic
```

**Author(s)**

```
Amey Thakur
```

**Abstract** - 271 words, limit 400. Plain text; paragraph breaks are discarded by viXra, so paste as one block.

```
A transformer is told where a digit sits, and that choice decides whether it can still add when the numbers get longer. Absolute and rotary encodings describe a digit by its index in the sequence, which moves when an operand is padded; an abacus encoding describes it by its significance, which does not. This paper compares five encodings on one architecture, one dataset, one optimiser and one seed, across three tasks that differ only in the operation: a+b, (a+b) p and (a x b) p. Every model trains on operands of two to four digits and is scored by exact match on two to eight. Three findings follow. Place value generalises where position does not, but barely: the abacus arms answer 1.4% and 2.1% of problems at unseen widths where both positional arms answer none of 4,000. The gain is small for a reason that has nothing to do with place value. The significance embedding inherits the problem it was meant to solve: only the rows the training widths touch are ever learned. Training that table over a wider range raises out-of-distribution accuracy to 38.3%, with in-distribution accuracy still at 100.0%. And none of it reaches modular multiplication, where all five encodings score between 1.8% and 3.2% inside the training widths and zero beyond, which places the difficulty in the arithmetic rather than the representation. A fourth result concerns the architecture this work submitted to the SAIR Modular Arithmetic Challenge: re-injecting the significance signal at every layer is no better than injecting it once, and on modular addition it is far worse, 24.9% against 76.0%. All code and data are public.
```

**Number of pages**

```
?
```

**Comment**

```
? pages, 4 figures, 4 tables
```

**Other instructions** - leave blank.

---

## Paper III - Andrews-Curtis

**PDF to upload:** `papers/III-andrews-curtis.pdf` (?, ? pages). Source `SAIR-ANDREWS-CURTIS-ARXIV/main.tex`, was bound for arXiv `math.GR`.

**Science Category** - select from the dropdown, one only:

```
Mathematics - Algebra
```

**Title of Paper**

```
Length as Priority, Not Constraint: Search Geometry of the Andrews-Curtis Challenge Pool
```

**Author(s)**

```
Amey Thakur
```

**Abstract** - 319 words, limit 400. Plain text; paragraph breaks are discarded by viXra, so paste as one block.

```
A search for an Andrews-Curtis reduction that bounds the total length of the relators is defeated by the bound rather than by its budget, and this paper measures the difference on the 10,115 balanced presentations of the SAIR Andrews-Curtis Challenge pool. Ten presentations whose shortest reduction is known are returned at exactly that length, in 0.4 to 2.6 seconds and 2,028 to 2,456,933 search states, by a search with no length bound at all, ordered instead by the priority L(P) + w d(P) on total relator length L and moves spent d, at w = 12. At w = 4 eight of the ten are exact; at w = 0 the same search returns 32 moves against an optimum of 15. That the bound and not the budget is the defect is then shown directly: on 196 presentations nobody has reduced, a bounded search closed its entire space in 256 to 897,279 states, so no reduction of any of them stays within its starting length, and for 33 none stays within four of it. Three further measurements bound what a search of this family can reach. The priority is at least w d, which caps reachable depth, and w = 12 solves every record of 16 moves or fewer and none of 35 at records 121 to 300. The backward half of a bidirectional search never reads the presentation, a fact one recurring state count, 7,226,201 across eight presentations of one run, makes visible; that permits amortisation and also bounds it, since one precomputed set of 22,000,000 states contained 2 of the 10,115 presentations. Under a tie rule that halves a record's value for each further team holding it, competence and point value are anti-correlated by construction: 146 held records paid 3.16 points while 1,012 unheld ones were worth about 388. One bounded non-existence statement is reported with its hypotheses stated in full. All code and data are public.
```

**Number of pages**

```
?
```

**Comment**

```
? pages, 5 figures, 10 tables
```

**Other instructions** - leave blank.

---

## Paper IV - Equational Distillation

**PDF to upload:** `papers/IV-equational-distillation.pdf` (?, ? pages). Source `SAIR-MATHEMATICS-DISTILLATION-ARXIV/main.tex`, was bound for arXiv `cs.LO`.

**Science Category** - select from the dropdown, one only:

```
Mathematics - Set Theory and Logic
```

**Title of Paper**

```
The Verdict Is Free: A Saturated Benchmark for Equational Implication, and What It Leaves to Prove
```

**Author(s)**

```
Amey Thakur
```

**Abstract** - 292 words, limit 400. Plain text; paragraph breaks are discarded by viXra, so paste as one block.

```
A benchmark that asks whether one equational law implies another can be saturated without anyone noticing, because the question it appears to pose is not the question it scores. We measure this on the 1,669 distinct problems of the public sets shipped with the SAIR Mathematics Distillation Challenge. A lookup against the Equational Theories Project lattice settles 100% of them at 100% accuracy in 0.4 seconds with no model call and no search, so the true/false verdict carries no information about a solver. What the competition actually scores is a machine-checked Lean 4 certificate, and that remains open. Separating the two relocates the difficulty precisely, and measuring the certificate-producing stages on the same fixed set shows where it sits. A finite counterexample search settles 800 problems, which is 47.9% of the set but 94.1% of the 850 problems it can possibly settle, since a counterexample refutes an implication and can never establish one. A syntactic collapse rule settles 244, which is 29.8% of the 819 true problems. Neither stage disagreed with ground truth on any problem, as a certificate-producing method should not. Splitting both figures by the benchmark's own difficulty label shows the search holding, at 86.3% on the hard false problems, while the collapse rule settles 48.6% of the easy true problems and 1 of 319 hard ones, so its aggregate describes no actual regime. The hard true implications are untouched, and that is where the remaining work is. We also report a measurement error of our own that inverted a result: an exception swallowed inside a harness reported counterexample search as firing on 0 of 1,669 problems rather than 800, a figure implausible enough to check and wrong in the direction that flatters the conclusion. Code and data are public.
```

**Number of pages**

```
?
```

**Comment**

```
? pages, 2 figures, 5 tables
```

**Other instructions** - leave blank.

---

## Paper V - Lean Kernel

**PDF to upload:** `papers/V-lean-kernel.pdf` (?, ? pages). Source `SAIR-LEAN-KERNEL-ARXIV/main.tex`, was bound for arXiv `cs.LO`.

**Science Category** - select from the dropdown, one only:

```
Computational Science - Data Structures and Algorithms
```

**Title of Paper**

```
A Whole Table Row in One Natural Number: Kernel-Checked Dynamic Programming with a Proved Width Bound
```

**Author(s)**

```
Amey Thakur
```

**Abstract** - 328 words, limit 400. Plain text; paragraph breaks are discarded by viXra, so paste as one block.

```
A proof assistant checks a computation by reducing it, so the data structure a verified algorithm is written over decides the cost of being checked, not only the cost of running. This paper measures that cost for one task with a locked specification: counting the partitions of n in Lean 4, where the answer must come with a machine-checked proof that holds for every n. Three designs compute the same recurrence. Evaluating the specification as written performs 672,182 primitive steps at n = 36, because every path to a table cell re-derives it. Holding each table row as a list brings that to 69,768, since a cell is then looked up rather than recomputed, but indexing position m of a list costs m constructor matches. Holding the whole row in a single natural number, with the entry for m in the m-th field of w bits, brings it to 716: a factor of 939 against the specification and 97 against the lists, and in reduction wall time 57.64 seconds against 0.07. The representation is sound only if no field overflows, which is a theorem and not an assumption: peeling one term off the specification's own sum yields partAux (k+1) m = partAux k m + partAux (k+1) (m - (k+1)), from which partAux k m 2^m+k follows, so w = 2n+1 bits suffice. The development uses core Lean only and proves its statement for every n. Asking the same question of the other seven problems found something the packing does not address: two of the eight shipped reference starters cannot be reduced at any judged size, both reaching well-founded recursion through Nat.minFac, so both score nothing while compiling with correct proofs. The competition's own metric has since scored this entry at 131,460,833 units against 3,396,012,941 for a narrow-operand alternative proved the same way, a factor of 25.8. The step count is blind to a field-width tuning worth a further 3.4 in wall time. Code and data are public.
```

**Number of pages**

```
?
```

**Comment**

```
? pages, 3 figures, 6 tables
```

**Other instructions** - leave blank.

---

## After submitting

Record each `viXra:YYMM.NNNN` and its abstract-page URL. Those fill the
*id pending* cells in this repository's README Papers table.

The five `SAIR-*-ARXIV` repositories can then be deleted. The compiled PDFs
are archived here in `papers/`, so the published artifacts survive; the LaTeX
sources, figure generators, number-checking tools and the CI that is the only
place these papers compile do not. A PDF does not reconstruct into a source.
