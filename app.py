from flask import Flask, render_template, request,redirect, url_for,flash
from dotenv import load_dotenv
import os 
import smtplib
from email.message import EmailMessage

load_dotenv()
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
    
    email = EmailMessage()
    email['Subject'] = f'New message from {name}'
    email['From'] = os.environ['SENDER_EMAIL']
    email['To'] = os.environ['RECEIVER_EMAIL']
    email['Reply-to'] = sender_email

    email.set_content(
        f'Name: {name}\n'
        f'Email: {sender_email}\n\n'
        f'Message:\n{message}'
    )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(
                os.environ['SENDER_EMAIL'],
                os.environ['SENDER_PASSWORD']
            )
            server.send_message(email)

        flash('Your message has been sent successfully!', 'success')

    except (smtplib.SMTPException, OSError, KeyError):
        app.logger.exception('Email sending failed')
        flash('Failed to send your message. Please try again.', 'error')

    return redirect(url_for('contactme'))

if __name__ == '__main__':
    app.run(debug=True)