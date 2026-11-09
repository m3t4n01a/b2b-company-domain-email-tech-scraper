# Company Domain to B2B Email & Tech Stack Enricher (DNS + Web OSINT)

[![Run on Apify Store](https://img.shields.io/badge/Apify_Store-Run_Actor-00C853?style=for-the-badge&logo=apify)](https://apify.com/willowy_catamaran_fco/b2b-domain-email-tech-scraper)
[![MCP Compatible](https://img.shields.io/badge/MCP-AI_Agent_Ready-7C3AED?style=for-the-badge)](https://apify.com/willowy_catamaran_fco/b2b-domain-email-tech-scraper/api)
[![n8n & Clay Ready](https://img.shields.io/badge/Integrations-n8n_%7C_Clay_%7C_Make-FF6D5A?style=for-the-badge)](https://apify.com/willowy_catamaran_fco/b2b-domain-email-tech-scraper)

Convert company names or domains into verified B2B emails, DNS MX/SPF/DMARC intelligence, and 35+ technology stack signals. Built for Clay, n8n, Make.com, and AI Agents.

---

## Why Growth Teams & AI Agents Use This Actor
- **Flat, Pre-Validated JSON Output:** Zero nested arrays - maps directly into **Clay.com columns**, **n8n HTTP Request nodes**, **Make.com**, **HubSpot**, and **Airtable**.
- **High-Concurrency Async Engine:** Powered by concurrent worker pools and TLS browser impersonation (`curl_cffi`) with low 256MB-512MB RAM footprint.
- **MCP & Autonomous Agent Ready:** Runs under `LIMITED_PERMISSIONS` with predictable Pay-Per-Event pricing so Claude, Cursor, LangChain, and CrewAI agents can call it autonomously.

---

## Quick Start: 1-Click API Call (n8n / Clay / cURL)

Use the synchronous endpoint below in **Clay (HTTP API enrichment)** or **n8n (HTTP Request node)** to run the extraction and receive the JSON array in a single request:

```bash
curl -X POST "https://api.apify.com/v2/acts/willowy_catamaran_fco~b2b-domain-email-tech-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "companiesOrDomains": [
    "Stripe",
    "Linear",
    "Vercel",
    "Supabase"
  ]
}'
```

---

## Sample Input
```json
{
  "companiesOrDomains": [
    "Stripe",
    "Linear",
    "Vercel",
    "Supabase"
  ]
}
```

## Real Output Sample
```json
{
  "companyName": "Stripe",
  "companyDomain": "stripe.com",
  "primaryEmail": "privacy@stripe.com",
  "allEmailsCsv": "privacy@stripe.com, sales@stripe.com, complaints-in@stripe.com",
  "techStackCsv": "Google Workspace, Microsoft 365, Atlassian, Stripe Verified, OpenAI Verified, Next.js, Google Analytics 4",
  "socialLinksCsv": "https://github.com/stripe"
}
```

---

## Connect to Claude Desktop / Cursor via Apify MCP
Add this Actor to your AI agent toolset using the official Apify MCP Server:
```json
{
  "mcpServers": {
    "apify-b2b-tools": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "willowy_catamaran_fco/b2b-domain-email-tech-scraper"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

## Keywords & Integrations
`b2b-lead-generation, email-finder, clearbit-alternative, tech-stack-detector, clay-enrichment, n8n-workflow, apify-actor, mcp-server`
