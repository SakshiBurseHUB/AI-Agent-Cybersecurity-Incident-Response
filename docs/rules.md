# Development Rules

**Project:** AI Agent for Cybersecurity Incident Response

**Version:** 1.0

**Last Updated:** 17 July 2026

---

# 1. Purpose

This document defines the development standards, coding practices, and project guidelines to ensure the project remains consistent, secure, and maintainable.

---

# 2. Coding Standards

* Follow **PEP 8** Python coding standards.
* Write clean, readable, and modular code.
* Keep functions focused on a single responsibility.
* Use meaningful variable, function, and class names.
* Add comments only when necessary to explain complex logic.

---

# 3. Project Structure

* Keep files in their designated folders.
* Do not create duplicate functionality.
* Store configuration files inside the `config/` folder.
* Keep documentation updated in the `docs/` folder.

---

# 4. Git Workflow

* Create a commit after completing each major task or feature.
* Use clear and meaningful commit messages.
* Push changes to GitHub regularly.
* Do not commit temporary or unnecessary files.

**Example Commit Messages**

* Initial project setup
* Complete PRD documentation
* Add system architecture
* Implement log collector
* Add AI threat analysis

---

# 5. Error Handling

* Use `try-except` blocks where appropriate.
* Log errors instead of ignoring them.
* Display user-friendly error messages.
* Avoid application crashes caused by unhandled exceptions.

---

# 6. Logging

Log important events such as:

* Application startup
* Incident detection
* AI analysis
* Errors and exceptions
* Database operations

Never log:

* Passwords
* API keys
* Sensitive user information

---

# 7. Security Rules

* Never hardcode passwords, API keys, or secrets.
* Store sensitive values in environment variables.
* Validate all user inputs.
* Follow secure coding practices.
* Keep dependencies updated.

---

# 8. AI Agent Boundaries

The AI Agent **can**:

* Analyze security incidents.
* Classify threats.
* Predict severity.
* Recommend response actions.
* Generate incident reports.

The AI Agent **must not**:

* Execute destructive system commands.
* Delete files automatically.
* Modify firewall or system settings.
* Take irreversible actions without user approval.

---

# 9. Approved Technologies

**Programming Language**

* Python 3.11+

**Frameworks**

* FastAPI
* Streamlit

**Database**

* SQLite (Development)
* PostgreSQL (Future)

**Libraries**

* Pandas
* NumPy
* Plotly
* SQLAlchemy
* Pytest

---

# 10. Testing Guidelines

* Test new features before committing.
* Fix errors before pushing code.
* Keep the project stable after every update.
* Write reusable and maintainable code.

---

# 11. Documentation Rules

* Update `memory.md` after completing each major milestone.
* Update `architecture.md` if the system design changes.
* Update `PRD.md` if project requirements change.
* Keep documentation clear and concise.

---

# 12. General Guidelines

* Write code that is easy to understand.
* Prefer reusable components over duplicated code.
* Keep the project modular for future expansion.
* Prioritize security, readability, and maintainability.
* Follow the planned project phases and avoid unnecessary scope changes.

---

**End of Document**
