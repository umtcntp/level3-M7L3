import string
import pytest
from password.new_password import generate_password


def test_password_characters():
    """Şifre sadece geçerli karakterler içerir"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)

    for char in password:
        assert char in valid_characters


def test_password_length():
    """Şifre istenen uzunlukta olmalı"""
    length = 32
    password = generate_password(length)
    assert len(password) == length


def test_passwords_are_different():
    """Arka arkaya üretilen şifreler farklı olmalı"""
    password1 = generate_password(32)
    password2 = generate_password(32)
    assert password1 != password2


def test_password_is_not_empty():
    """Şifre boş string olmamalı"""
    password = generate_password(16)
    assert password != ""


def test_password_contains_letter_and_digit():
    """Şifre en az 1 harf ve 1 rakam içermeli"""
    password = generate_password(32)

    assert any(char.isalpha() for char in password)
    assert any(char.isdigit() for char in password)


def test_invalid_length_raises_error():
    """Geçersiz uzunlukta hata fırlatılmalı"""
    with pytest.raises(ValueError):
        generate_password(0)
