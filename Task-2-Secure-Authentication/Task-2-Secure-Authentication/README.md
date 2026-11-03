# Secure Authentication Lab

## 1. Project Overview

This project implements a small local authentication service using Python and Flask.

The main objective is to demonstrate secure authentication practices, including password hashing, server-side input validation, secure session management, and protection against repeated login attempts.

## 2. Technologies Used

- Python
- Flask
- Werkzeug Security
- Visual Studio Code
- PowerShell Terminal

## 3. Security Features

### Password Hashing
Passwords are stored as secure hashes instead of plain text using Werkzeug password-hashing functions.

### Server-Side Input Validation
The application validates incoming registration and login data before processing requests.

### Secure Session Management
The application uses session cookies with security settings such as HttpOnly and SameSite.

### Session Expiry
A session lifetime is configured to limit how long a user remains logged in.

### Logout
Users can end their session through the logout endpoint.

### Rate Limiting
Repeated login attempts should be restricted to reduce brute-force attacks.

### Generic Authentication Errors
The application returns a generic error message for invalid login attempts.

## 4. API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/register` | POST | Register a user |
| `/login` | POST | Authenticate a user |
| `/logout` | POST | End the user session |

## 5. How to Run the Project

1. Install Python.
2. Install the required libraries.
3. Open the project folder in Visual Studio Code.
4. Run the Flask application using:

`python app.py`

5. Test the API endpoints using PowerShell.

## 6. Testing Evidence

Screenshots will demonstrate registration, successful login, unsuccessful login, and logout.

## 7. Conclusion

This project demonstrates basic secure authentication practices in a local Flask application. It helps understand how password protection, input validation, session security, and login protection improve application security.

**Note:** This is an educational local demonstration, not a production-ready authentication system.