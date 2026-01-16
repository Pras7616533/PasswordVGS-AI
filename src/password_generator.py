import secrets
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

# Test
if __name__ == "__main__":
    print("Generated Password:", generate_password())
