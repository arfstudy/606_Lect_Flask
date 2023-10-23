import hashlib

SALT = "325 gdfre#&!jd_gfr~f5j^"


def hash_password(password: str):
    """Хеширование пароля"""
    password = f"{password}{SALT}"    # "Посолим"
    password = password.encode()      # Переводим пароль из строчки в байты.
    return str(hashlib.md5(password))
