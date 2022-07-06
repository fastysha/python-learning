import json
from typing import List

from mg_models import Student

FILE_PATH = "games/math-game/student_data.json"

# Returns all students
def get_all_students() -> List[Student]:
    with open(FILE_PATH, "r") as file:
        students_json = file.read()
    students_dict_list = list(json.loads(students_json))
    return [__dict_to_obj(ds, lambda s: Student(**s)) for ds in students_dict_list]

def save_student(student: Student):
    student_json_data = ''
    with open(FILE_PATH, "r") as file:
        file_content = file.read()
        student_json_data = file_content if file_content else '[]'

    student_list = list(json.loads(student_json_data))
    student_list.append(student.__dict__)

    with open(FILE_PATH, "w") as file:
        file.write(json.dumps(student_list))

# Converts Dictionary to Class
def __dict_to_obj(dict_value, mapper):
    json_value = json.dumps(dict_value)
    return json.loads(json_value, object_hook=mapper)