import names 
import random

from mg_grade import get_grade
from mg_models import Student
from mg_grade import get_grade
from mg_storage import save_student
from uuid import uuid4

GENERATE_COUNT = 100
QUESTIONS_COUNT = 20

SCRIPT_ENABLED = False

# Create Random Users
for index in range(GENERATE_COUNT):
    if not SCRIPT_ENABLED:
        break

    random_correct_answers = random.randint(7, QUESTIONS_COUNT)

    student = Student(
        str(uuid4()),
        names.get_first_name(),
        names.get_last_name(),
        str(random.randint(5,11)), # any class from 5 to 11
        get_grade(QUESTIONS_COUNT, random_correct_answers),
        random.randint(20,80),
        random_correct_answers,
        QUESTIONS_COUNT
    )

    save_student(student)
