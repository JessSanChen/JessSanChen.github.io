# Inventory & positioning memo

Read of the 11 PDFs in `projects-papers/`. Dates marked `?` are guesses from
context — confirm them.

---

## The headline

**Your profile is far more coherent than "CS major who did a banking year." Seven
of these eleven papers are the same field.**

Uber Stable, the compute marketplace, PRIMES, the winner's-curse auctions, the
fairness-under-gaming paper, RN-SOAR, and the insurance claim-denials model are
all **EconCS**: what happens to a learning or allocation system when the agents
inside it are strategic. Matching, auctions, incentive-compatible selection,
strategic classification, sequential decisions under misaligned incentives. You
have been writing one dissertation-shaped body of work across five courses
without labeling it.

That matters for three reasons:

1. **"AI research generalist" undersells you.** It's the position of someone
   with a scattered record. You don't have one. *"I work on incentives in
   multi-agent learning systems"* is narrower, more credible, and immediately
   legible to the labs and PhD programs that would want you.
2. **It makes the banking year an actual asset rather than a rhetorical one.**
   In my first draft I had you arguing that restructuring taught you rigor —
   true but generic, and every banker says it. The real version: you work on
   mechanism design, and you spent a year inside the largest strategic-behavior
   laboratory there is, watching sophisticated parties bargain under asymmetric
   information with real money at stake. For an EconCS researcher that is
   *domain experience*, not a detour. Nobody else in the applicant pool has it.
3. **It gives the China/Taiwan work a home.** Hukou and cross-strait brain drain
   aren't a hobby wing — they're empirical political economy, same intellectual
   family. A site organized around *incentives, institutions, and learning
   systems* holds all three clusters without strain.

The neuroscience is the one genuine outlier. See the note at the bottom.

---

## Track 1 — EconCS / multi-agent systems (the spine)

| Work | What it is | Verdict |
|---|---|---|
| **Uber Stable: Formulating the Rideshare System as a Stable Matching Problem** — Acharya, **Chen**, Xiao. arXiv:2403.13083 [cs.MA], Mar 2024 | Gale–Shapley deferred acceptance for rider–driver matching over multiple periods; preference-aware assignment balancing revenue against equitable driver income. | **Lead with this.** It's a real preprint with a real arXiv ID. Publications outrank everything else on a research site, and right now it's invisible. |
| **PRIMES: An Incentive-Aligned Agent Selection Strategy for Federated Learning** — **Chen**, Ni, Wu. CS 243 | Clients selected on next-step loss, paid on *global* performance, so truthful reporting is the best response. Built on Flower FL with a separate gRPC back-channel. 1.5–2× accuracy per round vs. random and Oort clipping; 10–33% faster convergence. | **Strongest unpublished piece.** Mechanism design plus a real distributed implementation plus baselines you beat. This is the one that convinces a skeptical reader you can actually build. Consider a workshop submission. |
| **Multi-Dimensional Preference Ordering for a Stable Compute Marketplace** — **Chen** & Wu. CS 236r | Pricing/matching for a compute marketplace where users report multi-dimensional, possibly stochastic preferences. Finds stability decays exponentially in report noise, and — nicely — that stability doesn't predict social welfare. | **Strong.** The negative result is the interesting part; don't bury it. Code is public. |
| **Countering the Winner's Curse in Aggregated-Signal Common-Value Auctions** — **Chen** & Huang. CS 237 | Auction theory in the aggregated-signal setting rather than Bulow–Klemperer's max-signal setting. Pure NE in toy games, a novel inclusive posted-price design, and a clean asymmetric result: no bidder bids more than 2× their private signal. | **Strong, and the most "theory" of the set.** That 2× bound is a quotable result. |
| **Achieving Fairness in Multi-Round Online Gaming** — **Chen** & Wu. CS 226 | Extends Bechavod et al.'s strategic-interaction setting; shows fairness degrades when agents game features at asymmetric cost, then repairs it. | **Solid.** Overlaps thematically with PRIMES — present them as a pair rather than as two separate entries. |
| **RN-SOAR: Robust Nurse Scheduling in the Online Setting using Adaptive RL** — **Chen**, Yu, Zhong. CS 2880, Fall 2024, advised by Milind Tambe & Shresth Verma | Online RL for nurse scheduling under uncertainty. | **Include, and name Tambe.** Working under him is a credential in AI-for-social-impact; the advisor line does real work here. |
| **Claim Denials: Health Insurance from a Differential Learning Perspective** — 5 authors, Apr 2025 | Insurers exploit information asymmetry by partially denying claims; consumers Bayesian-update beliefs and drop out. Non-monotonic risk-pool evolution. | **Include, lower.** Genuinely interesting result. Five authors dilutes attribution — state your contribution explicitly. |

## Track 2 — China / Taiwan political economy

| Work | What it is | Verdict |
|---|---|---|
| **Impact of China's 2014 Hukou Reforms on City-Level Population Growth** — Ec 970, May 2025, advised by Andrés Maggi | Diff-in-diff on 2010–2023 city panels for Zhejiang and Sichuan, with reform intensity **hand-coded city by city from local regulations and news** rather than inferred from headline thresholds. Finds no average population gain; sub-provincial hubs keep growing while prefecture cities keep shrinking. | **Include prominently.** The methodological care is the selling point: you rejected the literature's proxy and built the treatment variable yourself, then scraped provincial yearbooks off bureau sites through a Hong Kong VPN. That's research temperament, and it's a much better story than the coefficient. |
| **The Cross-Strait Brain Drain: Resiliency of the Taiwanese Academia-Industrial Complex Against Geopolitical Risk** — Gov 1982, Dec 2023 | Argues geopolitical risk, more than wages, drives high-skilled semiconductor migration between Taiwan and China. | **Include.** Timely, personally grounded, and distinctive. Reads as someone with a real view, not a course requirement. |
| **Chinese Alignment Strategy (balance-of-threat)** — Gov 1982 midterm | Sino-Soviet alliance → split → US rapprochement through Walt's balance-of-threat framework. | **Cut, or fold into the above.** It's a competent midterm essay. A timed exam essay on a site next to an arXiv preprint dilutes rather than adds. |

## Track 3 — Neuroscience

| Work | What it is | Verdict |
|---|---|---|
| **Neuroanatomical Mapping of Upstream Targets of Somatostatin in the DMV/NTS via Cre-Dependent PRV** — Georgetown, Drs. Sahibzada & Bellusci, Dec 2019 | Cre-dependent pseudorabies virus retrograde tracing in Sst-Cre mice; confocal analysis mapping gastric→hypothalamus/amygdala vagal circuits. | **Include, dated honestly.** This is real wet-lab circuit neuroscience with named mentors — but it's from the TJHSST mentorship program in 2019, i.e. high school. Label it that way and it reads as precocious. Present it undated next to 2025 work and a reader who does the arithmetic feels misled. |

**On the neuroscience generally:** you named it as an interest, but this is the
only artifact, and it's seven years old. Two honest options — pick one, don't
straddle. Either **(a)** present it as formative history, one page, clearly
dated, no claim to current expertise; or **(b)** if you actually want NeuroAI
roles, the site can't carry that claim on a 2019 paper. You'd need one new thing
— a reproduction, an analysis on public neural data, a serious literature
review. The `spikeinterface_datasets` folder on your Mac suggests you may have
already started. Worth telling me.

---

## Proposed site structure

```
Publications        Uber Stable (arXiv)
Research            EconCS: PRIMES · compute marketplace · winner's curse
                    · fairness under gaming · RN-SOAR · claim denials
Political economy   Hukou reform · cross-strait brain drain
Earlier work        Neuroanatomical mapping (2019)
```

Three clusters, honestly labeled. The reader's takeaway should be: *she works on
incentives in learning systems, she has a real empirical streak, and she can
build the thing as well as prove things about it.*

---

## Order of work

1. **Fix the deploy** (see chat — Pages source setting, one click).
2. **Confirm the positioning.** Everything downstream depends on it.
3. **Project pages**, EconCS first. I have the abstracts; stubs are pre-filled.
4. **Rewrite the About and Research pages** around the real through-line.
5. **LaTeX standardization** — one two-column template, all papers rebuilt.
6. **Defensibility pass** — strengthen the arguments, not just the formatting.
7. **Hetzner** — separately, for the source files the standardization needs.
