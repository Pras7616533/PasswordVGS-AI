import re

COMMON_PATTERNS = ["123", "abc", "qwerty", "password", "admin"]

def extract_features(password):
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    lowercase = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special = len(re.findall(r'[^A-Za-z0-9]', password))

    repeated = 1 if re.search(r'(.)\1', password) else 0
    sequence = 1 if any(pat in password.lower() for pat in COMMON_PATTERNS) else 0

    return [
        length,
        uppercase,
        lowercase,
        digits,
        special,
        repeated,
        sequence
    ]

# Test
if __name__ == "__main__":
    print(extract_features("Prashant@2024"))
