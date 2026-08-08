---
featured: true
title: PRIMES — Incentive-Aligned Agent Selection for Federated Learning
kind: Research
venue: CS 243, Harvard
date: 2023-12
blurb: Paying federated clients on global performance rather than selection makes truthful reporting the best response — and converges 10–33% faster.
links: PDF|../files/primes.pdf ; Code|https://github.com/JessSanChen/
---

**Jessica Chen, Jared Ni, Gary Wu.** *CS 243, Harvard.*

## Summary

Federated learning assumes clients honestly do the work. They have no reason to.
A client that free-rides — training on corrupt data, or barely training at all —
still receives the final global model. Prior work on participant selection (Oort
and successors) optimizes *which* clients to pick for efficiency, but treats
their reports as truthful.

PRIMES changes what clients are paid for. Selection is on next-step loss, but
payment is a function of performance on global test data. Because payment
follows global performance rather than selection, misreporting to get selected
stops being profitable and truthful reporting becomes the best response.

We implemented it on Flower FL with a separate gRPC back-channel for the
incentive layer. Against random selection and Oort's clipping method, PRIMES
reaches **1.5–2× accuracy per round** and converges **10–33% faster** across
client populations with varying degrees of data corruption.

## Why this one matters

[This is your strongest unpublished piece — mechanism design plus a working
distributed implementation plus baselines you beat. Expand the method section
and add the convergence figure. Worth a workshop submission.]

## My contribution

[TODO]
