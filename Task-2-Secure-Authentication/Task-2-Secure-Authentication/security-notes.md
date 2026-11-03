# Security Implementation Notes

## 1. Password Hashing
The application uses Werkzeug's `generate_password_hash()` function to securely hash passwords before storing them.

The `check_password_hash()` function verifies passwords during login.

## 2. Server-Side Input Validation
The application checks:
- Username should not be empty.
- Password must contain at least 8 characters.
- Username and password must not exceed the permitted length.
- Invalid input requests are rejected.

## 3. Secure Session Management
Flask sessions are used to maintain authenticated user information.

Security settings:
- HttpOnly cookie enabled.
- SameSite set to Lax.
- Session expiry configured.
- Session data cleared during logout.

## 4. Logout Functionality
The logout endpoint clears the current session using `session.clear()`.

## 5. Login Error Handling
The application displays a generic error message:

`Invalid username or password`

This helps avoid revealing whether a username exists.

## 6. Rate Limiting
Rate limiting is a recommended security control to restrict repeated login attempts and reduce brute-force attacks.

**Implementation status:** Add and test a rate-limiting mechanism before claiming this feature is implemented.

## 7. Conclusion
These security measures demonstrate basic authentication protection in a local Flask application.