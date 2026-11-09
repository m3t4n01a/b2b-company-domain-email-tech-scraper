# Official Python Wrapper for Company Domain to B2B Email & Tech Stack Enricher (DNS + Web OSINT) (willowy_catamaran_fco/b2b-domain-email-tech-scraper)
import os
import json
import urllib.request

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/willowy_catamaran_fco~b2b-domain-email-tech-scraper/run-sync-get-dataset-items?token=" + APIFY_TOKEN

def run_extraction(payload: dict) -> list[dict]:
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))

if __name__ == "__main__":
    sample_payload = {
    "companiesOrDomains": [
        "Stripe",
        "Linear",
        "Vercel",
        "Supabase"
    ]
}
    print("Triggering willowy_catamaran_fco/b2b-domain-email-tech-scraper...")
    print(json.dumps(run_extraction(sample_payload), indent=2))
