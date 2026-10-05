// Vercel Serverless Function: /api/send-playbook
// Dispatches the Facebook Page Monetization Master Playbook (2026 Edition) to customer email

export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed. Use POST.' });
  }

  try {
    const { email, name } = req.body || {};

    if (!email || !email.includes('@')) {
      return res.status(400).json({ error: 'A valid email address is required.' });
    }

    const recipientName = (name && name.trim()) ? name.trim() : 'Valued Creator';
    const englishPdfUrl = 'https://www.skillsquery.com/Facebook_Page_Monetization_Master_Playbook_2026_English.pdf';
    const hindiPdfUrl = 'https://www.skillsquery.com/Facebook_Page_Monetization_Master_Playbook_2026_Hindi.pdf';
    const supportEmail = 'techpositive2002@gmail.com';

    // Rich HTML email template
    const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #0b0f19; color: #e2e8f0; margin: 0; padding: 20px; }
    .card { max-width: 600px; margin: 0 auto; background-color: #121829; border: 1px solid #1e293b; border-radius: 16px; padding: 32px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
    .badge { display: inline-block; background-color: #f59e0b; color: #000; font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; margin-bottom: 12px; }
    h1 { color: #ffffff; font-size: 24px; margin-top: 0; margin-bottom: 12px; }
    p { color: #cbd5e1; font-size: 15px; line-height: 1.6; }
    .highlight-box { background-color: #0b0f19; border: 1px solid #334155; border-radius: 12px; padding: 20px; margin: 24px 0; }
    .checklist-item { color: #a7f3d0; font-size: 14px; margin: 8px 0; }
    .cta-btn-blue { display: block; text-align: center; background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: #ffffff !important; font-weight: 800; font-size: 15px; padding: 14px 24px; border-radius: 12px; text-decoration: none; margin: 12px 0; box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4); }
    .cta-btn-gold { display: block; text-align: center; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #000000 !important; font-weight: 900; font-size: 15px; padding: 14px 24px; border-radius: 12px; text-decoration: none; margin: 12px 0; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4); }
    .footer { font-size: 12px; color: #64748b; text-align: center; margin-top: 32px; border-top: 1px solid #1e293b; padding-top: 20px; }
  </style>
</head>
<body>
  <div class="card">
    <span class="badge">Official Delivery</span>
    <h1>Your Facebook Monetization Master Playbook is Here! 🚀</h1>
    <p>Hi <strong>${recipientName}</strong>,</p>
    <p>Thank you for securing your copy of the <strong>Facebook Page Content Monetization Master Playbook (2026 Edition)</strong>.</p>
    <p>As promised, your purchase includes <strong>BOTH the English Edition and the संपूर्ण हिंदी संस्करण</strong>. You can download either or both editions below:</p>

    <div style="margin: 24px 0;">
      <!-- English Button -->
      <a href="${englishPdfUrl}" class="cta-btn-blue" target="_blank">
        📘 Download English Edition (20-Page PDF)
      </a>

      <!-- Hindi Button -->
      <a href="${hindiPdfUrl}" class="cta-btn-gold" target="_blank">
        📙 डाउनलोड करें हिंदी संस्करण (20-पेज संपूर्ण PDF)
      </a>
    </div>

    <div class="highlight-box">
      <div style="font-weight: bold; color: #ffffff; margin-bottom: 10px;">What's inside your 20-page manuals:</div>
      <div class="checklist-item">✅ 2026 Meta Content Monetization Architecture</div>
      <div class="checklist-item">✅ 30-Day Zero to $5,000/Month Implementation Blueprint</div>
      <div class="checklist-item">✅ Top 10 High-CPM Meta Niches ($15 - $35 RPM)</div>
      <div class="checklist-item">✅ 500+ Viral Hook & Caption Prompts Vault</div>
      <div class="checklist-item">✅ Indian Bank Payout Setup (SWIFT, W-8BEN, GST & ITR)</div>
    </div>

    <div class="footer">
      <p>Have questions or need help implementing? Reach our Creator Support Desk anytime at:</p>
      <p><a href="mailto:${supportEmail}" style="color: #60a5fa; font-weight: bold;">${supportEmail}</a></p>
      <p>&copy; 2026 SkillsQuery. All rights reserved.</p>
    </div>
  </div>
</body>
</html>
`;

    // 1. If RESEND_API_KEY is configured
    if (process.env.RESEND_API_KEY) {
      const resendRes = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: process.env.EMAIL_FROM || 'SkillsQuery <onboarding@resend.dev>',
          to: [email],
          subject: '🎉 Your Facebook Page Monetization Master Playbook (2026 Edition) - SkillsQuery',
          html: emailHtml
        })
      });

      const resendData = await resendRes.json();
      return res.status(200).json({
        success: true,
        provider: 'resend',
        result: resendData,
        message: `Master playbook successfully dispatched to ${email}`
      });
    }

    // 2. If SMTP / Nodemailer environment variables are configured
    if (process.env.SMTP_USER && process.env.SMTP_PASS) {
      try {
        const nodemailer = await import('nodemailer');
        const transporter = nodemailer.createTransport({
          service: 'gmail',
          auth: {
            user: process.env.SMTP_USER,
            pass: process.env.SMTP_PASS
          }
        });

        await transporter.sendMail({
          from: `"SkillsQuery Support" <${process.env.SMTP_USER}>`,
          to: email,
          subject: '🎉 Your Facebook Page Monetization Master Playbook (2026 Edition) - SkillsQuery',
          html: emailHtml
        });

        return res.status(200).json({
          success: true,
          provider: 'smtp',
          message: `Master playbook sent via SMTP to ${email}`
        });
      } catch (smtpErr) {
        console.error('SMTP Delivery error:', smtpErr);
      }
    }

    // 3. Fallback / Mock delivery when email provider API keys have not yet been placed in environment
    console.log(`[Email Dispatch Log] Customer ${email} requested playbook. Direct URL: ${pdfDownloadUrl}`);
    return res.status(200).json({
      success: true,
      provider: 'simulated',
      message: `Master playbook delivery registered for ${email}. Access link: ${pdfDownloadUrl}`,
      downloadUrl: pdfDownloadUrl
    });

  } catch (error) {
    console.error('Error handling playbook dispatch:', error);
    return res.status(500).json({ error: error.message || 'Internal server error' });
  }
}
