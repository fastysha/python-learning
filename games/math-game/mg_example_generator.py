from cgitb import reset
import random

MIN_N = 0
MAX_N = 10

SIGN_DICT = {
    "-": lambda a, b: a-b,
    "+": lambda a, b: a+b,
    "*": lambda a, b: a*b
}
def print_example_and_get_result(question_number) -> int:
        left_num = random.randint(MIN_N, MAX_N)
        right_num = random.randint(MIN_N, MAX_N)
        sign_key = random.choice(list(SIGN_DICT.keys()))

        print(question_number, ")", left_num, sign_key, right_num, "=", end=" ")
        operation = SIGN_DICT[sign_key]
        return operation(left_num, right_num)

    
 
