# Отсортировать лист от большего к меньшему и от меньшего к большему
numbers = [1,4,7,4,3,8,0,1,-2,5,9,1]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# посмотри метод sort()


# Отсортировать рабочих по зарплате, от большего к меньшему
def sort(employe):
    return employe ["salary"]
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
employees.sort(key=sort,reverse=True)
print(employees)