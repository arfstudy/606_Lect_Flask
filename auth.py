import hashlib

SALT = "325 gdfre#&!jd_gfr~f5j^"


def hash_password(password: str):
    """Хеширование пароля"""
    password = f"{password}{SALT}"
    password = password.encode()
    return str(hashlib.md5(password))
