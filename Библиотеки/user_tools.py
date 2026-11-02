import random
import string


# Проверка логина
def check_login(login):
    if len(login) >= 3 and len(login) <= 20:
        return True
    else:
        return False


# Проверка пароля
def check_password(password):
    if len(password) >= 8:
        return True
    else:
        return False


# Проверка электронной почты
def check_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False


# Генерация пароля
def generate_password():
    symbols = string.ascii_letters + string.digits
    password = ""

    for i in range(8):
        password += random.choice(symbols)

    return password


# Генерация ID пользователя
def generate_id():
    return random.randint(1000, 9999)
