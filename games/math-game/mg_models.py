import uuid
class Student:
    def __init__(self, name, surname, class_number, grade, time, correct_answers, questions_count, id=str(uuid.uuid4()),) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.class_number = class_number
        self.grade = grade
        self.time = time
        self.correct_answers = correct_answers
        self.questions_count = questions_count