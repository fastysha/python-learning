from datetime import datetime

from mg_storage import save_student
from mg_models import Student
from mg_grade import get_grade
from mg_example_generator import print_example_and_get_result

QUESTIONS_COUNT = 20

def istruenumeric(val: str) -> bool:
    return val.isnumeric() or (val and val[0] == '-' and val[1::].isnumeric())

print("Hi!! It is math game.You must solve 20 math examples! Good Luck ,guy!")

name = input("Your name: ")
surname = input("Your surname: ")
class_num = input("Your class number: ")

student = Student(name, surname, class_num, '', 0, 0, QUESTIONS_COUNT)

question_number = 1
correct_answers_counter = 0

start = datetime.now()
while question_number <= QUESTIONS_COUNT:

    example_result = print_example_and_get_result(question_number)

    user_answer = input("")
    while not (istruenumeric(user_answer)):
        user_answer = input("")
    user_answer = int(user_answer)

    if example_result == user_answer:
        correct_answers_counter += 1

    question_number += 1
# while end
time_spent = (datetime.now() - start).seconds

grade = get_grade(total=QUESTIONS_COUNT, actual=correct_answers_counter)

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

save_student(student)