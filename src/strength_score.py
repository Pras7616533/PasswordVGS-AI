def calculate_strength_score(strength, entropy, password, breached):
    score = 0

    # AI strength score
    if strength == "Very Weak":
        score += 5
    elif strength == "Medium":
        score += 25
    else:  # Strong
        score += 40

    # Entropy score
    if entropy < 40:
        score += 5
    elif entropy < 60:
        score += 20
    else:
        score += 30

    # Length score
    length = len(password)
    if length >= 12:
        score += 20
    elif length >= 8:
        score += 10
    else:
        score += 5

    # Breach penalty
    if not breached:
        score += 10

    return min(score, 100)
