# Написать функцию которая возвращает лист с приобразованными значениями
import unittest
class TestStringMethods(unittest.TestCase):
    def map(list, converter) -> list:
        return [converter(el) for el in list]

################################################### 
# Это трогать не нужно! Пишем только в теле функции
list = ['hello', 'i', 'am', 'fastysha']

upper_list = map(list, lambda s : s.upper())
# ['HELLO', 'I', 'AM', 'FASTYSHA']
print(upper_list)

capitalize_list = map(list, lambda s : s.capitalize())
# ['Hello', 'I', 'Am', 'Fastysha']
print(capitalize_list)

reversed_list = map(list, lambda s : s[::-1])
# ['olleh', 'i', 'ma', 'ahsytsaf']
print(reversed_list)