# MDAC Field Order Reference

Canonical order aligned to the Malaysia Digital Arrival Card website registration page.

## Personal Information
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

## Traveling Information
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

## Normalization guide

- Date input on website: `DD/MM/YYYY`
- China nationality dropdown value is typically represented as `CHN / CHINA`
- Thailand embarkation is typically represented as `THA / THAILAND`
- Mode of travel for flights: `AIR`
- Hotel stay type: `HOTEL / MOTEL / REST HOUSE`
- Kuala Lumpur federal territory state: `WP KUALA LUMPUR`

## User correction precedence

If OCR output conflicts with user-provided corrections, prefer user-provided corrections for:
- passport number
- full name
- flight number
- email
- phone
- departure date
- hotel name/address
