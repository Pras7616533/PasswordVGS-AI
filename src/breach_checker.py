def is_breached(password):
    try:
        with open("breached_passwords.txt", "r") as file:
            breached = file.read().splitlines()
        return password.lower() in (p.lower() for p in breached)
    except FileNotFoundError:
        return False
