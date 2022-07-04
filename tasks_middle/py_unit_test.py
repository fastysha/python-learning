# Написать тесты на 'list_map.py' and 'list_sort.py' модули

# Ознакомиться с Py Unit в Google. 
# https://pythonworld.ru/moduli/modul-unittest.html


##############################
# Пример теста от меня:

# Импортируем тестовый модуль
from email import message
import unittest

# Будем тестировать эту функцию
def div(a, b):
    if (b == 0):
        raise ValueError('Can not divide on zero')
    return a / b 

# Cоздаем тестовый класс и наследуемся от соответствующего класса
class TestDivFunction(unittest.TestCase):

    # эта функция будет тестировать самый простой кейс деления чисел друг на друга
    def test_div_positive_numbers(self):
        # вызываю функцию и сохраняю результат
        actual_res = div(10,5)
        # ожидаю что 10 поделить на 5 даст результат 2
        expected_res = 2
        # вызываю функцию которая предоставляется модулем, что бы сравнить actual и expected результаты
        self.assertEqual(expected_res, actual_res)

    def test_div_negative_numbers(self):
        # можно сделать все тоже самое но без переменных
        # слева пишу ожидаемый результат
        # справа пишем вызов метода, актуальный результат
        self.assertEqual(2, div(-4, -2))

    def test_div_divide_on_zero(self):
        # проверяем что будет выбрашена ошибка если делим на ноль
        with self.assertRaises(ValueError):
            div(1,0)

    def test_div_divide_on_negative(self):
        # тест который проверяет что если мы делим позитивное число на негативное, 
        # то мы всегда получим результат меньше нуля
        negative_number = self.get_random_negative_number()
        # Добавь сама этот тест используя assertLess
        actual_result=div(8,negative_number)
      
        self.assertLess(actual_result, 0)
    

    # эта функция ничего не тестирует, а просто служит как вспомогательная
    def get_random_negative_number(self):
        import random
        return random.randint(-100, -1)

# Запускаем все тесты
unittest.main()