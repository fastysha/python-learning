import random

QUESTIONS_COUNT = 20
MIN_N = 1
MAX_N = 10

print("Hi!! It is math game.You must solve 20 math examples! Good Luck ,guy!")
question_number = 1
correct_answers_counter = 0

sign_dict = {
    "-": lambda a, b: a-b,
    "+": lambda a, b: a+b,
    "*": lambda a, b: a*b
}

grade_dict={
    range(90,101):"A",
    range(80,90):"B",
    range(75,80):"C",
    range(65,75):"D",
    range(60,65):"E",
    range(0,60):"F"
}

while question_number <= QUESTIONS_COUNT:
    left_num = random.randint(MIN_N, MAX_N)
    right_num = random.randint(MIN_N, MAX_N)
    sign = random.choice(list(sign_dict.keys()))

    print(question_number, ").", left_num, sign, right_num, "=")
    answer = int(input(""))
    
    if sign_dict.get(sign)(left_num, right_num) == answer:
        correct_answers_counter += 1
    
    question_number += 1

percent_num=(correct_answers_counter*100)/QUESTIONS_COUNT

grade = ''
for range_key in grade_dict.keys():
    if percent_num in range_key:
        grade = grade_dict[range_key]
        break

print(correct_answers_counter, "correct out of", QUESTIONS_COUNT, ". Grade:", grade)
