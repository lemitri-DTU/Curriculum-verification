import os
import webbrowser

def get_unique_filename(filepath):
    """If file already exists, append (1), (2), etc. until a unique name is found."""
    if not os.path.exists(filepath):
        return filepath
    
    base, ext = os.path.splitext(filepath)
    counter = 1
    while os.path.exists(f"{base}_({counter}){ext}"):
        counter += 1
    return f"{base}_({counter}){ext}"

GREEN = "\033[92m"
RESET = "\033[0m"

def print_requirement_table(req, taken_courses):
    taken_set = set(taken_courses)

    col1_w, col2_w = 25, 10
    header = f"{'Course(s)':<{col1_w}} {'ECTS':>{col2_w}}"
    separator = "-" * (col1_w + col2_w + 1)

    print(header)
    print(separator)

    for course_group, ects in req['courses'].items():
        if len(course_group) > 1:
            # Highlight each course individually if it matches
            parts = []
            for course in course_group:
                if course in taken_set:
                    parts.append(f"{GREEN}{course}{RESET}")
                else:
                    parts.append(course)
            course_str = " or ".join(parts)
        else:
            course = course_group[0]
            course_str = f"{GREEN}{course}{RESET}" if course in taken_set else course

        # ANSI codes add invisible characters, so we pad manually
        visible_len = sum(len(c) for c in course_group) + (len(course_group) - 1) * 4  # 4 for " or "
        padding = col1_w - visible_len
        print(f"{course_str}{' ' * padding} {ects:>{col2_w}}")

    print(separator)

def write_requirements_to_text(student_name, requirements, taken_courses, ECT_earned, specialization, year):
    taken_set = set(taken_courses)
    
    if all(ECT_earned[req['name']]>=req['requirement'] for req in requirements):
        filename=f"{student_name}_requirements_{specialization}_{year}_(satisfied).txt"
    else:
        filename=f"{student_name}_requirements_{specialization}_{year}_(NOT satisfied).txt"   
    
    # Create output folder (if it does not exist) and build full path
    output_folder = os.path.join(os.path.dirname(__file__), '..', "output")
    filename = os.path.join(output_folder, filename)
    os.makedirs(output_folder, exist_ok=True)
    
    # Get unique filename to avoid overwriting
    filename = get_unique_filename(filename)

    col1_w, col2_w = 25, 10
    separator = "-" * (col1_w + col2_w + 1)

    all_lines = []
 
    all_lines.append(f"Requirements verification for {specialization} in {year}/{year+1}\n")  
    all_lines.append(f"{student_name}")
    all_lines.append("") # blank line 
    if all(ECT_earned[req['name']]>=req['requirement'] for req in requirements):
        all_lines.append("All requirement satisfied")
    else:
        all_lines.append("Requirement not satisfied (see details below)")
    all_lines.append("") # blank line 
    all_lines.append("* = course taken by student")
    all_lines.append("") # blank line 
    for req in requirements:
        all_lines.append(f"{req['name']}:\n")
        all_lines.append(f"The student must take at least {req['requirement']} ECTS from this list:")
        all_lines.append(f"{'Course(s)':<{col1_w}} {'ECTS':>{col2_w}}")
        all_lines.append(separator)

        for course_group, ects in req['courses'].items():
            if len(course_group) > 1:
                course_str = " or ".join(course_group)
            else:
                course_str = course_group[0]

            if any(course in taken_set for course in course_group):
                course_str = f"* {course_str}"
            else:
                course_str = f"  {course_str}"

            all_lines.append(f"{course_str:<{col1_w}} {ects:>{col2_w}}")

        all_lines.append(separator)
        if ECT_earned[req['name']]<req['requirement']:
            all_lines.append(f"Requirements not satisfied ({ECT_earned[req['name']]} ECTS earned; {req['requirement']-ECT_earned[req['name']]} ECTS missing)")
        else:
            all_lines.append(f"Requirements satisfied ({ECT_earned[req['name']]} ECTS earned)")
        all_lines.append("")  # blank line between tables

    with open(filename, "w") as f:
        f.write("\n".join(all_lines))

    if all(ECT_earned[req['name']]>=req['requirement'] for req in requirements):
        print(f"Full {year}/{year+1} curriculum and courses taken: Table written to '{filename}'")
    else:
        print(f"Missing courses for {year}/{year+1} curriculum: Table written to '{filename}'")


def write_requirements_to_html(student_name, requirements, taken_courses, ECT_earned, specialization, year, open_option=False):
    taken_set = set(taken_courses)
    
    if all(ECT_earned[req['name']]>=req['requirement'] for req in requirements):
        filename=f"{student_name}_requirements_{specialization}_{year}_(satisfied).html"
    else:
        filename=f"{student_name}_requirements_{specialization}_{year}_(NOT satisfied).html"
    
    # Create output (if it does not exist) folder and build full path
    output_folder = os.path.join(os.path.dirname(__file__), '..', "output")
    filename = os.path.join(output_folder, filename)
    os.makedirs(output_folder, exist_ok=True)
    
    # Get unique filename to avoid overwriting
    filename = get_unique_filename(filename)

    col1_w, col2_w = 25, 10
    separator = "-" * (col1_w + col2_w + 1)
    
    html_lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head><style>",
        "  body { font-family: monospace; white-space: pre; }",
        "  .title { font-size: 24px; font-weight: bold; margin-bottom: 20px; }",
        "  .taken { color: green; font-weight: bold; }",
        "  .not-taken { color: black; }",
        "  .legend { color: green; font-weight: bold; }",
        "  .satisfied { color: green; font-weight: bold; }",
        "  .not-satisfied { color: red; font-weight: bold; }",
        "</style></head>",
        "<body>",
        f'<div class="title">Requirements verification for {specialization} in {year}/{year+1}</div>',  # Title at the top
        f'<div class="subtitle">{student_name}</div>',
        ""  # blank line after title
    ]
    if all(ECT_earned[req['name']]>=req['requirement'] for req in requirements):
        html_lines.append(f'<span class="satisfied">All requirement satisfied</span>')
    else:
        html_lines.append(f'<span class="not-satisfied">Requirement not satisfied (see details below)</span>')
    html_lines.append("") # blank line    
    html_lines.append('<span class="legend">* = course taken by student</span>')
    html_lines.append("") # blank line

    for req in requirements:
        html_lines.append(f"{req['name']}:\n")
        html_lines.append(f"The student must take at least {req['requirement']} ECTS from this list:\n")
        html_lines.append(f"{'Course(s)':<{col1_w}} {'ECTS':>{col2_w}}")
        html_lines.append(separator)

        for course_group, ects in req['courses'].items():
            is_taken = any(course in taken_set for course in course_group)

            if len(course_group) > 1:
                # Highlight each course individually
                parts = []
                for course in course_group:
                    if course in taken_set:
                        parts.append(f'<span class="taken">{course}</span>')
                    else:
                        parts.append(f'<span class="not-taken">{course}</span>')
                course_str = " or ".join(parts)
                visible_len = sum(len(c) for c in course_group) + (len(course_group) - 1) * 4
            else:
                course = course_group[0]
                css_class = "taken" if is_taken else "not-taken"
                course_str = f'<span class="{css_class}">{course}</span>'
                visible_len = len(course)

            # Add marker and manual padding to account for HTML tags
            marker = "* " if is_taken else "  "
            visible_len += 2  # for marker
            padding = " " * (col1_w - visible_len)
            html_lines.append(f"{marker}{course_str}{padding} {ects:>{col2_w}}")

        html_lines.append(separator)
        if ECT_earned[req['name']]<req['requirement']:
            html_lines.append(f'<span class="not-satisfied">Requirement not satisfied ({ECT_earned[req['name']]} ECTS earned; {req['requirement']-ECT_earned[req['name']]} ECTS missing)</span>')
        else:
            html_lines.append(f'<span class="satisfied">Requirement satisfied ({ECT_earned[req['name']]} ECTS earned)</span>')
        html_lines.append("")  # blank line between tables

    html_lines.append("</body></html>")

    with open(filename, "w") as f:
        f.write("\n".join(html_lines))

    if all(ECT_earned[req['name']]>=req['requirement'] for req in requirements):
        print(f"Matched courses for {year}/{year+1} curriculum: Table written to '{filename}'")
    else:
        print(f"Missing courses for {year}/{year+1} curriculum: Table written to '{filename}'")
    
    if open_option:
        webbrowser.open(f"file://{filename}")
