---
title: Spike Sorting and Functional Connectivity Reconstruction from Flexible Mesh Probes
kind: Research
venue: Jia Liu Lab of Bioelectronics, Harvard SEAS
date: 2022-12
blurb: Rebuilt the lab's electrophysiology pipeline in SpikeInterface and used GLMCC to infer monosynaptic connections from chronically recorded mouse motor cortex.
links:
---

**Jessica Chen.** *Machine learning research assistant, [Jia Liu Lab of Bioelectronics](https://liulab.seas.harvard.edu/),
Harvard SEAS. February 2022 – early 2023.*

<div class="callout">
<p>No paper came out of this — it was undergraduate research assistance, and I'm
presenting it as that. What it produced was working pipeline code and a set of
analyses, which is the honest description.</p>
</div>

## Context

The lab builds flexible, tissue-embedded mesh electronics that record from the
same neurons over long timescales without the glial scarring that displaces
rigid probes. That stability is the point: it makes it possible to ask what a
population of neurons does across weeks rather than a single session.

I worked on the analysis side of that data.

## Electrophysiology pipeline

The experimental preparation was a head-fixed, water-restricted mouse trained to
pull a joystick past a threshold for a sweetened-water reward, with 32-channel
Intan recordings running alongside the behavioral signal.

I inherited a MATLAB preprocessing pipeline, audited which recording sessions
had complete variable sets, fixed a reshape bug in the trial-segmentation step,
and then **rebuilt the pipeline in Python on SpikeInterface** against the lab's
`mesh_probe` geometry — running MountainSort and Kilosort and then manually
curating the output unit-by-unit on waveform shape, merging over-split units and
dropping noise clusters across sessions.

Manual curation is unglamorous and it's where most of the real judgment in
extracellular ephys lives. [TODO: one sentence on what you learned about when to
trust an automated sorter — that's the interesting takeaway.]

## Functional connectivity

With sorted spike trains, I moved to **GLMCC** (Kobayashi et al., *Nature
Communications* 2019), which fits a GLM to the cross-correlogram between neuron
pairs to estimate monosynaptic connection strength in PSP units and separate
true synaptic coupling from correlation driven by shared input.

I got the reference implementation running on the lab's data and tuned the
correlogram window and bin width for our sampling rate, recovering candidate
excitatory connections between units. **Parameter tuning wasn't finished** — the
defaults are set for a different recording regime, and identifying the right
ones for chronic mesh-probe data was where I left off.

I also evaluated a **second-order memristor array** (tantalum-oxide, where the
device's internal temperature state gives native STDP) as a real-time
alternative to GLM-based reconstruction for high-channel-count recordings.

## Spatial transcriptomics

My first semester was on the lab's other side: graph-attention autoencoders for
spatially resolved transcriptomics. I presented STAGATE and DeepMAPS at journal
club and wrote a [PRISE] proposal to extend the lab's STARmap/ClusterMap work to
ligand–receptor cell–cell interaction using transformers. The proposal didn't
turn into a finished project.

## Why this is on the site

[Suggestion, in your words: population recordings and artificial networks pose
the same inference problem — you observe activity and have to recover the
computation, without access to the source code. Spike sorting, connectivity
inference from correlational data, and knowing when a method is telling you
about the system versus about your preprocessing are the same skills
interpretability work needs.]
