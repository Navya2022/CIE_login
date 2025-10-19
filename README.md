# Flask Login Vercel

This project is a simple login page built using Python Flask, designed to be hosted on Vercel. It includes a basic backend for user authentication and a frontend for user interaction.

## Project Structure

```
flask-login-vercel/
├── api/
│   ├── index.py          # Main backend Flask script (Vercel Serverless Function)
│   ├── templates/
│   │   ├── login.html    # HTML structure for login page
│   │   └── dashboard.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── app.js
├── tests/
│   └── test_auth.py      # Unit tests for authentication
├── .gitignore
├── requirements.txt      # Dependencies
├── runtime.txt           # Python version for Vercel (e.g., python-3.11)
├── vercel.json           # Vercel deployment configuration
└── README.md

```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-login-vercel
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python api/index.py
   ```

5. **Access the login page**:
   Open your browser and go to `http://localhost:5000`.

## Usage

- Users can enter their credentials on the login page.
- The backend handles authentication and returns appropriate responses.

## Testing

To run the tests, use the following command:
```
pytest tests/test_auth.py
```

## Deployment

## Deployment

The application is deployed on Vercel and can be accessed at:
https://cie-login.vercel.app/ 

- The login page is available at the root URL `/`.
- Ensure you are using compatible browsers for proper rendering of the login dashboard.
