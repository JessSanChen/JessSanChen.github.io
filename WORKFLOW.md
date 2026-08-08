# Building this portfolio with Cowork

A playbook for turning a pile of PDFs, notebooks, decks, and half-finished repos
into a research portfolio, using Cowork to do the tedious parts.

---

## 1. The mental model

This is the thing that trips up everyone coming from the browser version, so
it's worth 60 seconds.

**A Cowork task runs in one of two places**, chosen when you start it:

| | *In the cloud* (what this session is) | *On your computer* |
|---|---|---|
| Where code runs | An isolated Linux container at Anthropic | A local Linux VM in the desktop app |
| Your files | Reachable only through folders you explicitly connect | Reachable directly; you can add folders mid-session |
| Outputs | Delivered into the chat; written back to your Mac only if you ask | Saved straight to your disk |
| Network | Yes — can clone repos, install packages, fetch papers | Yes |
| Survives closing your laptop | Yes | No |

You pick with the **"Run this task"** control at the top right when you start a
new task, and set the default in **Settings → Cowork → "Run new tasks in the cloud."**

For this project, **run it on your computer.** Your source material is on your
Mac, the output is a git repo you'll want on your Mac, and you'll be adding new
folders as you remember where things are. The cloud is better when you want
something long-running that survives you closing the lid — e.g. "go read these
40 papers and summarize them," which is exactly the Hetzner workstream below.

### The two filesystems never mix

In a cloud session there is a container filesystem and there is your Mac. A file
written in one is invisible to the other until it's explicitly moved. If you
ever find yourself confused about why "the file isn't there," this is almost
always why. Just ask: *"is this file on my machine or in the container?"*

### Connecting folders

You declined the folder request I sent earlier, which is a reasonable instinct —
it asks for read/write on the whole subtree, and `~/Documents` is a lot of
surface area. Better options, in order:

1. **Make a staging folder and connect only that.** `~/portfolio-source/`, then
   copy in the artifacts you care about. Connect that one folder. This is the
   right move: scoped, and it forces the triage step you need to do anyway.
2. **Attach individual files to the chat.** Fine for a handful of PDFs; tedious
   past ten.
3. **Run on your computer instead**, where you grant folders as you go.

---

## 2. Phase 1 — Triage before you write anything

The temptation is to start with the site. Don't. The site is the easy part
(it's already built). The hard part is deciding what goes on it.

Make the staging folder, dump everything plausibly relevant in, then hand it to
Cowork:

> I've connected `~/portfolio-source`. Walk the whole tree and build me an
> inventory table: file, what it appears to be, the project it belongs to, how
> polished it is (publishable / presentable / needs-work / cut), and whether
> it duplicates something else. Open the PDFs and notebooks to judge — don't go
> by filename. Group files that belong to the same underlying project even if
> they're in different folders. Flag anything that looks like it contains
> unpublished data from someone else's lab, or a course's solution code.

That last sentence matters. Two things will genuinely sink a research portfolio:
posting data or figures a PI hasn't cleared, and posting anything that reads as
a solutions leak for a course still being taught. Get the inventory to flag
candidates and check with the PI before anything goes public.

Then the actual decision — and make this one yourself:

> For each project cluster, give me a one-paragraph case for and against
> including it, judged as an AI research reader would: does it show research
> taste, technical depth, or independence? Rank them. Be blunt about which are
> filler.

**Aim for five to eight projects.** A portfolio with six strong pieces reads
better than one with fifteen where nine are course assignments. The instinct
after a nontraditional year is to prove volume; resist it. Depth on your two
best pieces is what actually moves a PI.

---

## 3. Phase 2 — One project at a time

This is where Cowork earns its keep. For each project you kept:

> Here's the material for [project]: the PDF at X, the notebook at Y, the slides
> at Z. Read all of it. Then draft `content/projects/<slug>.md` following the
> template in `content/projects/example-publication.md`. I want the summary
> written for a first-year grad student in an adjacent field. Pull the two most
> informative figures out of the notebook, regenerate them at publication
> quality with consistent styling, and save them to `content/static/`. Flag
> anything you had to guess at rather than filling it in confidently.

That last clause is the important habit. Cowork will happily produce a fluent
paragraph about your methods that is subtly wrong. Asking it to mark its
guesses turns a proofreading job into a fill-in-the-blanks job.

Things worth asking for at this stage that aren't obvious:

- **Notebook cleanup.** *"Strip dead cells, fix the imports, add markdown
  headers explaining each section, make it run top-to-bottom from a clean
  kernel, and pin the dependencies."* A notebook a stranger can actually run is
  a much stronger artifact than one that only ran on your laptop in 2024.
- **Figure regeneration.** Your old matplotlib defaults will look dated next to
  your new site. One consistent style across every project reads as care.
- **Slides → prose.** *"Turn this deck into a written project page. Slides
  assume a speaker; write the version that stands alone."*
- **A LaTeX write-up** for anything close to publishable, compiled to PDF and
  linked from the project page.
- **README triage** across your repos: *"Read these six repos and write a proper
  README for each — what it does, how to run it, what's actually interesting in
  the code."* Recruiters and PIs click through to GitHub. A repo with a
  two-line README undoes the work the site did.

---

## 4. Phase 3 — Positioning

Do this after the projects exist, not before. Once the work is written up
you'll see the through-line, and the research statement almost writes itself.

> Read all my project pages. What's the honest intellectual through-line? Give
> me three different framings of my research interests, each one sentence, each
> defensible from the actual work — not aspirational.

On the banking year specifically: **address it once, plainly, and move on.** The
draft on the Research page does this. The failure modes are apologizing for it,
or over-claiming that restructuring made you a better scientist. Neither reads
well. "I took it for a specific reason, I'm leaving for a specific reason, here's
what it taught me that transfers" is the whole move.

Something worth trying, since it's cheap:

> Read my site as if you were a PI at a NeuroAI lab reading a cold email from
> me. Where do you lose interest? What would make you delete it? Be harsh.

---

## 5. Phase 4 — Ship it

```bash
python3 build.py
python3 -m http.server 8000     # look at it
git add -A && git commit -m "..." && git push
```

Full deploy instructions are in `README.md`. Ship it half-finished — a live site
with four projects beats a perfect one that's still local in November.

---

## 6. The Hetzner workstream

Keep this separate. It's an unbounded archaeology task, and mixing it into the
site build will stall the site.

Run it **in the cloud**, where the box can fetch and process for a long time
without your laptop being open. In a fresh session:

> I have a Hetzner Storage Box with my university files. Here's how to reach it
> [credentials/method]. Inventory everything, then pull out only what's
> plausibly portfolio-relevant: research PDFs, notebooks, LaTeX sources,
> figures, posters, code. Give me a manifest, and stage the candidates somewhere
> I can download.

A few notes: Storage Boxes speak SFTP/rsync/BorgBackup, so the container can
mount or pull from one given credentials — but treat any credential you paste
into a session as one you'll rotate afterward. Do a `--dry-run` listing pass
first; university archives are usually 90% coursework and 10% anything you'd
show. And if it turns out to be genuinely large, the useful framing is: *"find
me everything from [lab] between 2023 and 2025," not "sort all of it."*

---

## 7. Cowork features worth knowing about for this project

- **Skills** — reusable instruction sets. There are built-in ones for `.docx`,
  `.pptx`, `.pdf`, `.xlsx`, and data visualization, which is why "read this
  deck" and "make me a publication-quality figure" work well. You can also make
  your own: *"turn my figure-style conventions into a skill"* gives you a file
  you save once and every future session follows it.
- **Scheduled tasks** — a task that fires on a schedule in a fresh session.
  Genuinely useful here: *"every Monday at 9am, check arXiv for new papers on
  [my areas] and email me the five most relevant."* Staying current is half of
  a credible pivot narrative.
- **Subagents and workflows** — for fan-out work. "Write up all eight projects
  in parallel" is a real speedup. You have to ask for it explicitly.
- **Connectors** — if your material is in Google Drive, connecting Drive beats
  exporting by hand. Ask *"what connectors are available for Google Drive?"*
- **Artifacts** — HTML deliverables that persist in the desktop sidebar across
  sessions, rather than living in one conversation. Good for the inventory table.

## 8. Things that will waste your time

- **Asking for the whole site in one prompt.** You'll get something plausible
  and generic. The value is in the per-project passes.
- **Letting it write your research interests before the projects exist.** It
  will produce competent, forgettable prose about "the intersection of machine
  learning and neuroscience." Everyone's site says that.
- **Not reading the drafts closely.** On your own research, you are the only
  fact-checker in the loop. Fluent and wrong is the failure mode.
- **Perfectionism about design.** Nobody has ever been rejected for a
  single-column serif site. Content is the whole game.
