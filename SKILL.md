---
name: malaysia-mdac-from-images
description: Extract Malaysia MDAC (Malaysia Digital Arrival Card) submission fields from passport photos, flight itinerary screenshots, and user-supplied text corrections, then output a clean checklist in the same order as the official MDAC registration page. Use when the user wants to prepare Malaysia entry-card / MDAC information from images, OCR travel documents, verify extracted values, or generate a submission-ready field list for manual website entry.
---

# malaysia-mdac-from-images

Produce a **submission-ready MDAC field checklist** from images and short user corrections.

## Output goal

Always output fields in this order, matching the MDAC registration flow:

### Personal Information
1. Name
2. Passport No.
3. Date of Birth
4. Nationality / Citizenship
5. Place of Birth
6. Sex
7. Date of Passport Expiry
8. Email Address
9. Confirm Email Address
10. Country / Region Code
11. Mobile No.

### Traveling Information
12. Date of Arrival
13. Date of Departure
14. Flight / Vessel / Transportation No.
15. Mode of Travel
16. Last Port of Embarkation before Malaysia
17. Accommodation of Stay
18. Address (In Malaysia)
19. State
20. Postcode
21. City

## Workflow

1. Read the images the user sends.
2. OCR the images if OCR tooling is available.
3. Extract only high-confidence values from images.
4. Ask the user only for missing or ambiguous high-risk values.
5. Prefer explicit user corrections over OCR.
6. Normalize dates into the format required by MDAC entry:
   - `DD/MM/YYYY` for direct website entry
   - optionally also show an English human-readable version when useful
7. Normalize country/region values to the wording likely used in official dropdowns:
   - `CHN / CHINA`
   - `THA / THAILAND`
   - `AIR`
   - `HOTEL / MOTEL / REST HOUSE`
   - `WP KUALA LUMPUR`
8. Output a compact checklist the user can directly copy into the website.

## Extraction rules

- If OCR and user text conflict, trust the user text.
- Do not invent passport number digits.
- Do not guess the flight number unless the user confirms it.
- If only hotel name is available, mark address-related fields as needing confirmation unless the user explicitly authorizes you to look them up.
- If the official website flow is known, keep output order identical to the site.

## Expected final format

Use this exact structure unless the user asks for another format:

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

## When values are uncertain

If some fields are uncertain, split them into:
- `Confirmed`
- `Need confirmation`

But keep the same MDAC order.

## Bundled resources

- Read `references/mdac-field-order.md` for the canonical field order and normalization rules.
- Read `references/example-output.md` when you need to mirror the final output shape exactly.
- Read `references/usage-example.md` for the shortest user-trigger and final checklist example.
- Use `scripts/render_mdac_checklist.py` to render structured JSON into the final MDAC checklist text.

## Packaging standard

Before considering the skill complete:
1. Keep the output strictly aligned to MDAC website field order.
2. Make user corrections override OCR ambiguities.
3. Verify the bundled renderer script produces the same structure as the example output.
4. Package the skill with the packaging script and fix validation issues if any.
