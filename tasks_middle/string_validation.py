# Исследуем методы строки

# isnumeric() - являются ли все символы числами
# isalpha() - является ли все символы буквами


# Написать программу которая спрашивает имя и возраст человека
# Если человек ввел цифры в имени, пишем предупреждение
# Если человек ввел буквы в возрасте, пишем предупреждение
# Если данные правильные, пишем что все хорошо

name = input('Enter your name... ')
age = input('Enter your age... ')
if age.isnumeric() and name.isalpha():
    print("It is good")
else:print("invalid symbol")
# пишем код тут