import argparse
import requests
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="Dump Spoofer API after a given date or sessionid")
    parser.add_argument('--asn', nargs='*', type=int, help='List of ASNs')
    parser.add_argument('--date', type=str, help='Date string (required if sessionid is not set)')
    parser.add_argument('--sessionid', type=int, help='Session ID (required if date is not set)')
    args = parser.parse_args()

    if (args.date is None and args.sessionid is None) or (args.date and args.sessionid):
        print("usage: dump-spoofer-api-after.py\n"
              "  [--asn @ases]\n"
              "  [--date $date]\n"
              "  [--sessionid $id]", file=sys.stderr)
        sys.exit(-1)

    api = "https://api.spoofer.caida.org"
    headers = {"accept": "application/ld+json"}

    # Build initial URL
    if args.date:
        url = f"{api}/sessions?timestamp%5Bafter%5D={args.date.replace(' ', '%20')}"
    else:
        url = f"{api}/sessions?session%5Bgt%5D={args.sessionid}"

    if args.asn:
        for asn in args.asn:
            url += f"&asn%5B%5D={asn}"

    page = 1
    while True:
        print(f"page {page}", file=sys.stderr)
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: {response.status_code}", file=sys.stderr)
            break
        obj = response.json()
        if not obj:
            break
        for member in obj.get("hydra:member", []):
            print(json.dumps(member))
        next_url = obj.get("hydra:view", {}).get("hydra:next")
        if next_url:
            url = api + next_url
            page += 1
        else:
            break

if __name__ == "__main__":
    main()
