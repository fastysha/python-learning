# https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958
# 16. Print multiple elements in the same line

# вывести все четные числа в одну строку, разделитель пробел.
for num in range(50):
    if not num % 2:
        num=str(num)
        print (num, end=" ")

# Ожидаемый результат
# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48