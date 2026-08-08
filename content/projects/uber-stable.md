---
featured: true
title: Uber Stable — Formulating the Rideshare System as a Stable Matching Problem
kind: Publication
venue: EAAMO 2024 (ACM Conf. on Equity and Access in Algorithms, Mechanisms, and Optimization) — from CS 136
date: 2023-12
blurb: Deferred acceptance applied to rider–driver matching, trading system efficiency against equitable driver income.
links: arXiv|https://arxiv.org/abs/2403.13083 ; PDF|../files/uberstable.pdf ; Code|https://github.com/JessSanChen/
---

**Rhea Acharya, Jessica Chen, Helen Xiao.** *Published at EAAMO 2024. arXiv:2403.13083 [cs.MA], March 2024. Originating in CS 136, Economics and Computation.*

## Summary

Rideshare platforms are, underneath the app, a bipartite matching problem between
riders and drivers — but the matching is usually run greedily on proximity, which
quietly concentrates income among drivers who happen to sit in attractive
locations. We apply the Gale–Shapley deferred acceptance algorithm to a static
matching repeated over time periods, with preferences built from passenger
willingness-to-pay, driver preferences, and location attractiveness, and compare
against random and closest-driver matching.

We compare against random matching, closest-neighbour matching, and the Boston mechanism, on total revenue, revenue per ride, and the standard deviation of driver income — and examine what happens when the system prioritizes proximity to passengers versus distance from city centre.

[TODO: add the headline numbers — how much driver income inequality falls, and
what it costs in total system revenue. That tradeoff is the paper's point and it
should be in this paragraph.]

## My contribution

[TODO: state plainly which parts were yours.]
