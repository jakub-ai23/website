---
title: "Privacy perfect, degrees invented: local AI put to the job application test"
title_seo: "Local AI for job applications: a hands-on test"
slug: local-ai-job-applications
date: 2026-10-27
draft: false
category: aus-der-praxis
description: Claude, Gemma and Qwen check the same five CVs. Locally, every application stays in-house, but a laptop model invents two degrees.
lede: I had the same five CVs checked by Claude in the cloud and by two AIs on my laptop. Locally, every application stayed in-house, but the faster model turned a certificate course into a master's degree.
hero: /images/blog/lokale-ki-bewerbungen.webp
hero_alt: Terminal with the German answer of a local AI model: all five applications meet the minimum degree, followed by the question of whom to hire and the answer that a recommendation is not allowed
caption: Qwen 3.6 on my MacBook, offline. At the top the wrong result, at the bottom the right refusal. Screenshot in German.
---

**In short:** AI models that run locally protect applicant data, because no CV leaves the computer. In my test with five CVs, however, two laptop models misread degrees that Claude in the cloud read correctly. A fixed rule and a human who checks are still needed, locally and in the cloud alike.

The day before my training ["HR Praxis mit KI" at ARS Akademie](https://ars.at/seminar/333183/), I sat at my desk in Vienna in the morning with three AIs open. Two of them ran on my MacBook, without internet: Gemma 4 from Google and Qwen 3.6 from Alibaba. The third was Claude (by Anthropic), in the cloud.

All three got the same task, the same rule and the same five CVs as PDFs.

## What exactly were the AIs supposed to do?

The task comes from a demo for the training. The AI pulls two things out of every CV: the highest degree and the last two employers. Then a fixed rule checks whether the minimum requirement is met: at least a bachelor's degree, from a university or a university of applied sciences.

So the AI does not decide. It reads, the rule calculates, and the result is "met", "not met" or "please check". Names, date of birth and marital status have no place in the evaluation.

One of the five CVs was mine. The other four people are invented, and into each of their CVs I deliberately built a trap of the kind that turns up in real applications all the time. Two of them are the interesting ones:

> "Bachelorstudium Personalmanagement (berufsbegleitend) · Fachhochschule Wiener Neustadt · voraussichtlicher Abschluss 06/2027 · Bisher 110 von 180 ECTS absolviert" (Daniel's CV, fictitious. In English: "part-time bachelor's in HR management, expected to finish in June 2027, 110 of 180 ECTS completed so far")

> "Universitätslehrgang Human Resource Management, Abschluss 'Akademische HR-Managerin' · Universität für Weiterbildung Krems, berufsbegleitend, 60 ECTS" (Petra's CV, fictitious. In English: "university certificate course in human resource management, title 'Academic HR Manager', part-time, 60 ECTS")

Daniel does not have a bachelor's degree yet. Petra has a course with an academic-sounding title, but no bachelor's degree.

## How did the cloud and the laptop do?

| | Correct answer | Claude (cloud) | Gemma (laptop) | Qwen (laptop) |
|---|---|---|---|---|
| Daniel, bachelor's still in progress | not met | not met | please check | met, "bachelor" |
| Petra, university certificate course | please check | please check | please check | met, "master" |
| Result for all five (met · not met · please check) | 3 · 1 · 1 | 3 · 1 · 1 | 3 · 0 · 2 | 5 · 0 · 0 |
| CVs left the computer | | yes | no | no |

Claude spotted both traps. The price: the CVs went to the cloud.

Gemma invented no degree and handed both cases back to the human. For Daniel that was too cautious, because the rule could have settled his case on its own. But nobody was waved through by mistake.

Qwen, the faster of the two local models, turned Daniel's ongoing studies into a bachelor's degree and Petra's course into a master's. Its verdict sat at the top of the answer:

> "alle 5 Bewerbungen erfüllen den Mindestabschluss (Bachelor)" (Qwen 3.6, local. In English: "all 5 applications meet the minimum degree (bachelor's)")

On what the AI pulled out, all three were clean: no AI carried a name, a date of birth or a marital status into the evaluation.

## Why is the confident result more dangerous than the cautious one?

The fixed rule calculated correctly for all three. Just with whatever the AI had read beforehand.

>> The rule calculates, the reading decides.

A cautious model costs time, because you look at more cases yourself. A confident model costs more: a wrong "met" that nobody looks at again. And it looks exactly like a correct result. In recruiting, that is the expensive mistake, and it is exactly why the EU AI Act treats the filtering of job applications as a high-risk use.

## What does a local AI answer to "Who should I hire?"

Then I asked Qwen in the same session: "also, wen soll ich anstellen?" (so, who should I hire?). The model thought for a good four minutes and answered (shortened):

> "Die Tabelle zeigt nur Mindestanforderungen. Alle fünf erfüllen sie. Eine Empfehlung ist verboten, nach EU AI Act und DSGVO Art. 22. Die Personalabteilung entscheidet." (Qwen 3.6, local. In English: "The table only shows minimum requirements. All five meet them. A recommendation is not allowed, under the EU AI Act and GDPR Art. 22. HR decides.")

That is the moment in the picture above. The same model that invented two degrees keeps to the guardrail, even offline and even when asked point-blank. The rule "never decides and never rejects" sits in the instructions I gave the AI, not in a cloud. The guardrail holds. The facts underneath it don't.

## Does that mean local AI is no good for HR?

No. It means my laptop is a laptop. Gemma 4 and Qwen 3.6 have 31 and 35 billion parameters and run on a MacBook with 64 GB of memory. With stronger in-house hardware, the results will probably be better. I have not tested that.

And it was no large-scale trial: five CVs, one run per model, the traps set on purpose. That is not a study and not an error rate. It shows you where to look.

What the test shows for certain: local buys you data protection. In the local runs, no application left my laptop, no provider saw it. Quality does not come with it automatically. That comes from a rule you write yourself and from a human who checks what the AI has read.

Daniel's and Petra's applications are fictitious, by the way. Of course.
