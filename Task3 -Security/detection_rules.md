# Detection Rules – Security Log Investigation

**Project:** EdVyro Task 3  
**Category:** Cyber Security – Log Analysis

## 1. Password Spraying Detection

**Meaning:** An attacker tries a common password against multiple user accounts.

**Detection Rule:**
- Monitor login failures from the same source IP.
- Identify attempts against multiple different accounts.
- Flag repeated failures within a short time window.

**Evidence to check:**
- Source IP address
- Number of unique accounts
- Failed login count
- Timestamp pattern

## 2. Brute-Force Attack Detection

**Meaning:** Repeated password attempts against one account.

**Detection Rule:**
- Monitor repeated failed logins for the same account.
- Identify multiple failures within a short time period.
- Flag accounts with unusually high failure counts.

**Evidence to check:**
- Username
- Source IP
- Failed login count
- Time interval between attempts

## 3. Unusual Successful Access Detection

**Meaning:** A successful login that appears unusual based on the available log data.

**Detection Rule:**
- Identify successful logins from source IPs associated with repeated failures.
- Check administrator account access.
- Review successful login time and subsequent access events.

**Evidence to check:**
- Account name
- Source IP address
- Login result
- Access activity
- Timestamp

## 4. Investigation Limitations

- The supplied authentication logs are synthetic test data.
- IP addresses alone do not prove an attacker's identity.
- A successful login does not independently prove account compromise.
- Detection alerts require further investigation and context.

## 5. Conclusion

These rules help identify possible password spraying, brute-force attempts, and unusual successful access in authentication logs. Findings must be verified using supporting evidence.