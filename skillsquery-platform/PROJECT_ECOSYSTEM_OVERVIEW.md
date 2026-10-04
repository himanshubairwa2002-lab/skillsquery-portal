# SkillsQuery Ecosystem Architecture & Deployment Manifest

## 1. Domain & Infrastructure Setup
- **Registrar:** Hostinger
- **Primary Domain:** `skillsquery.com`
- **DNS Host:** Hostinger Custom DNS (`ns1.dns-parking.com`, `ns2.dns-parking.com`)
- **Hosting & Edge CDN:** Vercel Global Edge Network
- **Repository:** `himanshubairwa2002-lab/skillsquery-portal` (GitHub main branch)

### Active DNS Record Mapping:
| Type | Record Name | Target / Destination | TTL | Active Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **A** | `@` *(Apex)* | `216.198.79.1` | `300` | Points main domain to Vercel |
| **CNAME** | `www` | `skillsquery.com` | `300` | Resolves `www.skillsquery.com` with auto SSL |
| **CNAME** | `learn` | `cname.vercel-dns.com` | `300` | Resolves `learn.skillsquery.com` for courses |

---

## 2. Directory Structure & Organization
```
Razorpay/
├── homepage.html                    # Ecosystem umbrella portal
├── index.html                       # Primary high-converting sales funnel
├── thank-you.html                   # Instant digital delivery & upsell page
├── vercel.json                      # Vercel deployment & routing config
└── skillsquery-platform/             # Master archive & project documentation
    ├── homepage.html
    ├── PROJECT_ECOSYSTEM_OVERVIEW.md
    ├── CASHFREE_ACTIVATION_ACTION_PLAN.md
    └── youtube-automation-course/    # YouTube Automation Course Assets
        ├── index.html               # Course sales funnel page
        ├── thank-you.html           # Course delivery & download page
        ├── COURSE_SYLLABUS_AND_PLAYBOOK.md
        ├── VIRAL_SCRIPTS_AND_PROMPTS.md
        └── HIGH_RPM_NICHES_DATABASE.md
```

---

## 3. Live Verified URLs
- [https://skillsquery.com](https://skillsquery.com) (HTTP 308 redirect to secure `www`)
- [https://www.skillsquery.com](https://www.skillsquery.com) (Live High-Converting Sales Funnel)
- [https://learn.skillsquery.com](https://learn.skillsquery.com) (Dedicated Education & Course Subdomain)
- [https://skillsquery-portal.vercel.app](https://skillsquery-portal.vercel.app) (Direct Vercel Edge Endpoint)
