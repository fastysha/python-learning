# Отсортировать лист от большего к меньшему и от меньшего к большему
import unittest

numbers = [1,4,7,4,3,8,0,1,-2,5,9,1]

class TestStringMethods(unittest.TestCase):

    def test_numbers_sort(self):
       numbers = [1,4,7,4,3,8,0,1,-2,5,9,1]
       numbers.sort()
       expected_result = [-2,0,1,1,1,3,4,4,5,7,8,9]
       self.assertListEqual(expected_result, numbers)

    def test_reverse_numbers_sort(self):
        numbers = [-1,2,4,-2,6]
        numbers.sort(reverse=True)
        self.assertListEqual([6, 4, 2, -1, -2], numbers)

if __name__ == '__main__':
    unittest.main()


# посмотри метод sort()


# Отсортировать рабочих по зарплате, от большего к меньшему
# def sort(employe):
#     return employe ["salary"]
# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]
# employees.sort(key=sort,reverse=True)
# print(employees)