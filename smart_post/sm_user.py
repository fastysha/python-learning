from ast import While
from secrets import choice
from sm_dbconnector import create_parcel, find_user_by_phone_number
from sm_dbconnector import create_user
from sm_dbconnector import create_parcel
from sm_data_models import ParcelStatus

####################################################################
print("Привет это Smart Post")

user_phone_number = input("Введите свой номер: ")

current_user = find_user_by_phone_number(user_phone_number)

if current_user is None:
    print('Такого пользователя не существует.Зарегистрируйтесь!')
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone_number = input("Номер телефона:")
    country = input("Ваша страна: ")

    new_user = {
        "name": name,
        "surname": surname,
        "phone_num": phone_number,
        "country": country
    }

    create_user(new_user)
else:
    while True:
        print('Привет,', current_user["UserName"], current_user["UserSurname"])
        print("Выберите действие: 1-Мои посылки,2-Отправить посылку")
        choice = int(input())
        if choice == 1:
            
        elif choice == 2:
            phone_num_des = input("Номер телефона получателя: ")
            consumer = find_user_by_phone_number(phone_num_des)
            if consumer is None:
                print("Пользователь не найден в системе")
            else:
                print(f"Посылка поедет к: {consumer['UserName']} {consumer['UserSurname']}")
                name_parcel = input("Название посылки: ")
                price = input("Оценочная стоимость: ")
                post_num = input("Номер отделения: ")
                new_parcel = {
                    "name": name_parcel,
                    "phone": phone_num_des,
                    "price": price,
                    "post_num": post_num,
                    "sender_id":current_user["UserID"],
                    "consumer_id":consumer["UserID"],
                    "status":ParcelStatus.IN_PROGRESS.name
                }
                create_parcel(new_parcel)
