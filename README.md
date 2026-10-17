# Flask Email Contact Form

A simple email contact form built with Flask and Python. This project demonstrates how to collect messages from a website contact form and deliver them to an email address using the **Resend API**.

## Demo

Here is a demonstration of the email contact form in action:

[Email Contact Form Demo](https://github.com/jasurxayitmuradov/project-to-practice-on-emails/blob/master/assets/email_demo.gif)

![Email Contact Form Demo](https://github.com/jasurxayitmuradov/project-to-practice-on-emails/raw/master/assets/email_demo.gif)

## Features

- Collects the sender's name, email address, and message.
- Sends emails using the Resend API.
- Stores API credentials and application secrets in environment variables.
- Validates required form fields.
- Displays success and error notifications.
- Redirects users after form submission.
- Supports deployment to a production hosting platform.

## Technologies Used

- **Python** — Backend programming language.
- **Flask** — Web framework.
- **HTML5** — Form structure.
- **CSS3** — Styling.
- **Bootstrap 5** — Responsive user interface.
- **Resend API** — Email delivery.
- **python-dotenv** — Environment variable management.
- **Render** — Application hosting.

## How It Works

1. A visitor fills out the contact form on the website.
2. The form submits its data to a Flask endpoint using the HTTP `POST` method.
3. Flask validates the submitted fields.
4. The application creates an email request and sends it to the Resend API.
5. Resend processes the request for email delivery.
6. The website displays a success or error notification and redirects the visitor.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jasurxayitmuradov/project-to-practice-on-emails.git
cd project-to-practice-on-emails
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux or macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install Flask python-dotenv resend
```

Alternatively, if the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
FLASK_SECRET_KEY=your_random_secret_key
RESEND_API_KEY=your_resend_api_key
RECEIVER_EMAIL=your_email@example.com
```

Replace the example values with your actual configuration.

- `FLASK_SECRET_KEY` — Used to secure Flask sessions and flash messages.
- `RESEND_API_KEY` — Your Resend API key.
- `RECEIVER_EMAIL` — The email address that receives contact form submissions.

Never commit your `.env` file or expose your API key in a public repository.

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser and navigate to the contact page to test the form.

## Deployment

The application is deployed on Render.

**Live Demo:** https://project-to-practice-on-emails.onrender.com/

To deploy your own instance, configure the required environment variables in your hosting platform's environment settings.

## Security

- Store API keys and secret keys in environment variables.
- Add `.env` and `.venv/` to `.gitignore`.
- Validate and safely handle all contact form inputs.
- Avoid enabling Flask debug mode in production.
- Consider implementing CSRF protection and rate limiting to prevent abuse.
- Never expose your Resend API key in client-side code.

## Integration

This contact form can be integrated into other Flask applications that need a simple email notification feature. The email delivery logic can be extended with additional validation, rate limiting, and error handling.

## Author

**Jasur Xayitmurodov**

GitHub: [@jasurxayitmuradov](https://github.com/jasurxayitmuradov)
