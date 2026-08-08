---
title: HackRF Crystal Calibrator
kind: Build
venue: Personal project
date: 2021-05
blurb: Calibrating a software-defined radio's crystal oscillator via LTE cell search, after finding a large frequency offset while spoofing GPS.
links:
---

## What happened

While spoofing GPS signals with a HackRF One and a custom GNU Radio flowgraph, I
found a large frequency offset — the device's crystal oscillator was off enough
to break the work. Rather than eyeball a correction, I built a tool that
calibrates the crystal by searching for LTE cells, whose carriers are
tightly specified and can serve as a frequency reference.

[TODO: how far off was it, and how close did calibration get you?]
