# Curriculum Verification Tool

A tool to verify whether a student's course list satisfies the graduation requirements for an MSc specialization in the Sustainable Energy Systems MSc program at DTU, based on the year they started their studies.

Two implementations are provided: a **Python script** for local use and a **standalone HTML app** that runs entirely in the browser — no installation required.

---

## How It Works

The tool checks whether a student's list of completed courses satisfies the curriculum requirements for their chosen specialization. Since curricula can change from year to year, the tool checks the curriculum for every academic year from the student's start year to the current year. The tool then:

- **Reports success** if the student satisfies the requirements for *at least one* academic year, and identifies the earliest year for which requirements are fully met.
- **Reports failure** if the student does not satisfy the requirements for *any* academic year, and generates a detailed breakdown for each year showing which requirements are missing.

---

## Supported Specializations

| Specialization | Available curriculum years |
|---|---|
| General | 2023, 2024, 2025 |
| Digital Energy Systems | 2025 |
| Energy Systems Analysis | 2023, 2025 |
| Energy Efficient Building Systems | 2025 |

**Data for other years is missing**

---

## Requirements

| | Python | HTML |
|---|---|---|
| Runtime | Python 3.10+ | Any modern browser |
| Dependencies | `pypdf` | PDF.js via CDN |
| PDF extraction | ✓ | ✓ |
| Student name detection | ✓ (DTU transcript format) | ✓ (DTU transcript format) |
| Output formats | `.txt`, `.html` | Interactive (in-browser) |
| Works offline | ✓ | ✓ (after first load) |

---

## Repository Structure

```
curriculum verification/
│
├── _main.py                         # Entry point: define student study plan and run verification
│
├── src/                             # Source codes for python version
│   ├── curriculum_test.py           # Core verification logic
│   ├── pdf_extractor.py             # Extracts 5-digit course numbers from a PDF study plan
│   ├── write_solutions.py           # Outputs results as .txt or .html files
│   │
│   └── input/                       # Curriculum data
│       ├── curriculum_specializations.py  # Maps specialization names to their yearly curricula
│       ├── curriculum_groups_2023.py      # Course group definitions for academic year 2023/2024
│       ├── curriculum_groups_2024.py      # Course group definitions for academic year 2024/2025
│       └── curriculum_groups_2025.py      # Course group definitions for academic year 2025/2026
│
├── output/                          # Generated result files are saved here automatically
│
└── curriculum_verification.html        # Standalone browser-based tool (no install)
```
---

## How to Run it

### HTML Implementation 

**No installation. No Python. Works offline after the first load.**

1. Open `curriculum_verification.html` in any modern browser.
2. Upload the student's study plan PDF — course numbers are extracted automatically.
3. Select the specialization, enter the start year, and optionally add any course numbers not included in the PDF.
4. Click **Run Verification** to see the results.

Results are displayed directly in the page, with color-coded tables for each requirement group. Use the **Print / Save as PDF** button to downoad the results.

> **Note:** The tool uses [PDF.js](https://mozilla.github.io/pdf.js/) loaded from a CDN, so an internet connection is required on the first load. Everything else runs locally in the browser.

----

### Python Implementation

#### 1. Install dependencies

```bash
pip install pypdf
```

### 2. Define the student's study plan in `_main.py`

```python
study_plan = {
    'course_list': extract_course_numbers('path/to/study_plan.pdf') + ['42500'],  # optionally add courses manually
    'specialization': 'Energy Systems Analysis',
    'start year': 2023
}
```

- **`course_list`**: a list of 5-digit course codes (strings). These can be extracted automatically from a PDF using `extract_course_numbers()`, or defined manually as a Python list.
- **`specialization`**: one of the supported specialization names listed above.
- **`start year`**: the year the student started their MSc (e.g. `2023` corresponds to the 2023/2024 academic year).

#### 3. Run the script from the root folder

```bash
python _main.py
```

Make sure to run the script from `curriculum verification/` (the root folder), not from inside `src/`, so that Python resolves imports correctly.

#### 4. Check the output

Results are saved automatically in the `output/` folder. If a file with the same name already exists (e.g. from a previous run), a versioned filename is created automatically: `filename_(1).txt`, `filename_(2).txt`, etc.

Output files are named according to the following pattern:
```
requirements_{specialization}_{year}_(satisfied).txt
requirements_{specialization}_{year}_(NOT satisfied).txt
```
---

## Output Format

In both implementations, each output file contains one table per requirement group. For example:

```
Requirements verification for Energy Systems Analysis in 2023/2024

All requirements satisfied

* = course taken by student

Core competence mandatory courses (2023):
The student must take at least 15 ECTS from this list:
Course(s)                       ECTS
----------------------------------
* 46205                            5
* 46740                            5
* 46770                            5
----------------------------------
Requirements satisfied (15 ECTS earned)
```

Courses marked with `*` are present in the student's course list. Each table ends with a summary line indicating whether the requirement is satisfied and how many ECTS were earned.

Two output formats are available in `src/write_solutions.py`:
- **`.txt`** (default): plain text with `*` markers for taken courses.
- **`.html`**: color-coded version (taken courses in green, unsatisfied requirements in red) that can be opened in any web browser.

To switch to HTML output, comment out the `write_requirements_to_text(...)` line and uncomment the `write_requirements_to_html(...)` line in `src/curriculum_test.py`.

---

## Adding a New Academic Year

### In the HTML Implementation 

Add the new group objects to the C constant in the <script> block, following the same structure as existing entries (each entry has name, courses as an array of {codes, ects} objects, and requirement). Then register them in the CURRICULUMS mapping.

All curriculum data lives inside the `<script>` block of `html/curriculum_verification.html`. There are two places to edit: the **`C` constant** (where individual requirement groups are defined) and the **`CURRICULUMS` mapping** (where groups are assembled into a full curriculum per specialization and year).

#### Step 1 — Define the new requirement groups in `C`

Locate the `const C = { ... }` block. Each key is a group name and its value is an object with three fields:

```js
group_name_2026: {
  name: 'Human-readable group label (2026)',
  courses: [
    { codes: ['XXXXX'], ects: 5 },           // single course
    { codes: ['XXXXX', 'YYYYY'], ects: 5 },  // interchangeable alternatives (student needs one)
  ],
  requirement: 10   // minimum ECTS the student must earn from this group
},
```

- `name` — the label shown in the results table. Include the year in parentheses for clarity, e.g. `'Core competence mandatory courses (2026)'`.
- `courses` — an array of course entries. Each entry has a `codes` array (list of interchangeable course numbers) and an `ects` value. If two course numbers are interchangeable, put both in the same `codes` array; the student only needs to have taken one of them to earn those ECTS.
- `requirement` — the minimum total ECTS the student must accumulate from this group to satisfy it.

For example, adding a mandatory group and an elective group for 2026:

```js
// ── 2026 ─────────────────────────────────────────────────────────────────────
core_competence_mandatory_2026: {
  name: 'Core competence mandatory courses (2026)',
  courses: [
    { codes: ['46205'], ects: 5 },
    { codes: ['46740'], ects: 5 },
    { codes: ['46770'], ects: 5 },
  ],
  requirement: 15
},

ESA_core_competence_technology_2026: {
  name: 'Core competence technology courses for Energy Systems Analysis specialization (2026)',
  courses: [
    { codes: ['34552'], ects: 5 },
    { codes: ['41418'], ects: 5 },
    { codes: ['47301'], ects: 5 },
    { codes: ['47330', '47334'], ects: 5 },  // student may take either
  ],
  requirement: 10
},
```

Add as many groups as the new curriculum requires. Groups shared across specializations (such as polytechnic foundation or innovation courses) only need to be defined once and can be referenced multiple times in Step 2.

#### Step 2 — Register the groups in `CURRICULUMS`

Locate the `const CURRICULUMS = { ... }` object. Each key is a specialization name, and each value is an object whose keys are start years and whose values are arrays of groups (in the order they should appear in the results).

Add a `2026` entry under each relevant specialization:

```js
const CURRICULUMS = {

  'General': {
    2023: [ ... ],  // existing — do not change
    2024: [ ... ],  // existing — do not change
    2025: [ ... ],  // existing — do not change
    2026: [
      C.polytechnic_foundation_2026,
      C.innovation_II_2026,
      C.core_competence_mandatory_2026,
      C.core_competence_digital_2026,
      C.core_competence_technology_2026,
      C.core_competence_general_2026,
      C.core_competence_combined_2026
    ]
  },

  'Energy Systems Analysis': {
    2023: [ ... ],  // existing — do not change
    2025: [ ... ],  // existing — do not change
    2026: [
      C.polytechnic_foundation_2026,
      C.innovation_II_2026,
      C.core_competence_mandatory_2026,
      C.ESA_core_competence_digital_2026,
      C.ESA_core_competence_technology_2026,
      C.ESA_core_competence_general_1_2026,
      C.ESA_core_competence_general_2_2026,
      C.ESA_core_competence_combined_2026
    ]
  },

  // add 2026 to other specializations as needed
};
```

Only add a `2026` entry to specializations for which a 2026/2027 curriculum actually exists.

#### Step 3 — Update the Supported Specializations table

Update the table at the top of this README to include the new year next to the relevant specializations.

---

### In the ython Implementation 

To add curriculum data for a new year (e.g. 2026):

1. Create `src/input/curriculum_groups_2026.py` following the structure of existing files. Each requirement group is a dictionary with the following keys:
   - `'name'`: a descriptive name for the requirement group.
   - `'courses'`: a dictionary mapping tuples of course codes to their ECTS value. Courses grouped in the same tuple are interchangeable (i.e. the student can take any one of them to earn those ECTS).
   - `'requirement'`: the minimum number of ECTS the student must earn from this group.

2. Add the new year's curriculum lists to the relevant specialization dictionaries in `src/input/curriculum_specializations.py`.

