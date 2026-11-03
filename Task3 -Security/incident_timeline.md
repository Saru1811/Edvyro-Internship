# Incident Timeline – Security Log Investigation

**Project:** EdVyro Task 3  
**Date of Events:** 24 October 2026  
**Data Source:** Synthetic Authentication Logs

## 1. Timeline of Events

| Time | Source IP | Account | Event | Observation |
|---|---|---|---|---|
| 09:00:12 | 192.168.1.45 | user01 | Failed login | Authentication failed |
| 09:00:35 | 192.168.1.45 | user02 | Failed login | Different account targeted |
| 09:00:58 | 192.168.1.45 | user03 | Failed login | Multiple accounts targeted |
| 09:01:20 | 192.168.1.45 | user04 | Failed login | Repeated failures |
| 09:01:45 | 192.168.1.45 | user05 | Failed login | Five accounts attempted |
| 09:05:10–09:06:18 | 203.0.113.50 | admin | 10 failed logins | Repeated attempts against one account |
| 09:10:05 | 192.168.1.45 | user01 | Successful login | Login succeeded |
| 09:12:30 | 198.51.100.25 | admin | Successful login | Administrator login succeeded |
| 09:15:42 | 198.51.100.25 | admin | Successful access | Access event recorded |
| 09:20:10 | 192.168.1.45 | user02 | Failed login | Another failed attempt |
| 09:25:15 | 203.0.113.50 | admin | Failed login | Further failed attempt |
| 09:30:45 | 198.51.100.25 | admin | Successful logout | Session ended |

## 2. Key Observations

### Observation 1 – Possible Password Spraying
IP address `192.168.1.45` attempted logins against five different accounts with failed results within a short period.

### Observation 2 – Possible Brute-Force Activity
IP address `203.0.113.50` generated ten failed login attempts against the `admin` account.

### Observation 3 – Successful Administrator Access
The `admin` account successfully logged in from `198.51.100.25` and performed an access event.

## 3. Investigation Notes

- Multiple failed logins indicate suspicious authentication patterns.
- The successful administrator login requires further verification.
- The available logs do not prove that the administrator account was compromised.
- Source IP ownership and user identity are not established by this dataset.

## 4. Conclusion

The synthetic logs show possible password spraying and brute-force activity, followed by a successful administrator login. Further evidence is required to determine whether unauthorized access occurred.