import random

QUESTIONS_COUNT = 10
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

while question_number <= QUESTIONS_COUNT:
    left_num = random.randint(MIN_N, MAX_N)
    right_num = random.randint(MIN_N, MAX_N)
    sign = random.choice(list(sign_dict.keys()))

    print(question_number, ").", left_num, sign, right_num, "=")
    answer = int(input(""))
    
    if sign_dict.get(sign)(left_num, right_num) == answer:
        correct_answers_counter += 1
    
    question_number += 1

print(correct_answers_counter, "correct out of", QUESTIONS_COUNT)
