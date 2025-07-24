# MATH-008: Trigonometry
Summer 2025
### Overview
### Directory Structure
```text
math-008/
├── .venv/               # project-specific virtual environment
├── examples/            # example figures for lectures
├── exams/               # practice tests and study guides
├── figures/             # images used in notes or slides
├── lectures/            # lecture markdown / slide sources
├── src/                 # helper Python code (e.g., plotting utils)
├── transcripts/         # class session transcripts or captions
├── README.md
└── requirements.txt     # Python dependencies
```
### Lectures
- Lecture 1: The Unit Circle
- Lecture 2: Special Radian Measures
- Lecture 3: Special Locations on the Unit Circle
- Lecture 4: Values of the Unit Circle
- Lecture 5: Values of the Unit Circle (Part 2)
- Lecture 6: Trigonometric Functions 
- Lecture 7: The Graph of Sine
- Lecture 8: Graphs of Tangent and Cosine
- Lecture 9: Graphs of Cotangent and Secant
- Lecture 10: Translations
- Lecture 11: More Transformations
- Lecture 12: Intro to Inverses
- Lecture 13: Inverse Examples
- Lecture 14: Inverse Composition
- Lecture 15: Right Triangles
- Lecture 16: Law of Sines
- Lecture 17: Law of Cosines
- Lecture 18: Trig Equations
- Lecture 19: Trig Identities
- Lecture 20: More Examples for Verifying Identities
- Lecture 21: Sum and Difference Formulas
- Lecture 22: Double Angle Formulas
- Lecture 23: More on Double Angles
- Lecture 24: Half Angles
- Lecture 25: Polar Coordinates
- Lecture 26: Polar Equations
- Lecture 27: Examples of Polar Equations
- Lecture 28: Parametric Equations
- Lecture 29: Vectors
- Lecture 30: More Vectors

### Transcripts
Transcripts are generated via the Python library `yt-dlp`. This helper file is largely meant as a helper tool for codex to avoid having to pass the entirety of the json3 file into context and utilizing unnecessary tokens.

An example command used to download a transcript is shown below.
```bash
yt-dlp --skip-download --write-auto-subs --sub-langs "en" --sub-format json3 "https://www.youtube.com/watch?v=aimq-cUQu1E"
```
These transcripts (in `*.json3` format) can be converted into `*.txt` file using the `generate_transcript_txt.py` file. The newly generated text file is created in the same directory as the input json3 file. An example command is shown below
```bash
python src/generate_transcript_txt.py "transcripts/lecture-10.json3"
```