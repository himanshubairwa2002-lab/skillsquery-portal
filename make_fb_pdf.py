import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

pdf_path = r'c:\Users\himan\OneDrive\Documents\Razorpay\Facebook_Page_Monetization_Master_Playbook_2026.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Color Palette
C_PRIMARY = colors.HexColor('#0f172a')     # Dark Slate
C_ACCENT = colors.HexColor('#1877f2')      # Facebook Blue
C_GREEN = colors.HexColor('#10b981')       # Emerald Green
C_GOLD = colors.HexColor('#f59e0b')        # Amber Gold
C_CARD_BG = colors.HexColor('#f8fafc')     # Light Gray Background
C_TEXT = colors.HexColor('#1e293b')        # Body text

# Custom Typography Styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    alignment=TA_CENTER,
    textColor=C_PRIMARY
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
    textColor=C_ACCENT
)

h1_style = ParagraphStyle(
    'Header1',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=C_PRIMARY,
    spaceBefore=8,
    spaceAfter=4
)

h2_style = ParagraphStyle(
    'Header2',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=C_ACCENT,
    spaceBefore=5,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=C_TEXT
)

code_style = ParagraphStyle(
    'PromptCode',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=8,
    leading=11,
    textColor=colors.HexColor('#047857')
)

badge_style = ParagraphStyle(
    'Badge',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8,
    leading=10,
    alignment=TA_CENTER,
    textColor=colors.white
)

story = []

# --- PAGE 1: HEADER & CORE SYSTEM ARCHITECTURE ---
badge_p = Paragraph('OFFICIAL 2026 EDITION • COMPLETE FACEBOOK MONETIZATION BLUEPRINT', badge_style)
badge_table = Table([[badge_p]], colWidths=[360], rowHeights=[18])
badge_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), C_ACCENT),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(badge_table)
story.append(Spacer(1, 6))

story.append(Paragraph('FACEBOOK PAGE &amp; CONTENT MONETIZATION SYSTEM', title_style))
story.append(Spacer(1, 3))
story.append(Paragraph('The Complete Mobile &amp; Laptop Blueprint To Scale Viral Pages To $5,000+/Month', subtitle_style))
story.append(Spacer(1, 8))
story.append(HRFlowable(width='100%', thickness=1.5, color=C_ACCENT, spaceAfter=10))

# --- MODULE 1 ---
story.append(Paragraph('MODULE 1: The 2026 Meta Monetization Architecture', h1_style))
story.append(Paragraph('Facebook’s algorithm in 2026 prioritizes <b>Originality of Distribution</b> and <b>Audience Retention</b>. Understanding Meta’s payout channels is key to unlocking fast revenue:', body_style))
story.append(Spacer(1, 5))

m1_data = [
    [Paragraph('<b>Earning Channel</b>', body_style), Paragraph('<b>Qualification Requirement</b>', body_style), Paragraph('<b>Monthly Potential</b>', body_style), Paragraph('<b>Best Content Format</b>', body_style)],
    [Paragraph('<b>Meta Performance Bonus</b>', body_style), Paragraph('Invite-Only (Triggered by 15-20 daily high-engagement posts)', body_style), Paragraph('$1,500 – $8,500 / mo', body_style), Paragraph('AI Images, Polls, Quotes, Carousels', body_style)],
    [Paragraph('<b>In-Stream Ads</b>', body_style), Paragraph('5,000 Followers + 60,000 Eligible Minutes in 60 Days', body_style), Paragraph('$2,000 – $10,000 / mo', body_style), Paragraph('3+ Minute Edited Landscape / Vertical Videos', body_style)],
    [Paragraph('<b>Ads on Reels</b>', body_style), Paragraph('Invite-Only (Triggered by 100K+ Reels plays in 30 days)', body_style), Paragraph('$1,000 – $4,000 / mo', body_style), Paragraph('9:16 Vertical Reels (7 to 15s loops)', body_style)],
]
t_m1 = Table(m1_data, colWidths=[125, 160, 115, 140])
t_m1.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(t_m1)
story.append(Spacer(1, 10))

# --- MODULE 2 ---
story.append(Paragraph('MODULE 2: USA / Tier-1 High-RPM Page Setup (India Operation Blueprint)', h1_style))
story.append(Paragraph('To earn in US Dollars with high RPM ($15 – $35 per 1,000 views instead of $0.50 in Tier-3 countries), implement this setup from Day 1:', body_style))
story.append(Spacer(1, 3))
setup_steps = [
    '<b>1. Page Category & Naming:</b> Create the page under Business Category <i>\"Media/News Company\"</i> or <i>\"Creator\"</i>. Choose universally relatable English titles without regional slang.',
    '<b>2. Language & Timezone Sync:</b> Set page default language to English (US). Schedule primary posts between <b>6:00 PM to 2:00 AM IST</b> (8:30 AM to 4:30 PM US Eastern Time).',
    '<b>3. High-RPM Niches in 2026:</b> <i>Luxury Real Estate, American Historical Mysteries, DIY & Woodworking Crafts, Police Bodycam & Courtroom Psychology, Personal Finance Lessons</i>.',
    '<b>4. Payout Structuring:</b> In Meta Payouts, select <b>Individual / Sole Proprietorship</b>. Enter your legal PAN and Indian Bank Account with its SWIFT/BIC code (HDFC, ICICI, SBI, Axis). Meta handles automatic currency conversion into INR with zero friction.'
]
for step in setup_steps:
    story.append(Paragraph(f'• {step}', body_style))
    story.append(Spacer(1, 2))
story.append(Spacer(1, 6))

# --- MODULE 3 ---
story.append(Paragraph('MODULE 3: The 24-Hour Viral Group Sharing & Reach Multiplier (Anti-Ban Rules)', h1_style))
story.append(Paragraph('How top creators achieve 1,000,000+ reach in 24 hours without running paid Facebook Ads:', body_style))
story.append(Spacer(1, 3))
viral_steps = [
    '<b>The 3-Account Multiplier Stack:</b> Never share directly from your Page Admin profile. Use 2-3 aged secondary Facebook profiles (6+ months old) solely for interacting with groups.',
    '<b>Public Auto-Approval Groups:</b> Join 15-20 public Facebook groups in your exact niche that have \"Public Posting\" enabled without admin manual approval.',
    '<b>The 1:5 Golden Ratio Rule:</b> Before sharing your post, like 3 group posts and comment meaningfully on 2 posts. Then share your page video. This prevents Facebook anti-spam flags.',
    '<b>The Watch-Party & Recommendation Trigger:</b> When a video gets 15-20 organic shares within the first 60 minutes, Facebook flags it as trending and pushes it onto the global <i>\"Suggested for You\"</i> feed.'
]
for step in viral_steps:
    story.append(Paragraph(f'• {step}', body_style))
    story.append(Spacer(1, 2))

story.append(PageBreak())

# --- PAGE 2: AI CONTENT PRODUCTION & PROMPTS VAULT ---
story.append(Paragraph('MODULE 4: AI Content Creation Pipeline & Anti-Copyright Shield', h1_style))
story.append(Paragraph('How to produce 5 to 10 viral videos and image posts daily in under 45 minutes using free AI tools without getting copyright strikes or \"Limited Originality of Content\" (LOC) flags:', body_style))
story.append(Spacer(1, 4))

story.append(Paragraph('<b>1. The 3-Layer Visual Transformation (LOC Bypass):</b>', h2_style))
story.append(Paragraph('If curating public educational footage: (a) Crop by 5-8% to change original framing, (b) Apply subtle color grading (Saturation +5%, Warmth +4%), (c) Add kinetic animated captions in CapCut, and (d) Overlay copyright-free background ambient music.', body_style))
story.append(Spacer(1, 4))

story.append(Paragraph('<b>2. Master Scripting Prompt for Claude / DeepSeek:</b>', h2_style))
prompt_text = (
    "\"Write a 60-second viral Facebook Reel script about [TOPIC]. Follow this exact structure:<br/>"
    "• Seconds 0-3: Negative constraint hook (e.g., 'Never do this if you want...')<br/>"
    "• Seconds 4-20: Surprising revelation with fast pacing<br/>"
    "• Seconds 21-45: Three actionable takeaways with visual cues<br/>"
    "• Seconds 46-60: Open-loop question prompting high comment engagement.\""
)
prompt_p = Paragraph(prompt_text, code_style)
story.append(Table([[prompt_p]], colWidths=[540], style=[
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#86efac')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(Spacer(1, 8))

# --- MODULE 5 ---
story.append(Paragraph('MODULE 5: 10 High-Converting Viral Facebook Prompts Vault', h1_style))
hooks = [
    ('Mystery Hook', '\"Historians kept this discovery classified for decades until an ordinary traveler accidentally uncovered...\"'),
    ('Authority Reversal', '\"Almost everything you were told about luxury property investing is completely wrong. Here is why...\"'),
    ('Curiosity Gap', '\"In 1987, a cargo flight disappeared from radar for 42 minutes. When it landed, passengers reported this...\"'),
    ('High-Value DIY', '\"Master carpenters use this 20-second joint technique that makes standard furniture unbreakable...\"'),
    ('Finance Truth', '\"The 1 money rule wealthy families teach their children that ordinary schools will never mention...\"'),
    ('Controversy / Debate', '\"90% of homeowners make this critical mistake during home renovation that destroys property resale value...\"')
]
for title, text in hooks:
    story.append(Paragraph(f'<b>• {title}:</b> {text}', body_style))
    story.append(Spacer(1, 2))
story.append(Spacer(1, 8))

# --- MODULE 6 ---
story.append(Paragraph('MODULE 6: Payout Setup, Policy Compliance & 24/7 Student Support', h1_style))
story.append(Paragraph(
    '<b>Step-by-Step Payout Configuration for Indian Bank Accounts:</b><br/>'
    '1. <b>Payout Date:</b> Meta releases payouts on the <b>21st of every month</b> for earnings achieved in the previous calendar month.<br/>'
    '2. <b>Threshold:</b> Minimum payout threshold is $100 for Direct Wire Transfer.<br/>'
    '3. <b>Banking Information:</b> In Meta Business Suite Payout Settings, enter:<br/>'
    '&nbsp;&nbsp;&nbsp;• Account Holder Legal Name (Matches PAN)<br/>'
    '&nbsp;&nbsp;&nbsp;• Bank Account Number &amp; Bank SWIFT/BIC Code (Obtain from your local bank branch)<br/>'
    '&nbsp;&nbsp;&nbsp;• PAN Number (Required for Indian tax compliance)<br/>'
    '4. <b>Resolving Policy Issues:</b> If your page ever receives an Unoriginal Content flag, delete the flagged post, conduct 3 live video sessions (5 mins each) to verify human ownership, and request a review via Meta Creator Studio.<br/>'
    '5. <b>Direct 24/7 Student Support:</b><br/>'
    '&nbsp;&nbsp;&nbsp;• <b>Support Email:</b> techpositive2002@gmail.com<br/>'
    '&nbsp;&nbsp;&nbsp;• <b>Support WhatsApp / Phone:</b> +91 7302260772',
    body_style
))
story.append(Spacer(1, 12))

# Footer
story.append(HRFlowable(width='100%', thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=6))
story.append(Paragraph('© 2026 SkillsQuery.Com • Facebook Content Monetization System. All Rights Reserved.', ParagraphStyle(
    'FooterText', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, alignment=TA_CENTER, textColor=colors.HexColor('#64748b')
)))

doc.build(story)
print('Facebook Monetization PDF generated successfully at:', pdf_path)
