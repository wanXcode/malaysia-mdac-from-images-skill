# malaysia-mdac-from-images-skill

Extract Malaysia MDAC (Malaysia Digital Arrival Card) submission fields from passport photos, itinerary screenshots, and user corrections, then output a clean checklist in the same order as the official MDAC registration page.

## What this repository contains

This repository publishes the `malaysia-mdac-from-images` OpenClaw skill.

It is designed for workflows where a user wants to:
- prepare Malaysia MDAC information from images
- OCR passport and flight itinerary screenshots
- verify extracted values before submission
- generate a copy-paste-ready checklist for manual website entry

## Skill capabilities

The skill is optimized to:
- read passport photos and itinerary screenshots
- extract high-confidence MDAC fields
- prefer explicit user corrections over OCR output
- avoid guessing risky fields such as passport number digits or flight number
- ask only for missing or ambiguous high-risk values
- normalize output into MDAC website field order

## Output format

The final output follows this structure:

```text
Malaysia MDAC checklist

Personal Information
- Name:
- Passport No.:
- Date of Birth:
- Nationality / Citizenship:
- Place of Birth:
- Sex:
- Date of Passport Expiry:
- Email Address:
- Confirm Email Address:
- Country / Region Code:
- Mobile No.:

Traveling Information
- Date of Arrival:
- Date of Departure:
- Flight / Vessel / Transportation No.:
- Mode of Travel:
- Last Port of Embarkation before Malaysia:
- Accommodation of Stay:
- Address (In Malaysia):
- State:
- Postcode:
- City:
```

## Repository structure

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── references/
│   ├── mdac-field-order.md
│   ├── example-output.md
│   └── usage-example.md
└── scripts/
    └── render_mdac_checklist.py
```

## Included files

- `SKILL.md` — skill definition and workflow instructions
- `references/mdac-field-order.md` — canonical field order and normalization guidance
- `references/example-output.md` — expected output example
- `references/usage-example.md` — shortest trigger and response example
- `scripts/render_mdac_checklist.py` — helper script that renders structured JSON into the final checklist text

## Example use case

User says:

```text
帮我根据这几张护照和机票图片，整理成马来西亚 MDAC 官网填写顺序的清单。
```

Expected behavior:
- extract only reliable values from the images
- ask for missing or ambiguous important fields
- return a final checklist in official MDAC field order

## Development notes

This repository is intended to be simple and portable.

Recommended local checks:

```bash
python3 scripts/render_mdac_checklist.py < sample.json
```

Where `sample.json` is a JSON object keyed by MDAC field names.

## Publishing

Initial public repository:
- https://github.com/wanXcode/malaysia-mdac-from-images-skill

## License

MIT
