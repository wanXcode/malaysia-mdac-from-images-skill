#!/usr/bin/env python3
import json
import sys

FIELD_ORDER = [
    ("Personal Information", [
        "Name",
        "Passport No.",
        "Date of Birth",
        "Nationality / Citizenship",
        "Place of Birth",
        "Sex",
        "Date of Passport Expiry",
        "Email Address",
        "Confirm Email Address",
        "Country / Region Code",
        "Mobile No.",
    ]),
    ("Traveling Information", [
        "Date of Arrival",
        "Date of Departure",
        "Flight / Vessel / Transportation No.",
        "Mode of Travel",
        "Last Port of Embarkation before Malaysia",
        "Accommodation of Stay",
        "Address (In Malaysia)",
        "State",
        "Postcode",
        "City",
    ]),
]


def render(data: dict) -> str:
    lines = ["Malaysia MDAC checklist", ""]
    for section, fields in FIELD_ORDER:
        lines.append(section)
        for f in fields:
            lines.append(f"- {f}: {data.get(f, '')}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
    sys.stdout.write(render(data))


if __name__ == '__main__':
    main()
