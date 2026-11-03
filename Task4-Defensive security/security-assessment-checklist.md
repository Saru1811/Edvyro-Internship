# Security Assessment Checklist

**Project:** Defensive Security Assessment Capstone  
**Application:** Flask Secure Authentication Lab  
**Internship:** EdVyro Virtual Cyber Security Internship

## 1. Configuration Security

- [ ] Check whether debug mode is disabled.
- [ ] Check whether the application uses a secure secret key.
- [ ] Check session cookie security settings.
- [ ] Confirm HTTPS is required before production deployment.

## 2. Authentication Security

- [ ] Test user registration.
- [ ] Test login with valid credentials.
- [ ] Test login with an incorrect password.
- [ ] Check password length validation.
- [ ] Verify passwords are stored as hashes.
- [ ] Check login rate limiting.

## 3. Session Management

- [ ] Verify a session is created after successful login.
- [ ] Check access to protected routes without login.
- [ ] Test logout functionality.
- [ ] Verify the session is cleared after logout.
- [ ] Check session expiration settings.

## 4. Input Validation

- [ ] Test empty username input.
- [ ] Test empty password input.
- [ ] Test very long input values.
- [ ] Test invalid JSON requests.
- [ ] Verify appropriate error responses.

## 5. Dependency Security

- [ ] Review installed Python packages.
- [ ] Check dependency versions.
- [ ] Review known security advisories.
- [ ] Update vulnerable dependencies where appropriate.

## 6. Logging and Error Handling

- [ ] Check whether application errors are handled safely.
- [ ] Verify sensitive information is not exposed in error messages.
- [ ] Check whether useful security events are logged.
- [ ] Avoid recording passwords or session secrets in logs.

## 7. Final Verification

- [ ] Record test results.
- [ ] Document identified security issues.
- [ ] Apply suitable fixes.
- [ ] Repeat failed tests after fixing.
- [ ] Prepare the final assessment report.

**Note:** Mark a checkbox only after performing and verifying the corresponding test.