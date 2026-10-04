import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Don't draw header/footer on cover page (page 1)
        if self._pageNumber > 1:
            # Header
            self.drawString(54, 11 * 72 - 36, "FACEBOOK PAGE CONTENT MONETIZATION MASTER PLAYBOOK (2026)")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)
            
            # Footer
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(8.5 * 72 - 54, 36, page_text)
            self.drawString(54, 36, "CONFIDENTIAL & LICENSED MATERIAL • SKILLSQUERY.COM • SUPPORT: TECHPOSITIVE2002@GMAIL.COM")
            self.line(54, 48, 8.5 * 72 - 54, 48)
            
        self.restoreState()

def create_playbook(output_pdf_path):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=colors.HexColor('#0F172A'),
        alignment=1, # Center
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1,
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        leftIndent=15,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1E293B')
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # ------------------ COVER PAGE ------------------
    story.append(Spacer(1, 30))
    story.append(Paragraph("META CONTENT MONETIZATION SYSTEM (2026)", ParagraphStyle(
        'CoverSuper',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2563EB'),
        alignment=1,
        spaceAfter=10
    )))
    story.append(Paragraph("FACEBOOK PAGE MONETIZATION<br/>MASTER PLAYBOOK", title_style))
    story.append(Paragraph("THE ZERO-FACE BLUEPRINT FOR IN-STREAM ADS, REELS & PERFORMANCE BONUS", subtitle_style))
    story.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor('#2563EB'), spaceAfter=20))

    # Embed Desktop Pure Screen Dashboard
    if os.path.exists("assets/fb_proof_desktop_pure.jpg"):
        story.append(Image("assets/fb_proof_desktop_pure.jpg", width=460, height=258))
        story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Official Training Manual & Execution Standard</b><br/>Published by SkillsQuery Publishing House • Updated for 2026 Meta Algorithm", ParagraphStyle(
        'CoverMeta',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#64748B'),
        alignment=1
    )))
    
    story.append(Spacer(1, 20))

    # Meta Overview Box
    meta_summary_data = [
        [Paragraph("<b>Audience Target:</b> Tier-1 (USA, UK, CA, AU)", callout_style), Paragraph("<b>Expected RPM:</b> $15.00 - $35.00 / 1K views", callout_style)],
        [Paragraph("<b>Production Engine:</b> 100% Faceless AI Systems", callout_style), Paragraph("<b>Settlement:</b> Direct SWIFT Wire on the 21st", callout_style)],
        [Paragraph("<b>Official Support:</b> techpositive2002@gmail.com", callout_style), Paragraph("<b>Delivery Model:</b> Instant PDF with Lifetime Updates", callout_style)],
    ]
    t_summary = Table(meta_summary_data, colWidths=[240, 240])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_summary)
    story.append(PageBreak())

    # ------------------ MODULE 1: THE ELIGIBILITY ENGINE ------------------
    story.append(Paragraph("MODULE 1: The 2026 Meta Content Monetization Architecture", h1_style))
    story.append(Paragraph(
        "In 2026, Meta completely retired legacy Creator Studio in favor of the unified <b>Meta Content Monetization (CM)</b> platform. Under this framework, creators no longer manage separate silos for Ads on Reels, In-Stream Ads, and Bonuses. A single status unlock monetizes all qualifying public content across videos, reels, photos, and stories.",
        body_style
    ))

    # Two column status: Mobile App Proof & Explanation
    col1_data = []
    if os.path.exists("assets/fb_proof_mobile_pure.jpg"):
        col1_data.append(Image("assets/fb_proof_mobile_pure.jpg", width=180, height=320))
    
    col2_text = (
        "<b>Core Eligibility Checklist (Unified CM):</b><br/>"
        "• <b>Followers Threshold:</b> 5,000 active profile/page followers.<br/>"
        "• <b>Engagement Requirement:</b> 60,000 eligible minutes viewed within the last 60 days.<br/>"
        "• <b>Active Publishing:</b> At least 5 active original or transformative videos published.<br/>"
        "• <b>Policy Standing:</b> 100% green compliance on Partner Monetization Policies.<br/><br/>"
        "<b>Why Most Creators Fail:</b><br/>"
        "90% of aspiring creators get disqualified because of unoriginal duplicate re-uploads (Limited Originality of Content - LOC) or attempting to purchase bot followers that trigger security flags."
    )
    
    t_mod1 = Table([[col1_data[0] if col1_data else "", Paragraph(col2_text, body_style)]], colWidths=[200, 300])
    t_mod1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_mod1)
    story.append(Spacer(1, 10))

    # 30-Day Setup Roadmap Table
    story.append(Paragraph("<b>The 30-Day Fast-Track Roadmap</b>", h2_style))
    roadmap_data = [
        [Paragraph("<b>Phase</b>", callout_style), Paragraph("<b>Days</b>", callout_style), Paragraph("<b>Action Items & Milestones</b>", callout_style)],
        [Paragraph("Foundation", callout_style), Paragraph("Days 1 - 5", callout_style), Paragraph("Create Page in Professional Mode. Establish niche branding, complete bio, set up 2FA, post 10 baseline warm-up photo posts.", callout_style)],
        [Paragraph("Seed Content", callout_style), Paragraph("Days 6 - 15", callout_style), Paragraph("Publish 2 high-retention 4:5 aspect ratio Reels daily. Seed content into 3 target auto-approved niche groups.", callout_style)],
        [Paragraph("Viral Cascade", callout_style), Paragraph("Days 16 - 25", callout_style), Paragraph("Execute the 1:5 group sharing ratio formula. Target Tier-1 peak hours (8:00 PM - 11:30 PM EST). Cross 60,000 watch minutes.", callout_style)],
        [Paragraph("CM Submission", callout_style), Paragraph("Days 26 - 30", callout_style), Paragraph("Audit Partner Policy health. Submit application via Professional Dashboard. Link Indian Bank SWIFT/PAN.", callout_style)],
    ]
    t_roadmap = Table(roadmap_data, colWidths=[90, 70, 340])
    t_roadmap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_roadmap)
    story.append(PageBreak())

    # ------------------ MODULE 2: HIGH-RPM NICHES & TIER-1 TARGETING ------------------
    story.append(Paragraph("MODULE 2: High-RPM Niches & Tier-1 Geo-Targeting Strategy", h1_style))
    story.append(Paragraph(
        "A common pitfall for Indian creators is generating millions of views strictly from local domestic audiences, resulting in an effective RPM of $0.05 to $0.20 per thousand views. By configuring your content to appeal to Tier-1 nations (USA, United Kingdom, Canada, Australia), your payout multiplies by 20x to 100x ($15 to $35 RPM).",
        body_style
    ))

    # Niche Matrix Table
    niche_data = [
        [Paragraph("<b>Niche Category</b>", callout_style), Paragraph("<b>Tier-1 RPM Range</b>", callout_style), Paragraph("<b>Content Formats</b>", callout_style), Paragraph("<b>Production Difficulty</b>", callout_style)],
        [Paragraph("Personal Finance & Wealth Hacks", callout_style), Paragraph("$22.00 - $38.00", callout_style), Paragraph("AI Voiceover + Motion Infographics", callout_style), Paragraph("Low (Canva/CapCut)", callout_style)],
        [Paragraph("Luxury Real Estate & Mansions", callout_style), Paragraph("$18.00 - $32.00", callout_style), Paragraph("Curated Tour Clips + Ambient Music", callout_style), Paragraph("Very Low", callout_style)],
        [Paragraph("AI Tools & Future Tech", callout_style), Paragraph("$16.00 - $28.00", callout_style), Paragraph("Screen Demos + Automated Subtitles", callout_style), Paragraph("Low", callout_style)],
        [Paragraph("Mindset, Stoicism & Motivation", callout_style), Paragraph("$12.00 - $22.00", callout_style), Paragraph("Cinematic 4K Visuals + Deep AI Voice", callout_style), Paragraph("Very Low", callout_style)],
        [Paragraph("Wildlife & Rare Nature Wonders", callout_style), Paragraph("$10.00 - $18.00", callout_style), Paragraph("Documentary Cuts + Fast-Paced Hooks", callout_style), Paragraph("Low", callout_style)],
    ]
    t_niche = Table(niche_data, colWidths=[140, 95, 175, 90])
    t_niche.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#DBEAFE')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#93C5FD')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#BFDBFE')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_niche)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>The 4 Secrets to Attracting 80%+ Tier-1 Traffic from India:</b>", h2_style))
    story.append(Paragraph("<b>1. English-Only Audio & Metadata:</b> Eliminate Hindi captions, hashtags, and text overlays entirely. Every title, caption, and voiceover must be clear neutral English.", bullet_style))
    story.append(Paragraph("<b>2. Synchronize Upload Times with US Primetime:</b> Post between 7:30 PM and 11:30 PM IST (which corresponds to 9:00 AM to 1:00 PM EST in the United States).", bullet_style))
    story.append(Paragraph("<b>3. Geo-Targeted Group Seeding:</b> Share strictly into US and UK community groups (such as 'US Homeowners Tips', 'Texas Real Estate Investors', 'Tech Professionals California').", bullet_style))
    story.append(Paragraph("<b>4. Meta Distribution Algorithm Cue:</b> Facebook evaluates the location of the first 20 viewers of your video. If the first 20 engagements originate from Tier-1 geos, the recommendation feed pushes the video to North America.", bullet_style))
    
    story.append(Spacer(1, 8))

    # Real App Card Showcase inline
    if os.path.exists("assets/fb_real_meta_app_card.png"):
        t_card = Table([[
            Image("assets/fb_real_meta_app_card.png", width=140, height=140),
            Paragraph(
                "<b>Verified Meta Performance Case:</b><br/>"
                "Real creator dashboard showing <b>$1,315.79 in monthly earnings</b> (+348% growth) generated from US-targeted Reels and performance bonus tools.<br/><br/>"
                "<i>Notice the breakdown: Reels contributed $1,187.55 and Extra Bonus contributed $118.00 from short, zero-face 45-second clips.</i>",
                body_style
            )
        ]], colWidths=[150, 350])
        t_card.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t_card)

    story.append(PageBreak())

    # ------------------ MODULE 3: THE 100% FACELESS AI GENERATION PIPELINE ------------------
    story.append(Paragraph("MODULE 3: The 100% Faceless AI Production Engine", h1_style))
    story.append(Paragraph(
        "You do not need expensive camera gear, studio lighting, or voice recording equipment. Top-earning Facebook pages are built entirely using AI automation engines that generate scripts, synthetic human voices, cinematic imagery, and dynamic auto-captions in under 8 minutes per video.",
        body_style
    ))

    # 4-Step Pipeline Flowchart
    pipeline_data = [
        [Paragraph("<b>Step 1: Scripting</b>", callout_style), Paragraph("<b>ChatGPT / Claude 3.5</b><br/>Input viral retention prompt. Generate high-hook 45-second script with 3-second tension opener.", callout_style)],
        [Paragraph("<b>Step 2: Voiceover</b>", callout_style), Paragraph("<b>ElevenLabs (Adam / Rachel Voice)</b><br/>Generate 128kbps crystal-clear voiceover at 1.1x speed to maintain dopamine engagement.", callout_style)],
        [Paragraph("<b>Step 3: Visuals</b>", callout_style), Paragraph("<b>Midjourney v6 / Flux / Pexels 4K</b><br/>Generate photorealistic 1080x1350 (4:5) frames designed specifically for Facebook mobile feed real-estate.", callout_style)],
        [Paragraph("<b>Step 4: Assembly</b>", callout_style), Paragraph("<b>CapCut Pro / Premiere Rush</b><br/>Auto-generate kinetic bounce captions, add ambient boom sfx, apply 0.3s zoom cuts every 2.5 seconds.", callout_style)],
    ]
    t_pipeline = Table(pipeline_data, colWidths=[120, 380])
    t_pipeline.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#F1F5F9')),
        ('BACKGROUND', (1,0), (1,-1), colors.HexColor('#FFFFFF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_pipeline)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Production Master Prompt for ChatGPT (Copy & Paste):</b>", h2_style))
    prompt_box_data = [[Paragraph(
        "Act as an elite Facebook Content Monetization viral producer. Write a 45-second high-dopamine script on the topic: '[INSERT TOPIC]'.<br/>"
        "Requirements:<br/>"
        "1. The first 3 seconds MUST have a pattern interrupt that forces the viewer to stop scrolling.<br/>"
        "2. Structure: Hook (0-3s) -> Intriguing Problem (3-15s) -> 3 Rapid Value Points (15-35s) -> Comment Question Hook (35-45s).<br/>"
        "3. Write in short punchy sentences suitable for rapid text-to-speech audio.<br/>"
        "4. Provide visual asset descriptions for every 3 seconds of voiceover.",
        code_style
    )]]
    t_prompt = Table(prompt_box_data, colWidths=[500])
    t_prompt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_prompt)
    story.append(PageBreak())

    # ------------------ MODULE 4: THE 24-HOUR VIRALITY FORMULA ------------------
    story.append(Paragraph("MODULE 4: The 24-Hour 1,000,000+ Reach Virality Hack", h1_style))
    story.append(Paragraph(
        "Unlike YouTube where discovery relies heavily on Search & Browse features, Facebook is a <b>social graph and community sharing machine</b>. A brand new page with 0 followers can generate 500,000+ reach in 24 hours if you trigger Meta's auto-recommendation threshold through strategic group seeding.",
        body_style
    ))

    # The 1:5 Sharing Law Box
    sharing_law_data = [[
        Paragraph(
            "<b>THE GOLDEN 1:5 SHARING RATIO LAW:</b><br/>"
            "• <b>Never share directly from the Page Admin account:</b> This triggers Facebook's automated spam filters instantly.<br/>"
            "• <b>Use 3 to 5 separate Aged Contributor Profiles:</b> Assign them as 'Moderators' or simple community members.<br/>"
            "• <b>Maximum 1 share per profile per group per 4 hours:</b> Total shares across all groups should not exceed 15 in the first 2 hours.<br/>"
            "• <b>The Viral Tipping Point:</b> If a video achieves 15 group shares and generates 40 comments within 60 minutes, Facebook's algorithm flags the post as 'High Velocity Content' and pushes it to millions of organic news feeds.",
            callout_style
        )
    ]]
    t_law = Table(sharing_law_data, colWidths=[500])
    t_law.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_law)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>How to Identify Auto-Approved Facebook Groups:</b>", h2_style))
    story.append(Paragraph("• <b>Test Post Verification:</b> Before publishing your video, join candidate groups and make a test 1-sentence text post. If it appears on the feed immediately without 'Pending Admin Approval', the group is Auto-Approved.", bullet_style))
    story.append(Paragraph("• <b>Public Status:</b> Only target groups that are marked as <b>Public</b>. Private group shares cannot be viewed by users outside the group and do not count toward monetization minutes.", bullet_style))
    story.append(Paragraph("• <b>Member Activity Ratio:</b> Select groups with at least 50,000 members and a minimum of 10 posts per day.", bullet_style))
    story.append(Paragraph("• <b>Group Vault Strategy:</b> Maintain an active spreadsheet of 25 auto-approved groups categorized by niche.", bullet_style))

    story.append(PageBreak())

    # ------------------ MODULE 5: ANTI-STRIKE & LOC BYPASS ------------------
    story.append(Paragraph("MODULE 5: Anti-Strike & Limited Originality of Content (LOC) Bypass", h1_style))
    story.append(Paragraph(
        "The #1 reason pages lose monetization is the dreaded <b>Limited Originality of Content (LOC)</b> flag. This happens when Facebook's Rights Manager detects unedited footage or audio tracks that exist elsewhere in Meta's database. Follow our strict transformative editing rules to remain 100% compliant.",
        body_style
    ))

    # LOC Bypass Rules Table
    loc_rules_data = [
        [Paragraph("<b>Violation Risk</b>", callout_style), Paragraph("<b>Meta Detection Vector</b>", callout_style), Paragraph("<b>Guaranteed Solution & Bypass Rule</b>", callout_style)],
        [Paragraph("Direct Video Copying", callout_style), Paragraph("Pixel Hash & Frame Match", callout_style), Paragraph("Apply 1.05x speed shift + 3% zoom crop + subtle color LUT filter.", callout_style)],
        [Paragraph("Copyright Background Audio", callout_style), Paragraph("Audio Waveform Fingerprint", callout_style), Paragraph("Use only licensed audio from Meta Sound Collection or original ElevenLabs voice tracks.", callout_style)],
        [Paragraph("Static Re-upload Slideshows", callout_style), Paragraph("Low Movement Detection", callout_style), Paragraph("Add dynamic pan & zoom motion + animated text overlays on every frame.", callout_style)],
        [Paragraph("Unattributed Clip Usage", callout_style), Paragraph("Content Rights Match", callout_style), Paragraph("Add genuine transformative commentary voiceover that adds educational or comedic value.", callout_style)],
    ]
    t_loc = Table(loc_rules_data, colWidths=[120, 140, 240])
    t_loc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#FEE2E2')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F87171')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#FECACA')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_loc)
    story.append(Spacer(1, 10))

    # Real Student Chat Evidence
    if os.path.exists("assets/fb_chat_1.png"):
        story.append(Paragraph("<b>Student Verification Case Study:</b>", h2_style))
        t_chat = Table([[
            Image("assets/fb_chat_1.png", width=160, height=320),
            Paragraph(
                "<b>Case Study: Samay Singh (5 Pages Approved in 1 Week)</b><br/><br/>"
                "Samay implemented the LOC bypass formula detailed above across 5 newly created niche pages.<br/><br/>"
                "• <b>Previous Result:</b> Every previous page was hit with 'Limited Originality' within 10 days.<br/>"
                "• <b>After Implementing Playbook:</b> All 5 pages received official Meta Content Monetization approval status simultaneously with zero policy strikes.<br/>"
                "• <b>Key Technique Used:</b> 3-point transformative editing + Meta Sound Collection audio layers.",
                body_style
            )
        ]], colWidths=[180, 320])
        t_chat.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(t_chat)

    story.append(PageBreak())

    # ------------------ MODULE 6: PAYOUT SETUP & BANK WIRE ------------------
    story.append(Paragraph("MODULE 6: Meta Payout Setup & Indian Bank Wire Settlement", h1_style))
    story.append(Paragraph(
        "Meta pays out earned balances monthly on the <b>21st of each month</b> for earnings generated in the prior calendar month. Setting up your payout profile correctly avoids payment holds and unnecessary tax withholding.",
        body_style
    ))

    # Payout Wire Proof
    if os.path.exists("assets/fb_proof_payout.jpg"):
        story.append(Image("assets/fb_proof_payout.jpg", width=420, height=260))
        story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Step-by-Step Bank Payout Configuration:</b>", h2_style))
    story.append(Paragraph("<b>1. Business Type Selection:</b> Always select <b>Individual / Sole Proprietorship</b>. Never select Partnership or Corporation unless you have an active GST registered company.", bullet_style))
    story.append(Paragraph("<b>2. Tax Information (W-8BEN for Indian Citizens):</b> As a non-US resident, input your Indian PAN card number in the 'Foreign Tax Identifying Number' field. Claim 0% US withholding tax treaty benefits.", bullet_style))
    story.append(Paragraph("<b>3. Bank Account & SWIFT Code:</b> Enter your Indian Bank Account Number and your branch's official <b>8 or 11 character SWIFT/BIC code</b> (available from SBI, HDFC, ICICI, etc.). Do NOT enter an IFSC code for international wire transfer.", bullet_style))
    story.append(Paragraph("<b>4. Threshold & Deposit Schedule:</b> Meta's international wire threshold is $100. Payouts are finalized on the 10th and dispatched on the 21st directly to your bank account via SWIFT.", bullet_style))

    story.append(PageBreak())

    # ------------------ BONUS SECTION: 500+ VIRAL HOOKS VAULT ------------------
    story.append(Paragraph("BONUS VAULT: 50+ High-Retention Viral Hook Templates", h1_style))
    story.append(Paragraph(
        "The first 3 seconds of your video determine 80% of its total reach. Below are battle-tested hook formulas categorized by psychological trigger that consistently achieve 60%+ 3-second view rates on Facebook.",
        body_style
    ))

    hook_table_data = [
        [Paragraph("<b>Category</b>", callout_style), Paragraph("<b>Viral Hook Template (Plug & Play)</b>", callout_style)],
        [Paragraph("Curiosity Gap", callout_style), Paragraph("\"Most people have no idea this simple trick exists, but once you see it...\"", callout_style)],
        [Paragraph("Negative Threat", callout_style), Paragraph("\"Stop doing this immediately if you don't want to regret it next month...\"", callout_style)],
        [Paragraph("Behind the Scenes", callout_style), Paragraph("\"This is the exact hidden method that million-dollar creators never share publicly...\"", callout_style)],
        [Paragraph("Contrarian Fact", callout_style), Paragraph("\"Everyone tells you to do [X], but the data actually proves the exact opposite...\"", callout_style)],
        [Paragraph("Time Urgency", callout_style), Paragraph("\"You only have a few weeks left before Meta changes this rule completely...\"", callout_style)],
        [Paragraph("Financial Proof", callout_style), Paragraph("\"Here is exactly what happened when I tested this underground method for 14 days...\"", callout_style)],
        [Paragraph("Secret Knowledge", callout_style), Paragraph("\"If you're still working 8 hours a day, watch this before you make your next move...\"", callout_style)],
    ]
    t_hooks = Table(hook_table_data, colWidths=[120, 380])
    t_hooks.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E0E7FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#818CF8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#C7D2FE')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_hooks)
    story.append(Spacer(1, 15))

    # Official Support & Licensing Box (PII Cleaned)
    support_box_data = [[
        Paragraph(
            "<b>OFFICIAL STUDENT SUPPORT & VERIFICATION:</b><br/>"
            "This document is an authorized digital asset issued by SkillsQuery.Com.<br/>"
            "For all queries, implementation questions, or algorithmic updates, contact our desk:<br/>"
            "<b>Official Email:</b> techpositive2002@gmail.com<br/>"
            "<b>Response Commitment:</b> Every email is reviewed within 24 business hours.<br/>"
            "© 2026 SkillsQuery.Com. All Rights Reserved.",
            callout_style
        )
    ]]
    t_support = Table(support_box_data, colWidths=[500])
    t_support.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_support)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Master Illustrated PDF generated successfully at: {output_pdf_path}")

if __name__ == "__main__":
    out_pdf = os.path.join(os.path.dirname(__file__), "Facebook_Page_Monetization_Master_Playbook_2026.pdf")
    create_playbook(out_pdf)
