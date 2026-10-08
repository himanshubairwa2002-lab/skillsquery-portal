// Razorpay Webhook Handler: /api/webhook.js
// Handles payment.captured / order.paid events
// Automatically dispatches PDF download link via Email and logs transaction

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed. Use POST.' });
  }

  try {
    const event = req.body;

    if (event && (event.event === 'payment.captured' || event.event === 'order.paid')) {
      const payment = event.payload?.payment?.entity;
      const email = payment?.email;
      const contact = payment?.contact;
      const notes = payment?.notes || {};
      const customerName = notes.name || 'Valued Reader';

      console.log(`[Razorpay Webhook] Received payment ${payment?.id} of ₹${(payment?.amount || 9900) / 100} from ${email || 'customer'}`);

      if (email) {
        const pdfDownloadUrl = 'https://www.skillsquery.com/hairfall-hacks/downloads/99-Hair-Hacks-Master-Book.pdf';
        const supportEmail = 'techpositive2002@gmail.com';

        const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #0b0f19; color: #e2e8f0; margin: 0; padding: 20px; }
    .card { max-width: 600px; margin: 0 auto; background-color: #121829; border: 1px solid #1e293b; border-radius: 16px; padding: 32px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
    .badge { display: inline-block; background-color: #10b981; color: #000; font-weight: 800; font-size: 11px; padding: 4px 10px; border-radius: 9999px; text-transform: uppercase; margin-bottom: 12px; }
    h1 { color: #ffffff; font-size: 24px; margin-top: 0; margin-bottom: 12px; }
    p { color: #cbd5e1; font-size: 15px; line-height: 1.6; }
    .cta-btn-green { display: block; text-align: center; background: linear-gradient(135deg, #10b981, #059669); color: #ffffff !important; font-weight: 900; font-size: 16px; padding: 16px 24px; border-radius: 12px; text-decoration: none; margin: 20px 0; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4); }
    .checklist { background-color: #0b0f19; border: 1px solid #334155; border-radius: 12px; padding: 16px; margin: 20px 0; }
    .item { color: #a7f3d0; font-size: 14px; margin: 6px 0; }
    .footer { font-size: 12px; color: #64748b; text-align: center; margin-top: 28px; border-top: 1px solid #1e293b; padding-top: 16px; }
  </style>
</head>
<body>
  <div class="card">
    <span class="badge">Payment Verified • ₹99</span>
    <h1>Your 99 Hair Hacks Master Book is Here! 🌿</h1>
    <p>Hi <strong>${customerName}</strong>,</p>
    <p>Thank you for your purchase (Payment ID: <code>${payment?.id}</code>). Your publication-grade bilingual edition containing all 99 tested kitchen hair remedies is ready:</p>

    <a href="${pdfDownloadUrl}" class="cta-btn-green" target="_blank">
      📖 Download Master Book (Bilingual PDF • 2.85 MB)
    </a>

    <div class="checklist">
      <div style="font-weight: bold; color: #ffffff; margin-bottom: 8px;">Inside Your Guide:</div>
      <div class="item">✅ All 99 Verified Kitchen Hair Hacks (with tsp/tbsp ratios)</div>
      <div class="item">✅ Side-by-side Hindi + English bilingual text</div>
      <div class="item">✅ 3-Day Emergency Hairfall Control Protocol</div>
      <div class="item">✅ Essential Blood Test & Scalp Deficiency Matrix</div>
    </div>

    <div class="footer">
      <p>Have questions? Reach our Support Desk anytime at:</p>
      <p><a href="mailto:${supportEmail}" style="color: #34d399; font-weight: bold;">${supportEmail}</a></p>
      <p>&copy; 2026 99 Hair Hacks. All rights reserved.</p>
    </div>
  </div>
</body>
</html>
        `;

        if (process.env.RESEND_API_KEY) {
          await fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: process.env.EMAIL_FROM || '99 Hair Hacks <onboarding@resend.dev>',
              to: [email],
              subject: '🎉 Your 99 Hair Hacks Master Book (Download Link Inside)',
              html: emailHtml
            })
          });
        }
      }

      return res.status(200).json({ status: 'ok', message: 'Webhook processed successfully' });
    }

    return res.status(200).json({ status: 'ignored' });
  } catch (error) {
    console.error('[Razorpay Webhook Error]:', error);
    return res.status(500).json({ error: error.message });
  }
}
