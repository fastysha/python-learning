from sm_dbconnector import create_parcel, find_user_by_phone_number
from sm_dbconnector import create_user
from sm_dbconnector import create_parcel
from sm_data_models import ParcelStatus,User

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

    new_user = User(0, name, surname, phone_number, country)

    create_user(new_user)
else:
    while True:
        print('Привет,', current_user.full_name())
        print("Выберите действие: 1-Мои посылки,2-Отправить посылку")
        choice = int(input())
        if choice == 1:
            pass
        elif choice == 2:
            phone_num_des = input("Номер телефона получателя: ")
            consumer = find_user_by_phone_number(phone_num_des)
            if consumer is None:
                print("Пользователь не найден в системе")
            else:
                print(f"Посылка поедет к: {consumer.full_name()}")
                name_parcel = input("Название посылки: ")
                price = input("Оценочная стоимость: ")
                post_num = input("Номер отделения: ")
                new_parcel = {
                    "name": name_parcel,
                    "phone": phone_num_des,
                    "price": price,
                    "post_num": post_num,
                    "sender_id":current_user.id,
                    "consumer_id":consumer.id,
                    "status":ParcelStatus.IN_PROGRESS.name
                }
                create_parcel(new_parcel)
