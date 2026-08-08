---
title: Fairness in Multi-Round Online Gaming with Strategic Agents
kind: Research
venue: CS 226, Harvard
date: 2024-05
blurb: Fairness guarantees break down when agents can strategically modify reported features at asymmetric cost — and can be restored.
links: PDF|../files/fairness-gaming.pdf ; Code|https://github.com/JessSanChen/226-fairgaming
---

**Jessica Chen, Gary Wu.** *CS 226, Harvard.*

## Summary

Algorithmic fairness work on lending almost universally assumes applicant
features are static and the lender gets one shot at a fair classifier. Bechavod
et al.'s "Gaming Helps!" relaxes that: agents observe the current model and
strategically modify their reported features, at a cost, to improve their odds.

The cost functions aren't symmetric. Advantaged agents can modify cheaply;
disadvantaged agents pay more for the same movement. We show that the standard
online gaming setting is **not** fair under this asymmetry, then augment AIF360's
fairness metrics with feature dropping and partial-data robustness to restore
fairness across several definitions simultaneously.

Read this alongside [PRIMES](primes-federated-learning.html) — both are about
what happens to a learning system when the agents inside it have their own
objectives.

## My contribution

[TODO]
