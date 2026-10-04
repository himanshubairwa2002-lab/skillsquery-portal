import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
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
        # Top banner line (except on cover page)
        if self._pageNumber > 1:
            self.setStrokeColor(colors.HexColor('#F59E0B')) # Amber
            self.setLineWidth(1.5)
            self.line(40, letter[1] - 35, letter[0] - 40, letter[1] - 35)
            
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor('#9CA3AF'))
            self.drawString(42, letter[1] - 30, "SKILLSQUERY.COM  |  FACELESS YOUTUBE & META MONETIZATION SYSTEM (2026)")
            
            # Footer
            self.setStrokeColor(colors.HexColor('#1F2937'))
            self.setLineWidth(0.8)
            self.line(40, 42, letter[0] - 40, 42)
            
            self.setFont("Helvetica", 8)
            self.drawString(42, 30, "CONFIDENTIAL & PROPRIETARY  •  All Rights Reserved  •  support@skillsquery.com")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(letter[0] - 42, 30, page_text)
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=42,
        rightMargin=42,
        topMargin=48,
        bottomMargin=50
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1, # Center
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#FBBF24'), # Amber-400
        alignment=1,
        spaceAfter=25
    )
    
    badge_style = ParagraphStyle(
        'Badge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#10B981'),
        alignment=1,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#F59E0B'),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#111827'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#1F2937'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#374151'),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=0
    )

    prompt_style = ParagraphStyle(
        'PromptText',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#111827')
    )

    elements = []
    
    # ==================== COVER PAGE ====================
    elements.append(Spacer(1, 40))
    
    # Dark card container for cover
    cover_data = [
        [Paragraph("SKILLSQUERY PLATINUM PLAYBOOK", badge_style)],
        [Paragraph("FACELESS YOUTUBE & META<br/>MONETIZATION BLUEPRINT", title_style)],
        [Paragraph("The Complete 2026 AI-Driven System for Million+ Organic Views & Tier-1 RPM Monetization", subtitle_style)],
        [Paragraph("<b>OFFICIAL EDITION:</b> 2026.4 &nbsp;|&nbsp; <b>RETAIL VALUE:</b> $199 / ₹1,999 &nbsp;|&nbsp; <b>VERIFIED BY:</b> SkillsQuery Creator Labs", ParagraphStyle('CoverMeta', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, textColor=colors.HexColor('#9CA3AF'), alignment=1))]
    ]
    
    cover_table = Table(cover_data, colWidths=[letter[0]-84])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')), # Slate 900
        ('TOPPADDING', (0,0), (-1,-1), 32),
        ('BOTTOMPADDING', (0,0), (-1,-1), 32),
        ('LEFTPADDING', (0,0), (-1,-1), 24),
        ('RIGHTPADDING', (0,0), (-1,-1), 24),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 2, colors.HexColor('#F59E0B')),
    ]))
    elements.append(cover_table)
    elements.append(Spacer(1, 30))

    # Executive Summary Box
    summary_html = """
    <b>EXECUTIVE BLUEPRINT SUMMARY:</b><br/>
    This master playbook breaks down the exact operational roadmap to build, automate, and monetize faceless video assets across Facebook and YouTube without ever showing your face, recording voiceovers on mic, or having prior editing skills.<br/><br/>
    <b>Key Metrics Addressed:</b>
    • <b>Target CPM / RPM:</b> $15.00 – $42.00 (Focusing on Tier-1 US, UK, Canada & Australian audiences)<br/>
    • <b>Production Turnaround:</b> 1 Long-Form Video (8–11 mins) in under 35 minutes via AI pipeline<br/>
    • <b>Monetization Milestone:</b> Fast-track 60,000 Facebook watch minutes & 1,000 YPP subscribers inside 30 days.
    """
    summary_p = Paragraph(summary_html, body_style)
    summary_box = Table([[summary_p]], colWidths=[letter[0]-84])
    summary_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')), # Amber 100
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ]))
    elements.append(summary_box)
    elements.append(Spacer(1, 20))

    # Table of contents preview
    toc_data = [
        ["Module / Section", "Core Focus", "Outcome"],
        ["Module 1: High-RPM Niche Engineering", "Top 15 Tier-1 Niches & Competitor Hacking", "$15-$40 RPM Target"],
        ["Module 2: AI Scripting & Retention Loops", "Curiosity Gap Framework & Open Loops", ">65% Retention Rate"],
        ["Module 3: Ultra-Realistic Voiceovers", "ElevenLabs Settings & Cinematic Audio", "100% Human Feel"],
        ["Module 4: Google Flow & AI Video Pipeline", "Veo, Midjourney & CapCut 10-Min Flow", "Zero Camera Recording"],
        ["Module 5: Viral Packaging (CTR 10%+)", "Color Theory, Outlier Titles & Psychology", ">10% Click-Through Rate"],
        ["Module 6: Multi-Stream Monetization", "YPP, FB Stars, Affiliates & Sponsorships", "4 Revenue Streams"],
        ["Bonus 1: 100+ High-CTR Prompt Vault", "Ready-to-paste prompts for AI tools", "Instant Execution"],
        ["Bonus 2: Top 50 Niches Database", "US RPM vs Difficulty Matrix", "Data-Backed Niche Selection"]
    ]
    toc_table = Table(toc_data, colWidths=[150, 230, 140])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.HexColor('#FFFFFF')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
    ]))
    elements.append(toc_table)
    elements.append(PageBreak())

    # ==================== MODULE 1 ====================
    elements.append(Paragraph("MODULE 1: HIGH-RPM & EVERGREEN NICHE ENGINEERING", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))
    
    elements.append(Paragraph("<b>The Foundation: Why 90% of Creators Make Less Than $100/Month</b>", h2_style))
    elements.append(Paragraph(
        "The biggest beginner mistake is picking a broad entertainment or meme niche. An Indian entertainment video getting 1,000,000 views might generate $80 – $150. In stark contrast, a US finance, luxury real estate, or AI tech video with 1,000,000 views generates <b>$15,000 – $38,000</b>. The difference is advertiser competition and geographical purchasing power.",
        body_style
    ))
    
    elements.append(Paragraph("<b>Top 5 High-RPM Evergreen Niches for 2026:</b>", h2_style))
    elements.append(Paragraph("• <b>1. Personal Finance & Debt Restructuring (RPM: $28 - $45):</b> Credit score repair, mortgage interest loopholes, bankruptcy lessons from history.", bullet_style))
    elements.append(Paragraph("• <b>2. Geopolitics & Macroeconomics (RPM: $18 - $34):</b> Global debt dominance, dollar de-dollarization, central bank gold accumulation.", bullet_style))
    elements.append(Paragraph("• <b>3. B2B AI Automation & SaaS Case Studies (RPM: $22 - $38):</b> How 1-person companies use AI agents to automate $100k/mo businesses.", bullet_style))
    elements.append(Paragraph("• <b>4. Luxury Engineering & Billionaire Real Estate (RPM: $15 - $26):</b> Megaproject failures, private island tours, hypercar secrets.", bullet_style))
    elements.append(Paragraph("• <b>5. Dark Psychology & Stoic History (RPM: $12 - $22):</b> Ancient battle strategies, cognitive biases, historical mystery investigations.", bullet_style))

    elements.append(Paragraph("<b>Competitor Outlier Reverse-Engineering:</b>", h2_style))
    elements.append(Paragraph(
        "Never guess topics. Open YouTube or Facebook in an Incognito window, search for top channels in your niche, sort videos by 'Most Popular' within the last 60 days, and identify outlier videos that gained 5x–10x more views than the channel's subscriber count. These proven topic blueprints validate market interest.",
        body_style
    ))
    elements.append(Spacer(1, 10))

    # ==================== MODULE 2 ====================
    elements.append(Paragraph("MODULE 2: AI SCRIPTWRITING & RETENTION ARCHITECTURE", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))

    elements.append(Paragraph("<b>The 4-Beat Narrative Architecture (Target Retention: >65%):</b>", h2_style))
    elements.append(Paragraph("Every high-performing viral video script adheres to a rigid psychological structure:", body_style))
    elements.append(Paragraph("• <b>Beat 1 (0:00 - 0:15) - The Violent Hook:</b> Shatter a core assumption. Example: <i>'In 2024, everyone thought the US housing market was untouchable. But behind closed doors, a single mathematical error was quietly triggering a $1 trillion collapse...'</i>", bullet_style))
    elements.append(Paragraph("• <b>Beat 2 (0:15 - 0:45) - The Emotional Contract:</b> Explain why this matters right now to the viewer and seed the first mystery loop.", bullet_style))
    elements.append(Paragraph("• <b>Beat 3 (0:45 - 6:30) - Micro-Loops & Escalation:</b> Every 90 seconds, introduce a twist or counter-intuitive evidence before resolving the previous point.", bullet_style))
    elements.append(Paragraph("• <b>Beat 4 (6:30 - End) - The Climax & Future Loop:</b> The grand realization + an open question directing viewers to subscribe and watch the next recommended video.", bullet_style))
    
    # Prompt Callout
    prompt_box_data = [[
        Paragraph("""<b>MASTER SCRIPTING PROMPT (Copy into Claude 3.5 / ChatGPT 4o):</b><br/>
        <i>"Act as an award-winning documentary scriptwriter (similar to Magnates Media or ColdFusion). Write a 1,800-word YouTube video script about [TOPIC]. Follow the 4-Beat Narrative Architecture. Insert exact retention open-loops at [01:30], [03:45], and [06:00]. Include clear [B-ROLL DIRECTOR NOTES: Visual description, audio cue] in brackets. Voice tone: Authoritative, cinematic, and deeply gripping. No generic filler."</i>""", prompt_style)
    ]]
    prompt_tbl = Table(prompt_box_data, colWidths=[letter[0]-84])
    prompt_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    elements.append(Spacer(1, 4))
    elements.append(prompt_tbl)
    elements.append(PageBreak())

    # ==================== MODULE 3 & 4 ====================
    elements.append(Paragraph("MODULE 3: ULTRA-REALISTIC ELEVENLABS VOICEOVERS", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))
    
    elements.append(Paragraph("<b>The Golden ElevenLabs Settings:</b>", h2_style))
    elements.append(Paragraph(
        "Robotic voices kill retention instantly. Use ElevenLabs Multilingual v2 with the following tuned calibration:<br/>"
        "• <b>Best Voices:</b> Adam (Deep documentary tone), Marcus (Authoritative investigative), Daniel (Warm storytelling).<br/>"
        "• <b>Stability:</b> <b>55%</b> (Below 50% causes emotional cracking; above 65% sounds flat and robotic).<br/>"
        "• <b>Clarity / Similarity Boost:</b> <b>78%</b> (Prevents vocal distortion while keeping pronunciation crisp).<br/>"
        "• <b>Style Exaggeration:</b> <b>5% - 8%</b> (Adds subtle vocal cadence and suspenseful micro-pauses).",
        body_style
    ))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("MODULE 4: GOOGLE FLOW, VEO & AI VIDEO WORKFLOW", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))
    
    elements.append(Paragraph("<b>The 10-Minute Video Generation Pipeline:</b>", h2_style))
    elements.append(Paragraph(
        "1. <b>AI Visual Generation:</b> Use Google Flow / Veo 2 / Midjourney v6.1 for cinematic establishing shots and hyper-realistic scene renders.<br/>"
        "2. <b>Stock Footage Layering:</b> Complement with 4K B-Roll from Pexels, Pixabay, and Storyblocks via direct API integration.<br/>"
        "3. <b>CapCut Pro / Premiere Kinetic Typography:</b> Auto-generate captions, apply the 'Bold Pop' yellow/white highlight preset, and set word grouping to 3–4 words per line for mobile viewing.<br/>"
        "4. <b>Sound Design Stacking:</b> Layer low atmospheric drones at -24dB beneath voiceover (-14 LUFS) and insert subtle whooshes/risers on every visual scene change (every 3–4 seconds).",
        body_style
    ))
    elements.append(Spacer(1, 10))

    # ==================== MODULE 5 & 6 ====================
    elements.append(Paragraph("MODULE 5: VIRAL PACKAGING & 10%+ CTR THUMBNAIL DESIGN", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))
    
    elements.append(Paragraph("<b>The 3-Color Rule for YouTube & Facebook Thumbnails:</b>", h2_style))
    elements.append(Paragraph(
        "High-CTR packaging requires visual contrast that immediately halts the scroll on mobile screens:<br/>"
        "• <b>Base Color (60%):</b> Dark Charcoal (#0F172A) or Midnight Navy.<br/>"
        "• <b>Contrast Focal Point (30%):</b> Vivid Electric Cyan (#06B6D4) or Warm Amber Yellow (#F59E0B).<br/>"
        "• <b>Urgency Accent (10%):</b> Crimson Red or Neon Lime.<br/>"
        "• <b>Text Constraint:</b> Maximum 3 to 4 words. The thumbnail must NOT repeat the title; it must complete the visual story.",
        body_style
    ))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("MODULE 6: THE 4-WAY REVENUE MULTIPLIER", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))

    elements.append(Paragraph(
        "Never rely solely on ad revenue. Monitored creators stack 4 concurrent income streams on every video asset:<br/>"
        "1. <b>AdSense & Facebook In-Stream Ads:</b> Base revenue generated passively per 1,000 views.<br/>"
        "2. <b>Facebook Stars & Performance Bonus:</b> Meta pays monthly cash bonuses for engagement on uploaded reels and long-form videos.<br/>"
        "3. <b>High-Ticket Affiliate Commissions:</b> Place targeted SaaS/fintech affiliate links in pinned comments ($50–$150 payout per free trial sign-up).<br/>"
        "4. <b>Digital Product Direct Sales:</b> Link self-serve guides, cheat sheets, or prompt vaults (like this ₹299 playbook) to turn 1% of viewers into paying customers.",
        body_style
    ))
    elements.append(PageBreak())

    # ==================== BONUS SECTION: PROMPT VAULT ====================
    elements.append(Paragraph("BONUS SECTION: 100+ HIGH-CTR VIRAL PROMPTS", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))

    prompts_data = [
        ["Use Case", "Ready-to-Use Prompt Template"],
        [
            "Viral Title Generator",
            "Generate 10 click-worthy YouTube titles for [TOPIC] using these 4 psychology frameworks: 1) Negative consequence ('Why You Should Stop...'), 2) Secret mechanism ('The Unknown Rule...'), 3) The Unbelievable Contrast ('How a 22yo made $1M...'), 4) Exposed reality. Limit to 50 characters."
        ],
        [
            "High-Retention Hook",
            "Write a 15-second opening hook for a video about [TOPIC]. Beat 1: Direct shock statement challenging conventional wisdom. Beat 2: Startling data point. Beat 3: Open-loop question. Under 35 words. Tone: Cinematic, urgent."
        ],
        [
            "Midjourney Thumbnail",
            "cinematic portrait of [CHARACTER/SYMBOL], dramatic moody lighting, split cyan and warm tungsten light, hyper-detailed 8k, shallow depth of field, photorealistic, 16:9 aspect ratio --ar 16:9 --v 6.1 --style raw"
        ],
        [
            "Facebook Reel Description",
            "Write a 2-line viral Facebook Reel caption for [TOPIC] with a high-curiosity question that sparks debates in the comments. Add 5 trending hashtags."
        ],
        [
            "Sponsorship Pitch",
            "Draft a 4-sentence cold outreach email to [BRAND] proposing an integrated 60-second video sponsorship for an upcoming documentary reaching 150k+ Tier-1 viewers in the [NICHE] demographic."
        ]
    ]

    p_table = Table(prompts_data, colWidths=[130, 390])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.HexColor('#FFFFFF')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    elements.append(p_table)
    elements.append(Spacer(1, 15))

    # ==================== CHECKLIST & NEXT STEPS ====================
    elements.append(Paragraph("30-DAY EXECUTION TIMELINE (ACTION CHECKLIST)", h1_style))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#F59E0B'), spaceAfter=8))

    checklist_data = [
        ["Day / Phase", "Action Items & Daily Deliverables", "Target Milestone"],
        ["Days 1 – 3", "Niche selection, competitor 60-day outlier audit, brand asset creation", "Channel & FB Page Setup"],
        ["Days 4 – 10", "Generate 5 long-form scripts & batch ElevenLabs voiceovers", "First 5 Videos Ready"],
        ["Days 11 – 20", "Edit videos via CapCut Pro, export 9:16 reels, design 3 thumbnails per video", "First 5 Uploads Published"],
        ["Days 21 – 30", "Analyze YouTube Studio / Meta Business Suite retention, double down on winners", "First 10,000 Views & Follower Growth"]
    ]
    cl_table = Table(checklist_data, colWidths=[100, 310, 110])
    cl_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F1F5F9'), colors.HexColor('#FFFFFF')]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
    ]))
    elements.append(cl_table)
    elements.append(Spacer(1, 20))

    # Support / Community Banner
    banner_text = """
    <b>NEED HELP OR HAVE QUESTIONS?</b><br/>
    Email our dedicated creator desk at <b>support@skillsquery.com</b>.<br/>
    Access our official knowledge ecosystem at <b>https://skillsquery.com</b> and <b>https://learn.skillsquery.com</b>.
    """
    banner_p = Paragraph(banner_text, ParagraphStyle('Banner', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, textColor=colors.HexColor('#065F46'), alignment=1))
    banner_tbl = Table([[banner_p]], colWidths=[letter[0]-84])
    banner_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#D1FAE5')), # Emerald 100
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#10B981')),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(banner_tbl)

    # Build the document
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == '__main__':
    output_pdf = "Faceless_YouTube_Meta_Monetization_Playbook_2026.pdf"
    build_pdf(output_pdf)
