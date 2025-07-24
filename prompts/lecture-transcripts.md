---
name: lecture-transcripts
description: Identifies missing lecture notes
author: Tim Sanders
created: 2025-07-20
version: v1.0.0
notes: |
  This prompt is designed to be used with Codex to analyze specific lecture notes and the generated transcript from a YouTube video.
  The output will be added to the specified lecture notes under a `Codex notes` section
---

Given the transcript subtitle file that is in lectures/lecture-N.json3 and the notes that are in lecture-N.md, please identify any missing items that I did not include in my notes that should be added.

These items should be added in a new section at the bottom of the lecture-N.md file under a new header #### Codex notes.

You can use the src/generate_transcripts_txt.py file to extract a text version of the transcript.
