import re

def get_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters")

    if not any(c.isupper() for c in password):
        suggestions.append("Add at least one uppercase letter (A-Z)")

    if not any(c.islower() for c in password):
        suggestions.append("Add at least one lowercase letter (a-z)")

    if not any(c.isdigit() for c in password):
        suggestions.append("Add at least one number (0-9)")

    if not re.search(r'[^A-Za-z0-9]', password):
        suggestions.append("Add at least one special character (@, #, $, etc.)")

    if not suggestions:
        suggestions.append("Your password is strong 👍")

    return suggestions
