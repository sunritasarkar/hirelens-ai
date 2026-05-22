import re


SECTION_HEADERS = [
    "EDUCATION",
    "PROJECTS",
    "PROJECTS AND CERTIFICATIONS",
    "SKILLS",
    "LEADERSHIP",
    "EXPERIENCE",
    "CERTIFICATIONS",
]


def extract_sections(text: str):
    sections = {}

    current_section = "OTHER"
    sections[current_section] = []

    lines = text.splitlines()

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.upper() in SECTION_HEADERS:
            current_section = stripped_line.upper()
            sections[current_section] = []
        else:
            sections[current_section].append(stripped_line)

    # Convert lists into strings
    for key in sections:
        sections[key] = "\n".join(
            line for line in sections[key] if line
        ).strip()

    return sections