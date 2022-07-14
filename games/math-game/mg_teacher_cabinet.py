# TODO Write our code here!
from mg_models import Student
from mg_storage import get_all_students
from prettytable import PrettyTable
from itertools import groupby

def group_by(arr, grouper):
    arr.sort(key=grouper)
    return {grade_key: len((list(students))) for grade_key, students in groupby(arr, key=grouper)}

print("""1-List students
2-Rating
3-Student Statistics
4-
""")
teacher_choice=int(input(""))

list_students=get_all_students()
if teacher_choice==1:
    list_students.sort(key=lambda s : (s.name, s.surname))
elif teacher_choice==2:
    rating=list_students.sort(key=lambda s: (s.grade, -s.correct_answers, s.time))
elif teacher_choice==3:
    grouped = group_by(list_students, lambda s : s.grade)
    # TODO Move to module
    print(grouped)

table = PrettyTable(['#', 'Full Name', 'Class', 'Grade', 'C/T', 'Time'])

for index in range(len(list_students)):
    student = list_students[index]
    full_name = student.name + ' ' + student.surname
    corr_to_total = "{}/{}".format(student.correct_answers, student.questions_count)

    table.add_row([index + 1, full_name, student.class_number, student.grade, corr_to_total, student.time])

print(table)