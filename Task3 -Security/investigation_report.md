# Security Log Investigation – Final Report

**Internship:** EdVyro Virtual Cyber Security Internship  
**Task:** Task 3 – Security Log Investigation  
**Domain:** Cyber Security  
**Log Date:** 24 October 2026  
**Investigation Type:** Authentication Log Analysis

## 1. Executive Summary

This project analyzes synthetic authentication logs to identify suspicious login patterns and possible security incidents.

The investigation identified repeated failed login attempts against multiple user accounts, repeated attempts against an administrator account, and a subsequent successful administrator login.

## 2. Objective

- Analyze authentication log records.
- Identify suspicious login activities.
- Detect possible password spraying.
- Detect possible brute-force attempts.
- Document important events in a timeline.
- Prepare an investigation report.

## 3. Tools and Technologies

- Python
- Visual Studio Code
- Windows PowerShell
- CSV log processing

## 4. Findings

### Finding 1 – Possible Password Spraying

Source IP: `192.168.1.45`

Five different user accounts received failed login attempts within a short period.

**Assessment:** Pattern is consistent with possible password spraying.

### Finding 2 – Possible Brute-Force Attempts

Source IP: `203.0.113.50`

The administrator account received ten failed login attempts between 09:05:10 and 09:06:18.

**Assessment:** Pattern is consistent with possible brute-force activity.

### Finding 3 – Successful Administrator Login

Source IP: `198.51.100.25`

The administrator account successfully logged in at 09:12:30 and performed an access event at 09:15:42.

**Assessment:** Requires further verification. The available logs do not establish whether the login was authorized.

## 5. Evidence Summary

| Evidence | Observation |
|---|---|
| Multiple account failures | Five accounts targeted |
| Repeated admin failures | Ten failed attempts |
| Successful admin login | Login recorded |
| Admin access event | Access recorded |
| Logout event | Session ended successfully |

## 6. Recommendations

- Implement multi-factor authentication (MFA).
- Apply account lockout or progressive login delays.
- Monitor repeated failed login attempts.
- Review administrator account activity.
- Maintain centralized security logs.
- Investigate unusual successful logins.

## 7. Limitations

- All supplied log entries are synthetic.
- No real system compromise is established.
- IP addresses do not identify a person.
- Additional endpoint, network, and authentication evidence would be needed for confirmation.

## 8. Conclusion

The investigation demonstrates basic authentication log analysis and identification of suspicious login patterns. It highlights the importance of monitoring authentication activity and documenting security events systematically.

**Project Status:** Documentation prepared. Findings are based on synthetic test data.