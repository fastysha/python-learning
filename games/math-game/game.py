from genericpath import exists
import random
from datetime import datetime
import json

QUESTIONS_COUNT = 20
MIN_N = 0
MAX_N = 10

def istruenumeric(val: str) -> bool:
    return val.isnumeric() or (val and val[0] == '-' and val[1::].isnumeric())

FILE_PATH = "games/math-game/student_data.json"

sign_dict = {
    "-": lambda a, b: a-b,
    "+": lambda a, b: a+b,
    "*": lambda a, b: a*b
}

grade_dict = {
    range(90, 101): "A",
    range(80, 90): "B",
    range(75, 80): "C",
    range(65, 75): "D",
    range(60, 65): "E",
    range(0, 60): "F"
}

print("Hi!! It is math game.You must solve 20 math examples! Good Luck ,guy!")

name = input("Your name: ")
surname = input("Your surname: ")
class_num = input("Your class number: ")


class Student:
    def __init__(self, name, surname, cn, grade, ts, ca, qc) -> None:
        self.name = name
        self.surname = surname
        self.class_number = cn
        self.grade = grade
        self.time = ts
        self.correct_answers = ca
        self.questions_count = qc

student = Student(name, surname, class_num, '', 0, 0, QUESTIONS_COUNT)

question_number = 1
correct_answers_counter = 0

start = datetime.now()
while question_number <= QUESTIONS_COUNT:
    left_num = random.randint(MIN_N, MAX_N)
    right_num = random.randint(MIN_N, MAX_N)
    sign = random.choice(list(sign_dict.keys()))

    print(question_number, ")", left_num, sign, right_num, "=", end=" ")
    answer = input("")
    while not (istruenumeric(answer)):
        answer = input("")
    answer = int(answer)

    if sign_dict.get(sign)(left_num, right_num) == answer:
        correct_answers_counter += 1

    question_number += 1
# while end
time_spent = (datetime.now() - start).seconds

correct_answers_percentage = (correct_answers_counter * 100) // QUESTIONS_COUNT

grade = ''
for grade_range_key in grade_dict.keys():
    if correct_answers_percentage in grade_range_key:
        grade = grade_dict[grade_range_key]
        break

print("""
{} correct answers out of {}.
Time spent: {} seconds.
Grade: [{}]
"""
      .format(correct_answers_counter,
              QUESTIONS_COUNT,
              time_spent,
              grade)
      )

student.grade = grade
student.correct_answers = correct_answers_counter
student.time = time_spent

student_json_data = ''
with open(FILE_PATH, "r") as file:
    file_content = file.read()
    student_json_data = file_content if file_content else '[]'

student_list = list(json.loads(student_json_data))
student_list.append(student.__dict__)

with open(FILE_PATH, "w") as file:
    file.write(json.dumps(student_list))
