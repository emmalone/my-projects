---
title: "Contact / Get a Quote"
draft: false
menu:
  main:
    name: "Contact"
    weight: 100
---
Need a quote or have a question? We’ll get back to you quickly.

**Phone:** (555) 555-5555  
**Email:** [info@klminsurance.com](mailto:info@klminsurance.com)  
**Address:** 123 Main St, Anytown, PA 19000

<form name="contact" method="post" action="mailto:info@klminsurance.com" enctype="text/plain">
  <p><label>Your name<br>
    <input type="text" name="name" required></label></p>
  <p><label>Email<br>
    <input type="email" name="email" required></label></p>
  <p><label>How can we help?<br>
    <textarea name="message" rows="6" required></textarea></label></p>
  <p><button type="submit">Send</button></p>
</form>

<div style="font-size:0.9rem;opacity:0.7;">
This simple form uses your email client. We can switch to Netlify Forms or an AWS API (API Gateway + Lambda + SES) for a fully hosted form with autoresponders.
</div>
