# Directive: Pull GHL Contacts with Attribution

## Goal

Pull recent contacts from GoHighLevel and check for attribution data (gclid, fbclid, utm params).

## Inputs

- `location_id`: GHL Location ID (from .env)
- `api_key`: GHL API Key (from .env)
- `days_back`: Number of days to look back (default: 7)

## Tools

- `execution/ghl_pull_contacts.py`

## Outputs

- JSON file in `.tmp/contacts_{date}.json`
- Console summary showing:
  - Total contacts
  - Contacts with gclid
  - Contacts with fbclid
  - Contacts with utm_source

## Edge Cases

- API rate limiting: 100 requests/minute
- Empty response: Log and continue
- Missing attribution: Flag in summary

## Usage

```bash
python execution/ghl_pull_contacts.py --days 7
```
