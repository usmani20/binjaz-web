from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
secret_key = os.environ.get('FLASK_SECRET_KEY')
app.secret_key = secret_key # Required for flashing messages

# 1. HOME PAGE
@app.route('/')
def home():
    # This will load your index.html
    return render_template('index.html')

# 2. ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')

# 3. SERVICES (PROGRAMS) PAGE
@app.route('/services')
def services():
    return render_template('services.html')


# 4. INSIGHTS PAGE
@app.route('/insights')
def insights():
    return render_template('insights.html')

# --- Email Configuration ---
# --- Elite Titan Email Configuration ---
app.config['MAIL_SERVER'] = 'smtp.titan.email'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False # Titan prefers SSL on 465
app.config['MAIL_USERNAME'] = os.environ.get("MY_EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get("TITAN_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = ('Binjaz Briefing System', 'connect@binjaz.co')

mail = Mail(app)

# 5. CONTACT PAGE
@app.route('/contact', methods=['GET', 'POST'])

def contact():
    if request.method == 'POST':
        # Get data from the "Elite" form we built
        name = request.form.get('name')
        email = request.form.get('email')
        org = request.form.get('organization')
        role = request.form.get('designation')
        interest = request.form.get('interest')
        message = request.form.get('message')

        # Create the email message
        msg = Message(
            subject=f"New Briefing Request: {org} - {interest}",
            recipients=[os.environ.get("MY_EMAIL")],  # Where YOU want to receive it
            body=f"""
            New Capability Briefing Request via Binjaz.co:

            Name: {name}
            Email: {email}
            Organization: {org}
            Role: {role}
            Interest: {interest}

            Strategic Context/Message:
            {message}
            """
        )

        try:
            mail.send(msg)
            flash('Your request has been prioritized. A Binjaz consultant will reach out within 24 hours.', 'success')
        except Exception as e:
            flash('There was an error sending your request. Please try again or email us directly.', 'danger')
            print(f"Error: {e}")

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)