# Dump Spoofer API After

A Python script to fetch and dump session data from the [CAIDA Spoofer API](https://www.caida.org/projects/spoofer/) after a given date or session ID, optionally filtered by ASN(s). This is a port of the official Perl script to Python for easier usage and integration.

## Features
- Query the CAIDA Spoofer API for session data after a specific date or session ID
- Optionally filter results by one or more ASNs
- Handles API pagination automatically
- Outputs each session as a single JSON line (newline-delimited JSON)

## Requirements
- Python 3.6+
- [requests](https://pypi.org/project/requests/) library

Install dependencies with:
```sh
pip install requests
```

## Usage

```sh
python dump_spoofer_api_after.py --date "YYYY-MM-DD"
python dump_spoofer_api_after.py --sessionid SESSION_ID
python dump_spoofer_api_after.py --date "YYYY-MM-DD" --asn 12345 67890
```

- `--date`: Fetch sessions after this date (format: YYYY-MM-DD)
- `--sessionid`: Fetch sessions with session ID greater than this value
- `--asn`: (Optional) Filter by one or more ASNs (Autonomous System Numbers)
- 
**Note:** You must provide either `--date` or `--sessionid`, but not both.

## Example

Fetch all sessions after January 1, 2024:
```sh
python dump_spoofer_api_after.py --date "2024-01-01"
```

Fetch all sessions after session ID 12345, filtered by ASNs 1234 and 5678:
```sh
python dump_spoofer_api_after.py --sessionid 12345 --asn 1234 5678
```

## License
MIT
