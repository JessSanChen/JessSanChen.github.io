---
title: Multi-Dimensional Preference Ordering for a Stable Compute Marketplace
kind: Research
venue: CS 236r, Harvard
date: 2024-12
blurb: Matching stability decays exponentially in preference-report noise — and stability turns out not to predict social welfare.
links: PDF|../files/compute-marketplace.pdf ; Code|https://github.com/JessSanChen/computatemarketplace
---

**Jessica Chen, Gary Wu.** *CS 236r, Harvard.*

## Summary

Proposals for compute marketplaces (DeepMarket, CrowdFL) sketch the architecture
but leave the pricing and matching algorithms unspecified — which is where the
difficulty actually lives. Training jobs have complex, multi-dimensional
requirements, so users can't be expected to report a clean preference ordering
over asking price and training duration.

We model users reporting multi-dimensional preferences with stochastic noise and
indifference groups, and measure what that does to a Gale–Shapley market.

**Three results:** stability rates decay exponentially in both report noise and
indifference-group size; stability does *not* predict social welfare in this
system; and collapsing multi-dimensional preferences to one dimension before
matching reliably generates marketplace revenue.

The middle result is the interesting one — stability is the standard objective in
matching-market design, and here it comes apart from the thing you actually care
about. Lead with it.

## My contribution

[TODO]
