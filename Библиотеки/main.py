from user_tools import *

print("Библиотека для работы с пользователями")

login = "student123"
password = "12345678"
email = "student@gmail.com"

print("\nПроверка логина:")
print(check_login(login))

print("\nПроверка пароля:")
print(check_password(password))

print("\nПроверка почты:")
print(check_email(email))

print("\nНовый пароль:")
print(generate_password())

print("\nID пользователя:")
print(generate_id())
