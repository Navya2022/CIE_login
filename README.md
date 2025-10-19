# Flask Login Vercel

This project is a simple login page built using Python Flask, designed to be hosted on Vercel. It includes a basic backend for user authentication and a frontend for user interaction.

## Project Structure

```
flask-login-vercel
├── api
│   └── index.py          # Main backend script for the Flask application
├── templates
│   └── login.html        # HTML structure for the login page
├── static
│   ├── css
│   │   └── styles.css     # CSS styles for the login page
│   └── js
│       └── app.js         # JavaScript for client-side functionality
├── tests
│   └── test_auth.py       # Unit tests for authentication functionality
├── .gitignore              # Files and directories to be ignored by Git
├── requirements.txt        # List of dependencies required for the project
├── runtime.txt             # Python version for the Vercel environment
├── vercel.json             # Configuration settings for Vercel deployment
└── README.md               # Documentation for the project
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

Follow the instructions on Vercel to deploy the application. Ensure that the `runtime.txt` and `vercel.json` files are correctly configured for your environment.