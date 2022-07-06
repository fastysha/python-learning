import json 
from mg_models import Student

FILE_PATH = "games/math-game/student_data.json"

def save_student(student: Student):
    student_json_data = ''
    with open(FILE_PATH, "r") as file:
        file_content = file.read()
        student_json_data = file_content if file_content else '[]'

    student_list = list(json.loads(student_json_data))
    student_list.append(student.__dict__)

    with open(FILE_PATH, "w") as file:
        file.write(json.dumps(student_list))
