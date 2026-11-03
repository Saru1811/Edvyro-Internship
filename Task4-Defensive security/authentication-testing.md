# Authentication Testing

## 1. Project
Defensive Security Assessment – Secure Authentication Application

## 2. Objective
To evaluate the authentication functionality and identify possible weaknesses in the login and session management process.

## 3. Test Environment
- Application: Flask Secure Authentication App
- Environment: Localhost
- Testing Type: Authorized security testing
- Tools: Browser, Python, Flask

## 4. Authentication Test Cases

| Test ID | Test Description | Expected Result | Actual Result |
|---|---|---|---|
| AT01 | Login with valid credentials | User should log in successfully | Pending |
| AT02 | Login with invalid password | Login should be rejected | Pending |
| AT03 | Login with unknown username | Login should be rejected | Pending |
| AT04 | Access protected page without login | Access should be denied | Pending |
| AT05 | Access protected page after login | Access should be allowed | Pending |
| AT06 | Logout from application | User session should end | Pending |
| AT07 | Access protected page after logout | Access should be denied | Pending |

## 5. Security Checks

- Passwords should be stored using secure password hashing.
- Invalid login attempts should not expose sensitive information.
- Protected routes should require authentication.
- Session handling should be properly configured.
- Logout should invalidate the authenticated session.

## 6. Test Results

Testing status: Pending.

Actual results must be recorded after performing each test on the local application.

## 7. Conclusion

Authentication testing helps verify whether the application protects user accounts and restricts unauthorized access.

**Note:** This document contains test cases and expected results. It does not confirm that the tests have passed.