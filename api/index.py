# ...existing code...
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.getenv("SECRET_KEY", "fallback_key")
# Dummy user data for demonstration purposes
users = {
    "user@example.com": "password123",
    "navya@gmail.com": "navya12345"
}

@app.route('/')
def home():
    # show login page
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # use .get() to avoid KeyError when fields are missing
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash('Please provide both email and password.', 'warning')
        return redirect(url_for('home'))

    if email in users and users[email] == password:
        session['user'] = email
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('home'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    flash('Logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
# ...existing code...