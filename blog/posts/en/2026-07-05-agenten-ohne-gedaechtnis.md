---
title: My AI agents had no memory
slug: agenten-ohne-gedaechtnis
date: 2026-07-05
draft: false
category: aus-der-praxis
description: Ten AI agents, 27 research missions, and the full reports were all gone. Why agents forget everything by default, what that costs, and the fix that takes ten minutes.
lede: I found out I was running an intelligence agency that shreds its own reports.
---

## The intelligence agency that shreds its own reports

For over a month I've had a fleet of ten AI agents running parallel missions. A researcher that digs deep into companies and markets. A critic that checks every output before it goes out. A sales scout, a content engine, a website builder, a finance analyst. Ten agents, each with a clear job, each deployed dozens of times.

After 27 research missions, I discovered something uncomfortable: the full reports were gone. Every single one.

The mission briefing was still there. The three-line logbook note was still there. Date, topic, result, all neatly archived. But the actual intelligence, the detailed findings, the source tables, the competitive maps, the analysis that took 45 minutes: vanished. Deleted when the conversation ended. Overwritten when the next session started.

Like an intelligence agency that keeps the mission file and shreds the report. I had a perfectly organised archive of what my agents had done. And almost no record of what they had found.

## A logbook is not a report

I did have a form of memory built in. After every mission, each agent writes three lines to the logbook: date, what it did, what it found, which lesson.

That's good. It's far better than nothing. But it doesn't replace the full report.

A logbook note reads like this:

> Researched the corporate training market in Austria. Found 12 active providers. ARS Akademie is the dominant player. Lesson: BFI Wien blocks web access, use the OTS press releases instead.

Useful. Next time, the agent knows to use OTS. The lesson compounds.

But the full report had the 12 providers with programme structure, pricing signals and positioning. The source links and how reliable they were. The competitive analysis of who serves which segment. The note is the index card. The report is the book.

>> With the index card but not the book, you know something exists, but you can't get to it.

## Forgetting is the default

This isn't a bug. It's how these systems work. The context window closes, the session is gone. Everything you didn't explicitly save to a file goes with it.

For a chatbot, that's fine. Question in, answer out, done. For an agent that works over weeks, it's a fundamental problem. Because agents don't just answer questions. They build something meant to carry the next mission, and the one after that.

An employee who wakes up every morning with no memory of their previous work would be unemployable. They'd have to be retrained daily. They'd make the same mistakes again and again, because they have no record of having made them before. That's exactly what most AI agent setups look like. Not out of carelessness, but because memory has to be deliberately designed, and the urgency only shows up once something is lost.

For me it was 27 reports before I noticed.

## The real capital

And this is where it gets interesting for anyone using AI in a company.

The accumulated knowledge of an agent fleet IS the product. Not the code, that can be copied. Not the prompts, those can be rebuilt. The real capital is the institutional memory: the saved reports, the reviewed outputs, the lessons, the domain-specific knowledge that has grown over months of real work.

That's why "we used AI" is a weak position. "We have six months of AI-generated, human-reviewed intelligence on this topic, organised and searchable" is a strong one. The only difference is whether the reports get saved.

I track my agents like Pokémon, by the way, with levels and experience points. A researcher at level 4 has 27 missions behind it. But that number only means something if the 27 reports are actually accessible. If they're gone, the level is a fiction: it counts deployments, not skill. The number looks impressive. The capability doesn't exist.

## The fix and the lesson

The fix took ten minutes: one line in every agent's system prompt, "save the report". Technically solved.

But the lesson is bigger than a config snippet. My fleet looked functional. 384 results in 31 days, ten agents with logbooks and levels. It looked like an organised operation. And then I went looking for a report from three weeks earlier and found nothing.

That's the moment you understand the difference between an expensive chat session and a real agent system. The chat session produces outputs that live and die in the conversation. The real system accumulates: today's work makes next month's work faster, cheaper, better.

The only difference is whether the reports get saved. Don't build the forgetting kind.
