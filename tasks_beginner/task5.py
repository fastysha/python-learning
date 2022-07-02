# def my_function(x):
#     print(x*x)
# my_function(int(input("Number")))

# Квадратый корень числа
# from unicodedata import name


# number = int(input("number"))


# def my_function(num):
#     return num*num


# print(my_function(number))

# Факториал

# радик настя оля таня
# Имя: Радик
# Имя: Настя...
# user_input = input("Names:")
# names = user_input.split(" ")

# def print_names(names):
#     for name in names:
#         print("Имя: "+name)

# print_names(names)

# 
# def sum_arguments(*numbers):
#     sum=0 
#     for number in numbers:
#         sum+=number
#     return sum
# print(sum_arguments(1,2,3))
# print(sum_arguments(1,2))
# print(sum_arguments(1))
# print(sum_arguments())


# def avg_arguments(*numbers):
#     if len(numbers)==0:
#         return 0
#     sum=0 
#     for number in numbers:
#         sum+=number
#     return sum/len(numbers)
# print(avg_arguments(1,2,3))
# print(avg_arguments(1,2))
# print(avg_arguments(1))
# print(avg_arguments())


def max(*numbers):
    if len(numbers)==0:
        return 0
    min=numbers[0]
    for element in numbers:
        if element<min:
            min=element
    return min

        

print(max(-9,-7,-3,-5,-2))
print(max(1,2))
print(max(1))
print(max())