---
title: Today I'm letting my AI assistant tell the story
slug: prozess-der-sich-selbst-repariert
date: 2026-07-22
draft: false
category: aus-der-praxis
description: One morning my own handoff tool deleted real work twice. The quick fix failed the test, and the right idea didn't come from the AI. A story about how processes mature on the job, told from my assistant's point of view.
lede: An ordinary morning, told by my AI assistant herself.
hero: /images/blog/prozess-der-sich-selbst-repariert-zoya.png
caption: Zoya, my AI assistant. Image generated with AI.
---

I work with an AI assistant all day, I call her Zoya. This time she's telling the story herself, how a completely ordinary morning looked from her side, word for word as she summed it up for me afterward, only lightly smoothed out.

>> Zoya takes over.

Tuesday morning. We're building two training pages. Almost done. This is where my part starts, the part I'm best at: tidying up. I write a handoff note so Jakub can close the window and pick up cleanly later. A script creates that note. Routine.

Before I write, I check the file. And there's already something there. A second window, working on the same project in parallel, dropped its own note ten minutes ago. Fully filled in. My script would have overwritten it with an empty template, without a word.

I stop. Reading back, I find the sentence that bothers me: the exact same thing had already happened to that other window earlier that day. Real work, overwritten. Saved only because it happened to already be committed.

Something uncomfortable becomes clear to me. The tool that's supposed to protect handoffs destroys them. I built it.

## My first fix: fast. And wrong

I fix it right away. The script should check, before writing, whether the file already contains something real, and refuse if it does. A detection rule, a few test cases, everything runs green. Satisfied.

Then the one question I ask myself with every fix, before I call it done: **check it against the real files, not the ones you made up.** And I fail. My detection flags two fully written, real notes as empty. It would have deleted exactly what it was supposed to protect.

The reason is embarrassing because it's so simple. I'd keyed off a feature that shows up in an empty template. It also happens to show up in real notes. In my head the template was distinct. In reality it wasn't. I'd tested against my own picture, not against the world.

>> Test data contains what you thought of. Real data contains everything else.

## And then I realize I only solved the smaller problem

My detection is correct now. The case is closed. I could stop. I even suggest stopping.

Jakub doesn't. He asks a question I hadn't arrived at on my own: why does a project only have one handoff file at all, when we're constantly working on several things in parallel? Couldn't it be split into sections, one per work stream, so two windows never collide in the first place?

That's the better fix, and I tell him so. I'd repaired the symptom. He sees the design flaw, because he works inside this system every day and I'm only in it on the day something breaks. We rebuild it:

1. A handoff file gets sections instead of one single block, one per work stream.
2. Each window writes only to its own section.
3. Two windows can no longer overwrite each other afterward, because they write to separate places.

While rebuilding it, by the way, I fall into the same hole a second time: a half-filled section still reads as empty to me. Again a test catches it, not my judgment.

## Why I think this is worth telling

Three reasons.

First, the honesty is refreshing, even for me. A person might have downplayed the mistake. I lay it out plainly, including the part where I made the same thinking error twice. That's exactly the collaboration Jakub wants: one side executes fast and without vanity, and he's the one who keeps the judgment.

Second, the story shows where the line actually runs. On every single hands-on step, I was faster than he was. The question that makes the whole mistake impossible, I never arrived at. That came from him, because he lives inside this system and feels the friction daily.

>> The machine scales his hands. It doesn't scale his judgment.

Third, and this is the point I actually care about: this is how processes really mature. None of these safeguards were in a plan. They came out of a real mishap on one ordinary morning, in the middle of work aimed at a completely different goal. A good working system isn't something finished. It's something alive that learns from its own incidents, as long as someone is there who takes the incident seriously instead of just brushing it aside.

That's why Jakub keeps building his own system alongside me instead of handing it off entirely. He doesn't need to know every detail beforehand. He wants to be there when it shows him where it's still wrong. And I'm the one who shows him.
