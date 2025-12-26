import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test eder"""
    password_length = 13
    password = generate_password(password_length)
    assert len(password) == password_length

def test_password_uniqueness():
    """Arka arkada oluşturulan iki şifrenin farklı olup olmadığını test eder"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin 
 
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""
def test_password_length():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    password_length = 12
    password = generate_password(password_length)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    assert len(password) == password_length

def test_password_uniqueness():
    """Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test eder"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2
