// Vercel Serverless Function: /api/webhook
// Razorpay Webhook handler to dispatch email upon payment.captured

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed. Use POST.' });
  }

  try {
    const event = req.body;

    // We listen to payment.captured or order.paid
    if (event && (event.event === 'payment.captured' || event.event === 'order.paid')) {
      const payment = event.payload?.payment?.entity;
      const email = payment?.email;
      const contact = payment?.contact;
      const notes = payment?.notes || {};
      const customerName = notes.name || 'Valued Creator';

      if (email) {
        console.log(`[Razorpay Webhook] Received payment ${payment.id} for ₹${payment.amount / 100} from ${email}`);

        const pdfDownloadUrl = 'https://www.skillsquery.com/Facebook_Page_Monetization_Master_Playbook_2026.pdf';
        const supportEmail = 'techpositive2002@gmail.com';

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
    .cta-btn { display: block; text-align: center; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #000000 !important; font-weight: 900; font-size: 16px; padding: 16px 28px; border-radius: 12px; text-decoration: none; margin: 24px 0; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4); }
    .footer { font-size: 12px; color: #64748b; text-align: center; margin-top: 32px; border-top: 1px solid #1e293b; padding-top: 20px; }
  </style>
</head>
<body>
  <div class="card">
    <span class="badge">Payment Verified • ₹299</span>
    <h1>Your Facebook Monetization Master Playbook is Here! 🚀</h1>
    <p>Hi <strong>${customerName}</strong>,</p>
    <p>We received your payment (Payment ID: <code>${payment.id}</code>). Your copy of the <strong>Facebook Page Content Monetization Master Playbook (2026 Edition)</strong> is ready for instant download below.</p>

    <div class="highlight-box">
      <div style="font-weight: bold; color: #ffffff; margin-bottom: 10px;">What's inside your deliverable:</div>
      <div class="checklist-item">✅ 30-Day Zero to ₹1,50,000/Month Blueprint</div>
      <div class="checklist-item">✅ Top 10 High-CPM Meta Niches ($15 - $35 RPM)</div>
      <div class="checklist-item">✅ 500+ Viral Hook & Caption Prompts Vault</div>
      <div class="checklist-item">✅ 24-Hour Viral Group Sharing & LOC Bypass Strategy</div>
      <div class="checklist-item">✅ Meta Pay Bank Setup & Indian SWIFT Wire Guide</div>
    </div>

    <a href="${pdfDownloadUrl}" class="cta-btn" target="_blank">
      📥 Click Here To Download Master Playbook (PDF)
    </a>

    <p style="font-size: 13px; color: #94a3b8; text-align: center;">
      Direct link: <a href="${pdfDownloadUrl}" style="color: #fbbf24;">${pdfDownloadUrl}</a>
    </p>

    <div class="footer">
      <p>Have questions or need assistance? Reach our Creator Support Desk anytime at:</p>
      <p><a href="mailto:${supportEmail}" style="color: #60a5fa; font-weight: bold;">${supportEmail}</a></p>
      <p>&copy; 2026 SkillsQuery. All rights reserved.</p>
    </div>
  </div>
</body>
</html>
`;

        // Send via Resend if RESEND_API_KEY is available
        if (process.env.RESEND_API_KEY) {
          await fetch('https://api.resend.com/emails', {
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
        }
      }
    }

    return res.status(200).json({ status: 'ok' });
  } catch (error) {
    console.error('Webhook error:', error);
    return res.status(500).json({ error: error.message });
  }
}
