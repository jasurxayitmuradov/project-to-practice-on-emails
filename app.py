from flask import Flask, render_template, request,redirect, url_for,flash
from dotenv import load_dotenv
import os 
from email.message import EmailMessage
import resend

load_dotenv()

resend.api_key = os.environ["RESEND_API_KEY"]


app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/contactme')
def contactme():
    return render_template('contactme.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['POST'])
def contact():

    name = request.form.get('name','').strip()
    sender_email = request.form.get('email','').strip()
    message = request.form.get('message', '').strip()
    if not name or not sender_email or not message:
        flash('Please fill in all fields.', 'error')
        return redirect(url_for('contactme'))
    
    html_template = f"""
<div style="margin:0; padding:32px 12px; background-color:#f3f4f6;
            font-family:Arial,Helvetica,sans-serif; color:#111827;">
  <div style="max-width:600px; margin:0 auto; background:#ffffff;
              border:1px solid #e5e7eb; border-radius:16px; overflow:hidden;">

    <div style="padding:28px 32px; background:#111827; color:#ffffff;">
      <p style="margin:0 0 10px; color:#93c5fd; font-size:12px;
                font-weight:bold; letter-spacing:2px;">
        PERSONAL WEBSITE
      </p>
      <h1 style="margin:0; font-size:24px; line-height:1.4;">
        You've received a new message
      </h1>
      <p style="margin:10px 0 0; color:#d1d5db; font-size:14px;">
        Someone has contacted you through your website.
      </p>
    </div>

    <div style="padding:28px 32px;">
      <p style="margin:0 0 6px; color:#6b7280; font-size:12px;">
        FROM
      </p>
      <h2 style="margin:0 0 22px; font-size:20px;">
        {name}
      </h2>

      <div style="padding:14px 16px; margin-bottom:24px;
                  background:#f9fafb; border:1px solid #e5e7eb;
                  border-radius:10px;">
        <p style="margin:0 0 6px; color:#6b7280; font-size:12px;">
          EMAIL ADDRESS
        </p>
        <a href="mailto:{sender_email}"
           style="color:#2563eb; text-decoration:none;
                  font-size:14px; overflow-wrap:anywhere;">
          {sender_email}
        </a>
      </div>

      <p style="margin:0 0 12px; color:#6b7280; font-size:12px;
                font-weight:bold; letter-spacing:1px;">
        MESSAGE
      </p>
      <div style="padding:18px; background:#f9fafb;
                  border-left:4px solid #2563eb; border-radius:6px;
                  font-size:15px; line-height:1.8;
                  overflow-wrap:anywhere; white-space:pre-wrap;">
        {message}
      </div>

      <div style="margin-top:28px; text-align:center;">
        <a href="mailto:{sender_email}"
           style="display:inline-block; padding:13px 22px;
                  background:#2563eb; color:#ffffff;
                  text-decoration:none; border-radius:8px;
                  font-size:14px; font-weight:bold;">
          Reply to {name}
        </a>
      </div>
    </div>

    <div style="padding:20px 32px; background:#f9fafb;
                border-top:1px solid #e5e7eb; text-align:center;">
      <p style="margin:0; color:#6b7280; font-size:12px; line-height:1.7;">
        This message was sent through your personal website's contact form.
        <br>© 2026 Personal Website
      </p>
    </div>
  </div>
</div>
"""
    try:
        r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": [os.environ["RECEIVER_EMAIL"]],
            "subject": f"Message from {name}",
            "html": html_template
        })
        flash("Your message has been sent successfully!", "success")
    except:
        app.logger.exception("Resend email failed")
        flash("Failed to send your message. Please try again.", "error")


    return redirect(url_for('contactme'))

if __name__ == '__main__':
    app.run(debug=True)