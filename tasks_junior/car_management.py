count_cars = int(input("Количество:"))
cars_mark = []
text_format = "Марка машины {}:"

for count in range(count_cars):
    mark = input(text_format.format(count+1))
    cars_mark.append(mark)

print(cars_mark)

# ---
choice = -1

while(choice != 0):
    choice = int(input("""Выберите действие:
1 = добавить машину
2 = удалить машину
0 = выйти с програмы: """))

    if (choice == 1):
        mark = input(text_format.format(len(cars_mark) + 1))
        cars_mark.append(mark)
    elif (choice == 2):
        mark = input('Напишите машину для удаления: ')
        cars_mark.remove(mark)
    else:
        print('Неверное действие')
    print(cars_mark)
else:
    print('Пока пока!')