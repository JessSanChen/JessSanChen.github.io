---
title: Spectre — Multi-Agent Red-Teaming for Defense
kind: Build
venue: SCSP AGI Hackathon — $25,000 first prize
date: 2024-10
featured: true
blurb: A multi-agent system that generates diversified red-team prompts across defense applications and attack styles. It jailbroke the Air Force Research Lab's LLM.
links: Code|https://github.com/JessSanChen/SpectreRedTeaming
---

**First prize ($25,000), SCSP AGI Hackathon**, sponsored by former Google CEO Eric Schmidt. October 2024.

## What it does

Red-teaming an LLM by hand produces attacks that all look like the person who
wrote them. Spectre uses a **multi-agent system to generate diversified
adversarial prompts**, spreading coverage across defense application domains and
across attack styles rather than depth-first down whatever the operator thought
of.

It jailbroke the **Air Force Research Lab's LLM** during the event.

## How it works

[TODO: the one technically interesting thing — how agents are specialized, how
diversity is enforced or measured, how successful attacks feed back. Every
hackathon project has exactly one interesting idea; this is yours.]

## Why it's here

Adversarial prompt generation is a multi-agent search problem, and it's the same
question as the rest of my research from the other direction: what does a system
do when the agents inside it are optimizing against it?

## Honest status

Built in a weekend. Prototype, not a hardened tool.
