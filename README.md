# Curriculum Verification Tool

This tool verifies whether a student's course list satisfies the requirements for a given MSc specialization at DTU, based on the year they started their studies.

---

## Repository Structure

```
curriculum verification/
│
├── _main.py                         # Entry point: define student study plan and run verification
│
├── src/                             # Source code
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
└── output/                          # Generated result files are saved here automatically
```

---

## How It Works

The tool checks whether a student's list of completed courses satisfies the curriculum requirements for their chosen specialization. Since curricula can change from year to year, the tool checks the curriculum for every academic year from the student's start year to the current year. The tool then:

- **Reports success** if the student satisfies the requirements for *at least one* academic year, and identifies the earliest year for which requirements are fully met.
- **Reports failure** if the student does not satisfy the requirements for *any* academic year, and generates a detailed breakdown for each year showing which requirements are missing.

In both cases, a result file is written to the `output/` folder.

---

## Supported Specializations

- `General`
- `Digital Energy Systems`
- `Energy Systems Analysis`
- `Energy Efficient Building Systems`

---

## Usage

### 1. Install dependencies

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

### 3. Run the script from the root folder

```bash
python _main.py
```

Make sure to run the script from `curriculum verification/` (the root folder), not from inside `src/`, so that Python resolves imports correctly.

### 4. Check the output

Results are saved automatically in the `output/` folder. If a file with the same name already exists (e.g. from a previous run), a versioned filename is created automatically: `filename_(1).txt`, `filename_(2).txt`, etc.

Output files are named according to the following pattern:
```
requirements_{specialization}_{year}_(satisfied).txt
requirements_{specialization}_{year}_(NOT satisfied).txt
```

---

## Output Format

Each output file contains one table per requirement group. For example:

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

To add curriculum data for a new year (e.g. 2026):

1. Create `src/input/curriculum_groups_2026.py` following the structure of existing files. Each requirement group is a dictionary with the following keys:
   - `'name'`: a descriptive name for the requirement group.
   - `'courses'`: a dictionary mapping tuples of course codes to their ECTS value. Courses grouped in the same tuple are interchangeable (i.e. the student can take any one of them to earn those ECTS).
   - `'requirement'`: the minimum number of ECTS the student must earn from this group.

2. Add the import in `src/input/__init__.py`:
   ```python
   from .curriculum_groups_2026 import *
   ```

3. Add the new year's curriculum lists to the relevant specialization dictionaries in `src/input/curriculum_specializations.py`.
