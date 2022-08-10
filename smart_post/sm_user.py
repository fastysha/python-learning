from secrets import choice
from sm_dbconnector import find_user_by_phone_number
from sm_dbconnector import create_user
print("Привет это Smart Post")

user_phone_number=input("Введите свой номер: ")

user = find_user_by_phone_number(user_phone_number)

if user is None:
    print('Такого пользователя не существует.Зарегистрируйтесь!')
    name=input("Введите имя: ")
    surname=input("Введите фамилию: ")
    phone_number=input("Номер телефона:")
    country=input("Ваша страна: ")

    new_user={
        "name": name,
        "surname":surname,
        "phone_num":phone_number,
        "country":country
        }

    create_user(new_user)
else:
    print('Привет,', user["UserName"], user["UserSurname"])
    print("Выберите действие: 1-Мои посылки,2-Отправить посылку")
    choice=int(input())


