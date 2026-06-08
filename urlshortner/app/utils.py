import secrets
import string

chars = string.ascii_letters + string.digits

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(
        secrets.choice(chars)
        for _ in range(length)
    )