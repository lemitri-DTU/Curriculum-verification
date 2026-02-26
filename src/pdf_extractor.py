"""
Extract 5-digit course numbers from a PDF file.

Usage:
    python extract_courses.py <path_to_pdf>

Requirements:
    pip install pypdf
"""
import re
import sys

from pypdf import PdfReader


def extract_student_name(pdf_path: str) -> str | None:
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text = page.extract_text()
        match = re.search(r"Det bekræftes hermed, at (.+?), cpr-nr:", text)
        if match:
            return match.group(1).strip()
    return None   

def extract_course_numbers(pdf_path: str) -> list[str]:
    """
    Extract all 5-digit course numbers from a PDF file.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A deduplicated list of 5-digit course number strings.
    """
    reader = PdfReader(pdf_path)

    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""

    # Match standalone 5-digit numbers (not part of a longer number)
    matches = re.findall(r'(?<!\d)(\d{5})(?!\d)', full_text)

    # Check for duplicates and warn
    seen = set()
    duplicates = set()
    for num in matches:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    if duplicates:
        print(f"Warning: Duplicate course numbers found and removed: {sorted(duplicates)}")

    # Return unique course numbers, preserving first-occurrence order
    unique_courses = list(dict.fromkeys(matches))
    return unique_courses
