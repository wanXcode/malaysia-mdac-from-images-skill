# malaysia-mdac-from-images-skill

A public GitHub repository for the `malaysia-mdac-from-images` OpenClaw skill.

## What it does

This skill helps extract Malaysia MDAC (Malaysia Digital Arrival Card) submission fields from:
- passport photos
- flight itinerary screenshots
- user-supplied text corrections

It then outputs a clean, submission-ready checklist in the same order as the official MDAC form.

## Main use cases

- Prepare MDAC information from travel document images
- OCR passport / itinerary screenshots into structured fields
- Verify extracted values before manual submission
- Generate a copy-paste-ready MDAC checklist

## Included files

- `SKILL.md` — skill definition and workflow instructions
- `references/` — field order, normalization rules, and output examples
- `scripts/` — helper script for rendering the final checklist

## Repository

GitHub: https://github.com/wanXcode/malaysia-mdac-from-images-skill
