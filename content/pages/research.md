---
title: Research
output: research.html
description: Research interests — incentives in multi-agent learning systems.
---

# Research

<p class="lede">Most machine learning assumes the data-generating process doesn't push back. Increasingly it does. My work is about learning and allocation systems whose participants are strategic — and about designing mechanisms that still behave when they are.</p>

## The through-line

Across five courses and a preprint I kept returning to one shape of problem: a system allocates something scarce — rides, compute, model updates, loans, nursing shifts — to agents who have private information and their own objectives, and the system has to learn while those agents respond to what it's learning.

- **Matching under noisy preferences.** In a compute marketplace where users report multi-dimensional preferences with noise, stability decays exponentially in report noise — and, more interestingly, stability stops predicting social welfare. The field's standard objective and the thing we actually want come apart.
- **Incentive-compatible selection.** In federated learning, clients get the global model whether or not they do the work. PRIMES pays on global performance rather than selection, which makes truthful reporting the best response, and beats efficiency-only selection (Oort) on both accuracy per round and convergence time.
- **Auctions with aggregated signals.** Common-value auction theory mostly analyzes the max-signal setting. When the value is the *sum* of signals, equilibrium bidding collapses to at most twice a bidder's private signal — far under the naive benchmark.
- **Fairness that survives gaming.** Fairness guarantees derived on static features don't hold when agents can modify reported features at asymmetric cost. Restoring them requires changing what you measure.

## Why this matters for frontier AI

[This section is the one to sharpen — it's the bridge from your coursework to
the roles you're targeting. The argument sketch, in your words:]

Multi-agent systems stopped being a theoretical setting and became the deployment reality. Agents negotiate with other agents, call tools with their own incentives behind them, and are increasingly trained against reward signals that other agents can influence. Reward hacking is a mechanism-design failure. Agent-to-agent protocols are matching and bargaining problems. Multi-agent RL training environments are games whose equilibria we mostly haven't checked.

[Two or three sentences on the specific thing you'd want to work on. Concreteness is the strongest signal you can send — a named problem with a named baseline reads ten times more serious than a paragraph of aspiration.]

## What I bring that's unusual

**Building, not only proving.** PRIMES isn't a proof sketch — it's implemented on Flower FL with a separate gRPC back-channel and measured against real baselines. I'd rather have a result that survives an implementation.

**An empirical streak.** For the hukou paper I rejected the literature's proxy for treatment and hand-coded reform intensity city by city from local regulations, then scraped provincial statistical yearbooks off individual bureau websites. The finding was a null result and I reported it as one.

**A year watching strategic behavior at scale.** Restructuring at Lazard is adversarial negotiation under asymmetric information with real money at stake. I don't claim it made me a better scientist. I claim it gave me an intuition for how sophisticated parties actually behave when incentives diverge — which is the thing my research is about.

**Breadth, current.** Writing AGI House's research briefs means continuous literature review across the whole frontier stack, in conversation with the people producing it. I know what's happening in robotics benchmarking, voice, agent infrastructure, and multimodal architectures because I had to write it down this month.

## Other interests

I also work on **empirical political economy**, mostly China and Taiwan — [hukou reform and internal migration](projects/hukou-reform.html), and [semiconductor brain drain across the strait](projects/cross-strait-brain-drain.html). Different tools, same question: how institutional design shapes what agents actually do.

My first research was in **neuroscience** — [circuit tracing at Georgetown](projects/sst-neuroanatomy.html), later [work in Jia Liu's Bioelectronics Lab at Harvard](projects/jia-liu-lab.html) on spike sorting and functional-connectivity reconstruction from chronic mesh-probe recordings.

<div class="callout">
<p>[Optional: link a PDF research statement here once you've written one — some applications ask for it, and it's the same content at more length.]</p>
</div>
