import string
import secrets


def generate_password(length: int) -> str:
    if length <= 0:
        raise ValueError("Şifre uzunluğu 0'dan büyük olmalı")

    characters = string.ascii_letters + string.digits + string.punctuation


    password = [
        secrets.choice(string.ascii_letters),
        secrets.choice(string.digits),
    ]

    password += [secrets.choice(characters) for _ in range(length - 2)]

    secrets.SystemRandom().shuffle(password)
    return "".join(password)
