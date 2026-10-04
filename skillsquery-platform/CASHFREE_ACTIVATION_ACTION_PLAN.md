# Cashfree Payment Gateway Fast-Track Re-Activation & Setup SOP

## 1. Context & Diagnosis
- **Merchant ID:** `1279227`
- **Current Issue:** The account was previously registered under an inactive/dormant entity (`Nexaroz`) for physical goods/dropshipping. Due to dormancy and revised RBI guidelines, the live payment gateway mode is suspended until Video KYC (VCIP) is completed and website details are updated.
- **Dedicated Account Manager:** Nayana G (`nayana.g@cashfree.com`)
- **Support Contact:** `care@cashfree.com`

---

## 2. Fast-Track Action Steps to Get Payment Gateway Active

### Step 1: Update Domain & Category in Cashfree Merchant Dashboard
1. Log in to [Cashfree Dashboard](https://merchant.cashfree.com).
2. Go to **Settings** > **Domain & App Info**.
3. Click **Add Website / App URL** and enter:
   - Primary: `https://www.skillsquery.com`
   - Subdomain: `https://learn.skillsquery.com`
4. Update Business Category:
   - Select: **"Education / E-Learning / Digital Training & Coaching"**
   - Product Description: *"Self-paced digital masterclass, playbooks, prompts, and templates for YouTube and Facebook content creators."*

### Step 2: Ensure Mandatory Legal Compliance on Website (Already Implemented!)
Cashfree compliance auditors check 5 mandatory pages before enabling live PG. These are already built into our footer:
- **Terms & Conditions:** Outlines digital license, IP, and non-resale terms.
- **Privacy Policy:** Compliant with DPDP Act & international privacy standards.
- **Refund & Cancellation Policy:** Explicit 100% 7-Day Money-Back Guarantee.
- **Shipping & Delivery Policy:** Clarifies *"Instant Digital Access via download link immediately upon payment confirmation"*.
- **Contact Us:** Official support email (`support@skillsquery.com`) and response SLA (within 24 hours).

### Step 3: Schedule & Complete VCIP (Video KYC)
1. Send an email to Nayana G (`nayana.g@cashfree.com`) and `care@cashfree.com`:
   - **Subject:** *Urgent: VCIP Video KYC Request & Domain Update for Merchant ID 1279227 (SkillsQuery)*
   - **Body:**
     > Hi Nayana,
     > 
     > I have updated our business website to **https://www.skillsquery.com** offering self-paced digital education courses and playbooks for content creators.
     > All mandatory compliance policies (Terms, Privacy, Refund, Delivery, Contact) are live and active.
     > 
     > Please schedule my VCIP (Video KYC) verification link at the earliest so we can complete identity re-verification and enable live payment processing.
     > 
     > Merchant ID: 1279227  
     > Website: https://www.skillsquery.com
2. Once the VCIP link is received, complete the 2-minute video call with your original PAN and Aadhaar on hand.

---

## 3. Creating the ₹299 Cashfree Payment Form / Payment Link
Once live processing is unlocked (or using Cashfree Payment Forms):
1. In the Cashfree dashboard, navigate to **Payment Gateway** > **Payment Forms** (or **Payment Links**).
2. Click **Create Payment Form**:
   - **Title:** *YouTube & Facebook Automation Master Playbook (2026 Edition)*
   - **Amount:** `₹299`
   - **Customer Details Required:** Name, Email, Phone Number.
   - **Redirect URL on Success:** `https://www.skillsquery.com/thank-you.html`
3. Copy the generated Payment Link or Embed Form Code.
4. Plug the checkout URL directly into the `checkout-form` in `index.html`.
