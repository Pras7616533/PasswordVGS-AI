import math
import string

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def entropy_level(entropy):
    if entropy < 40:
        return "Low ❌"
    elif entropy < 60:
        return "Medium ⚠️"
    else:
        return "High ✅"
