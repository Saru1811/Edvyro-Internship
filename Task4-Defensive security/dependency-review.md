# Dependency Review

## 1. Project
Defensive Security Assessment – Secure Authentication Application

## 2. Objective
To review the third-party Python packages used by the application and identify outdated or vulnerable dependencies.

## 3. Tools Used
- Python
- pip
- requirements.txt
- Terminal / Command Prompt

## 4. Dependency Review Checklist

| Test ID | Review Activity | Expected Result | Status |
|---|---|---|---|
| DR01 | Check installed Python packages | Package list should be available | Pending |
| DR02 | Review requirements.txt | Required dependencies should be listed | Pending |
| DR03 | Check outdated packages | Outdated packages should be identified | Pending |
| DR04 | Check known package vulnerabilities | No known unresolved vulnerabilities | Pending |
| DR05 | Remove unused dependencies | Only necessary packages should remain | Pending |

## 5. Review Commands

Display installed packages:

`pip list`

Check outdated packages:

`pip list --outdated`

Display dependency details:

`pip show Flask`

## 6. Security Recommendations

- Use trusted Python packages.
- Keep dependencies updated.
- Remove unused libraries.
- Avoid installing packages from unknown sources.
- Review security advisories before updating dependencies.
- Maintain a requirements.txt file.

## 7. Review Results

Review status: Pending.

Record the actual package versions and findings after performing the review.

## 8. Conclusion

Dependency review helps identify outdated or potentially vulnerable third-party packages and improves the security of the application.

**Note:** These commands are for reviewing the local project environment. No vulnerability scan has been confirmed yet.
