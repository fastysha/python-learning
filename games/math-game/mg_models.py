class Student:
    def __init__(self, name, surname, cn, grade, ts, ca, qc) -> None:
        self.name = name
        self.surname = surname
        self.class_number = cn
        self.grade = grade
        self.time = ts
        self.correct_answers = ca
        self.questions_count = qc