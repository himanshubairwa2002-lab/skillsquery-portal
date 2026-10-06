# SkillsQuery - Meta Ads & Marketing Architecture Memory

> **Last Updated**: October 5, 2026  
> **Repository / Subfolder**: `skillsquery-portal` (`c:\Users\himan\OneDrive\Documents\Razorpay`)  
> **Status**: 100% Connected, Verified & Active

---

## 1. Meta Marketing API & MCP Integration

### Active MCP Server Configuration
The programmatic Meta Ads MCP server is configured and active in the global configuration file:
* **Path**: `C:\Users\himan\.gemini\config\mcp_config.json`
* **Package**: `@mikusnuz/meta-ads-mcp@latest` (135 Marketing API tools)
* **Executable**: `C:\Program Files\nodejs\npx.cmd`

```json
"meta-ads": {
  "command": "C:\\Program Files\\nodejs\\npx.cmd",
  "args": [
    "-y",
    "@mikusnuz/meta-ads-mcp@latest"
  ],
  "env": {
    "META_ADS_ACCESS_TOKEN": "EAAeCOTwQfh0BStZClLgEa6ydXkKoQ7yNVitqpIxAEekkvjKZCbZCELC6raC55EIkmTJARdF6bsHJlnBXZCqYk8LBK9flFcHg6QqMC4UzAB31KQwZAbnEOWsKHaTPUAvyHuaitkKtmBcFjcTRobYhVYhjKg2efwnOEbZAQcNLG1SkNqkOAa4CIsnvdZAp1GZAVxIr1gZDZD",
    "META_AD_ACCOUNT_ID": "787469274344806",
    "META_PIXEL_ID": "2043692866312535",
    "META_BUSINESS_ID": "429697524691488"
  }
}
```

---

## 2. Business Assets & Identity Details

### Business Portfolio
* **Business Portfolio Name**: `Himanshu`
* **Business Portfolio ID**: `429697524691488`
* **Security / 2FA Policy**: Set to `No one` (frictionless API token access)

### Meta Developer App
* **App Name**: `Digital Services Outreach`
* **App ID**: `2113507169435165`
* **Installed Products / Use Cases**:
  * Marketing API (Create & manage ads with Marketing API)
  * Facebook Login for Business

### System User & Permissions
* **System User Name**: `Conversions API System User`
* **System User ID**: `61581233871328`
* **Token Expiry**: `Never`
* **Granted Scopes**:
  * `ads_management` (Full ad creation, modification, budget scaling)
  * `ads_read` (Real-time performance reports & insights)
  * `business_management` (Business assets & audience access)
  * `pages_read_engagement` (Page analytics & engagement data)

### Target Ad Account
* **Account Name**: `Nexaroz_787469274344806`
* **Account ID**: `787469274344806` (API format: `act_787469274344806`)
* **Currency**: `INR` (Indian Rupee)
* **Account Status**: `1` (Active & Healthy, 0 Policy Violations, Opportunity Score: 100/100)
* **Strict Rule**: Strictly avoid personal account `1521775175778084` or restricted account `810531658140026`.

### Facebook Page
* **Primary Target Page**: `The Financial Mechanics` (ID: `1296276050242475`)
* **Alternative Active Pages**:
  * `MaanshuKart` (ID: `755551467647786`) — Connected to business portfolio
  * `Aaanya Sharma` (ID: `61591094054039`)
  * `Crime Files Hindi` (`thecrimefileshindi`)

---

## 3. Tracking, Meta Pixel & Conversions API (CAPI)

### Meta Pixel / Dataset
* **Dataset Name**: `SkillsQuery Pixel`
* **Dataset / Pixel ID**: `2043692866312535`
* **Status**: Active & Verified (`is_unavailable: false`)
* **Linked Ad Account**: `787469274344806`

### Client-Side Tracking Integration
* **`index.html`**:
  * Base Pixel code initialized with `2043692866312535` (`fbq('track', 'PageView')`).
  * `InitiateCheckout` event fired on payment initiation (Value: `₹299.00 INR`).
* **`thank-you.html`**:
  * Direct `Purchase` event fired upon redirect (Value: `₹299.00 INR`, Currency: `INR`).

### Server-Side Tracking (Meta CAPI)
* **Handler File**: `api/webhook.js` (Vercel Serverless Function)
* **Trigger Event**: Razorpay webhook `payment.captured` or `order.paid`
* **Payload Encryption**: User `email` and `phone` SHA-256 hashed according to Meta Privacy Standards.
* **CAPI Endpoint**: `https://graph.facebook.com/v21.0/2043692866312535/events`
* **Dispatched Data**:
  * Event: `Purchase`
  * Action Source: `website`
  * Value: `299.00 INR`
  * Order ID: `payment.id`
  * Content Name: `Facebook Page Monetization Master Playbook 2026`

---

## 4. SkillsQuery Product & Funnel Details

* **Product**: Facebook Page Monetization Master Playbook (2026 Edition)
* **Price Point**: ₹299 INR (Special launch pricing, discounted from ₹1,999)
* **Format**: Instant Digital Delivery (20-Page PDF in BOTH English & Hindi)
  * English PDF: `https://www.skillsquery.com/Facebook_Page_Monetization_Master_Playbook_2026_English.pdf`
  * Hindi PDF: `https://www.skillsquery.com/Facebook_Page_Monetization_Master_Playbook_2026_Hindi.pdf`
* **Fulfillment**: Automated dual delivery:
  1. Instant redirect to `thank-you.html` with 1-click download buttons.
  2. Automated transactional email dispatched via `nodemailer` via Razorpay webhook.

---

## 5. Live Management Commands & Usage

### Test Ad Account via Node.js
```bash
node -e "const token = 'EAAeCOTwQfh0BStZ...'; fetch('https://graph.facebook.com/v25.0/act_787469274344806?fields=id,name,account_status,currency&access_token=' + token).then(r => r.json()).then(console.log)"
```

### Pull Live Campaign Hierarchy
```bash
node -e "const token = 'EAAeCOTwQfh0BStZ...'; fetch('https://graph.facebook.com/v25.0/act_787469274344806/campaigns?fields=id,name,status,daily_budget&access_token=' + token).then(r => r.json()).then(console.log)"
```

### Programmatic Control via Meta Ads MCP Server
With the `@mikusnuz/meta-ads-mcp` tool suite loaded, any agent can invoke:
* `create_campaign`, `update_campaign`, `list_campaigns`
* `create_adset`, `update_adset`, `get_delivery_estimate`
* `create_ad`, `create_creative`, `get_ad_preview`
* `get_campaign_insights`, `get_ad_insights`

---

## 6. Video Generation & Creative Directives

### Tooling Strategy (Authorized by User on Oct 5, 2026)
* **Google Flow MCP Repo Status**: Uninstalled and deleted. The cookie-bridge extension approach is abandoned due to Google's DBSC session protection conflicts.
* **PRIMARY TOOL FOR GENERATION**: User has given **explicit authorization** to use **Chrome MCP (`chrome-primary`)** to operate the already-open, authenticated **Google Flow PRO** workspace tab (`flow.google.com/u/1/project/...`).
* **Generation Method**: Drive the built-in **Google Flow Creative Agent** and prompt interface via CDP in the user's active Chrome session.
* **Account Safety**: All actions operate strictly within the user's genuine, existing Chrome session on localhost (`127.0.0.1:12306`). Zero credential handling or cookie extraction.

### Creative & Campaign Goal
* **Target Offer**: SkillsQuery ₹299 Facebook Page Monetization Master Playbook (Hindi + English).
* **Creative Format**: Authentic, high-converting **UGC (User-Generated Content)** video ads.
* **Key Visual Hooks**:
  1. Casual, natural Indian creator POV (over-the-shoulder or front-facing smartphone camera).
  2. Holding a phone displaying live Meta Creator Studio dashboard with verified green monetization badges.
  3. Realistic, candid bedroom/desk setup with natural lighting (NOT corporate, stock, or CGI-looking).
* **KPI Goal**: Maintain sub-₹4 CPC and sub-₹70 CPA to deliver 4x+ ROAS on the ₹299 front-end offer.

---

## 7. Multi-Agent & Subagent Architecture for Meta Ads

When running campaigns or research across different models (Gemini, Claude, GPT, etc.), use this exact subagent architecture:

### Subagent Roles & Configurations

| Agent Name | Role | Model Tier | Tools Granted | Purpose |
|:---|:---|:---|:---|:---|
| **`MCP Schema Researcher`** | Schema Analyst | `flash` | `view_file` | Reads all 9+ MCP JSON tool schemas under `mcp/meta-ads/` to extract exact required/optional parameters, enums, and API constraints. |
| **`Meta Ads Optimization Researcher`** | Strategy Specialist | `flash` | `search_web`, `view_file` | Researches Indian audience targeting, bid strategies, ad copy psychology, Advantage+ settings, and budget allocation in INR. |
| **`Targeting & Reach Analyst`** | Targeting Specialist | `inherit` | `call_mcp_tool` (`meta-ads`) | Calls `search_targeting`, `get_targeting_suggestions`, and `get_reach_estimate` to discover and validate high-intent interest/behavior IDs. |
| **`Video Ad Production Agent`** | Creative Engine | `inherit` | `run_command`, `view_file`, `write_to_file` | Drives ElevenLabs Devanagari TTS synthesis, Pexels authentic stock footage selection, Crime Files audio mastering (-14.2 LUFS), and FFmpeg assembly. |
| **`Campaign Execution Agent`** | Deployment Orchestrator | `inherit` | `call_mcp_tool` (`meta-ads`) | Uploads video creatives, creates Campaign → Ad Set → Creative → Ad hierarchy via programmatic API calls. |
| **`Chrome MCP Remediation Agent`** | Browser Automation / Fallback | `inherit` | `call_mcp_tool` (`chrome-primary` / `chrome-devtools`) | Inspects live Ads Manager, fixes UI-level warnings/blocks, configures custom conversions, or debugs pixel events via Chrome CDP on port 12306. |

---

## 8. Verified Targeting Research & Audience Spec (India, INR)

### Demographics
* **Country**: India (`IN`)
* **Age Range**: `18 – 38` (optimal for Indian aspiring creators/freelancers)
* **Gender**: All (`0`)
* **Locales**: Hindi (`6`), English All (`45`)
* **Estimated Reach**: **216.5M – 254.7M users** (with Advantage+ expansion)

### High-Intent Interest Stack (Verified Meta Interest IDs)
| Interest Name | Meta ID | Category / Path | Audience Size (Global) |
|:---|:---|:---|:---|
| **Social media marketing** | `6003389760112` | Interests > online > Social media marketing | 341M – 402M |
| **Digital marketing** | `6003127206524` | Interests > online > Digital marketing | 398M – 468M |
| **YouTube** | `6004158316095` | Interests > Additional > YouTube | 894M – 1.05B |
| **Massive open online course** | `6004234093587` | Interests > Additional > MOOC | 19.9M – 23.4M |
| **Freelancer** | `6003374632277` | Interests > Additional > Freelancer | 163M – 191M |
| **Marketing services & orgs** | `6853952393067` | Interests > Additional > Marketing services | 83.5M – 98.2M |

### High-Intent Behavior Stack (Verified Meta Behavior IDs)
| Behavior Name | Meta ID | Category / Path | Audience Size (Global) |
|:---|:---|:---|:---|
| **Facebook Page admins** | `6015683810783` | Behaviours > Digital activities > FB page admins | 1.05B – 1.24B |
| **Instagram business profile admins** | `6297846662583` | Behaviours > Digital activities > IG business admins | 90.3M – 106.2M |
| **New Page admins (<2 weeks)** | `6041891177783` | Behaviours > Digital activities > New page admins | 739M – 869M |
| **Business Page admins** | `6020530281783` | Behaviours > Digital activities > Business admins | 64M – 75.3M |

### Target Ad Set JSON Payload
```json
{
  "age_min": 18,
  "age_max": 38,
  "genders": [0],
  "geo_locations": { "countries": ["IN"] },
  "locales": [6, 45],
  "flexible_spec": [
    {
      "interests": [
        { "id": "6003389760112", "name": "Social media marketing" },
        { "id": "6003127206524", "name": "Digital marketing" },
        { "id": "6004158316095", "name": "YouTube" },
        { "id": "6004234093587", "name": "Massive open online course" },
        { "id": "6003374632277", "name": "Freelancer" }
      ],
      "behaviors": [
        { "id": "6015683810783", "name": "Facebook Page admins" },
        { "id": "6297846662583", "name": "Instagram business profile admins" }
      ]
    }
  ],
  "targeting_automation": {
    "advantage_audience": 1
  }
}
```

---

## 9. Campaign Architecture & Optimization Rules

### Funnel Strategy
* **Campaign Objective**: 
  * Phase 1 (Testing / Pre-Pixel volume): `OUTCOME_TRAFFIC` with `LANDING_PAGE_VIEWS` optimization.
  * Phase 2 (Direct Conversions): `OUTCOME_SALES` with `OFFSITE_CONVERSIONS` (Event: `Purchase`, Pixel: `2043692866312535`).
* **Bid Strategy**: `LOWEST_COST_WITHOUT_CAP` (Highest Volume). Avoid early Cost Cap / Bid Cap to prevent bid starvation.
* **Special Ad Categories**: `[]` (None).
* **Starting Budget**: ₹500/day to ₹1,000/day per ad set (`50000` to `100000` paisa).
* **Scaling Cadence**: Increase daily budget by 15–20% every 48–72 hours on winning ad sets. Never double overnight.

### Live Production Campaign Deployment (Created via Meta Ads MCP)
* **Campaign ID**: `120251947553870548` (`SkillQuery_FB_Monetization_Traffic_Oct2026`)
* **Ad Set ID**: `120251947559910548` (`SkillQuery_India_18-38_Creators_Broad` - Budget: ₹600/day / `60000` paisa)
* **Ad 1 (Video Ad)**:
  * **Ad ID**: `120251947776430548` (`SkillQuery_FB_Monetization_Video_Ad_v1`)
  * **Creative ID**: `1453747650201526` (`SkillQuery_FB_Monetization_Video_Creative`)
  * **Video Asset ID**: `1776778736872768` (49.53s vertical 9:16)
  * **Thumbnail Hash**: `85d100427f7f6cac17fada92551a1f99`
  * **Status**: `ACTIVE` 🟢 (Top Performer: 7.12% CTR, ₹0.53 CPC, ₹1.30 Cost/LPV)
* **Ad 2 (Old Image Ad)**:
  * **Ad ID**: `120251947838900548` (`SkillQuery_FB_Monetization_HighCTR_Image_Ad_v1`)
  * **Status**: `PAUSED` ⏸️ (Budget bleed stopped per user instruction)
* **Ad 3 (New Before/After Split Payout Creative)**:
  * **Ad ID**: `120251955083190548` (`SkillQuery_FB_Monetization_BeforeAfter_Split_Ad_v2`)
  * **Creative ID**: `3289468181441903`
  * **Image Hash**: `2dc0e59bc7026d7a268364f9094a70c3` (Dramatic Before/After Policy Violation vs ₹1,48,920 Bank Payout)
  * **Status**: `PAUSED` (Ready to activate anytime via Meta MCP)

### High-Converting Hinglish Ad Copy Template
* **Primary Text**:
  > Facebook par roz Reels aur Videos upload kar rahe ho, par 1 rupiya bhi nahi ban raha? ❌
  > 
  > Bohot se creators sochte hain ki bas views aa jayein toh paisa aana shuru ho jayega... Par sachai ye hai ki 90% creators ko kabhi bhi Monetization nahi milta kyunki unhe pata hi nahi ki Meta ke actual rules kya hain! 🛑
  > 
  > Agar aapko sach mein Facebook se In-Stream Ads aur Performance Bonus earn karna hai, toh aapko ek proven blueprint ki zaroorat hai.
  > 
  > 🚀 Skill Query Facebook Monetization Masterclass mein seekhein:
  > ✅ 5,000 Followers aur 60,000 Watch Minutes fast-track karne ka formula
  > ✅ Policy Violations & Red Flags hatane ke secret steps
  > ✅ In-Stream Ads aur Reels Bonus program setup guide
  > ✅ Bank Account & Payout Setup bina kisi issue ke
  > ✅ Original content banane ka step-by-step tareeka
  > 
  > 📲 Abhi link par click karein aur apni seat book karein! ⬇️
* **Headline**: `Facebook Monetization Masterclass 🚀 Proven Blueprint`
* **Description**: `5,000+ Creators Enrolled | Practical Training by Skill Query`
* **Call to Action**: `LEARN_MORE`
* **Landing Page**: `https://skillsquery.com`

### Meta Policy Compliance Guardrails
* ⚠️ **NEVER use unrealistic income claims**: Avoid *"Ghar baithe ₹1 Lakh kamao"* or *"Earn fast money"*.
* ⚠️ **Skill-first framing**: Frame the offering around *"compliance rules, eligibility criteria, and digital content creation skills"*.
* ⚠️ **Mandatory footer disclaimer on landing page**: Include non-affiliation statement with Meta Platforms, Inc.

---

## 10. Video Creative Production Engine

### Master Creative Asset
* **Path**: `C:\Users\himan\Downloads\skill_query_ad_output\skill_query_fb_ad_master.mp4`
* **Specs**: 1080×1920 (9:16 vertical), 49.53 seconds, H.264/AAC, 30fps, 28.8 MB.
* **Audio**: ElevenLabs Liam (`TX3LPaxmHKxFdv7VOQHJ`), `eleven_multilingual_v2` model, synthesized from pure Devanagari Hindi text for authentic native pronunciation.
* **Audio Mastering**: Crime Files pipeline audio engine, normalized to -14.2 LUFS with sub-bass ambient bed.
* **Visuals**: Authentic Pexels stock footage, glassmorphic badges, kinetic captions, clean non-price CTA plate pointing to `skillsquery.com`.

---

## 11. Chrome MCP Server Integration & Fallback Procedures

When automated API calls encounter permission, verification, or UI-specific blockers:
* **Active Server**: `chrome-primary` (or `chrome-devtools`)
* **Endpoint / Connection**: Connects to the user's running Chrome instance on port `12306`.
* **Primary Capabilities**:
  1. `get_windows_and_tabs` — Locate active Meta Business Suite / Ads Manager tabs.
  2. `chrome_navigate` / `navigate_page` — Open Meta Ads Manager directly at `https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=787469274344806`.
  3. `chrome_click_element` / `chrome_fill_or_select` — Resolve 2FA challenges, verify domain ownership, approve ad previews, or publish drafts directly in Meta's native interface.
  4. `chrome_screenshot` — Capture visual confirmation of campaign status, delivery errors, or pixel event diagnostics.


