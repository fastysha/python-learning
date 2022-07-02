# https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958
#   82. Multiple conditions at a single if-statement
#   83. At least one condition is met out of many in a single if-statement

# Программа по поиску телефона который соответствует ВСЕМ критериям. Нужно использовать подход который описан в этой статье.

# Критерии обьявлены мной. Их не менять
min_camera_quality = 24
min_memory_size = 128
max_price = 1_500 # 1_500 тоже самое что и 1500
blacklist_brands = ('sony', 'meizu', 'huawei') # что угодно кроме этих брендов

while True:
    camera_quality = int(input('Enter camera quality... '))
    memory_size = int(input('Enter memory size... '))
    price =int( input('Enter price... '))
    brand = input('Enter brand... ')
    condition=[ camera_quality >= min_camera_quality, min_memory_size <=memory_size, max_price>=price, brand not in blacklist_brands]
    if all(condition):
        print("Buy")
    else:
        print("Don`t buy")
    # пиши свой код тут. Если все критерии совпали, выводим "Покупаем!". Если не совпали пишем "Не покупаем...".

