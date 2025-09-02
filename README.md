# 🔒 Secure CI/CD Pipeline

A reference implementation of a **security-hardened CI/CD pipeline** designed to catch vulnerabilities early, enforce compliance, and build resilient software delivery practices.  

This project demonstrates how to integrate **DevSecOps best practices** into a modern GitHub Actions workflow, featuring tools for static analysis, dependency auditing, secrets detection, and semantic code analysis.  

---

## 🚀 Features

- **Static Analysis**: Python code scanning with [Bandit](https://github.com/PyCQA/bandit).  
- **Secrets Detection**: [Gitleaks](https://github.com/gitleaks/gitleaks) integration to prevent committing credentials.  
- **Dependency Security**: Vulnerability detection via [pip-audit](https://pypi.org/project/pip-audit/).  
- **CodeQL**: Semantic code analysis for advanced security checks.  
- **SARIF Reporting**: Upload results directly to GitHub’s Code Scanning Alerts for visibility.  
- **Fail-Fast Security Gates**: Block merges on critical findings.  

---

## 📂 Repository Structure
```
secure-ci-pipeline/
├── .github/workflows/ # GitHub Actions workflows
├── src/ # Example Python app
├── requirements.txt # App dependencies
├── bandit.sarif # Sample scan output
└── README.md # You are here
```
---

## ⚙️ Workflows

| Workflow          | Purpose                                      |
|-------------------|----------------------------------------------|
| `bandit.yml`      | Run Bandit for Python SAST.                  |
| `gitleaks.yml`    | Scan repo for hardcoded secrets.             |
| `codeql.yml`      | Perform semantic security analysis.          |

Each workflow is designed to run **on pull requests** and **main branch pushes**, enforcing a security-first development cycle.  

---

## 🛡️ Why This Matters

Modern attackers automate, so defenders must too. This pipeline:  
- Shifts security **left**, catching issues before they hit production.  
- Protects against **secrets exposure** and **supply-chain attacks**.  
- Ensures compliance with **OWASP Top 10**, **PCI-DSS**, and other standards.  
- Reduces friction for developers by embedding checks into CI.  

---

## 🧑‍💻 Author

**Steven Horton**  
Security Engineer | Red Teaming | DevSecOps | Cloud Security  

- 💼 [LinkedIn](https://www.linkedin.com/in/steven-horton-66325520)  
- 🐙 [GitHub](https://github.com/shortontech)  

---

## 📜 License

MIT License – if you feel like this is useful, go ahead and use it.