
my_word = list('banana')
list_new = ["_" for el in my_word]

while True:
    print(" ".join(list_new))
    letter = input(" ")
    positions = [index for index, val in enumerate(my_word) if val == letter]

    if len(positions) == 0:
        print("не угадал")
    else:
        for p in positions:
            list_new[p] = letter

    if my_word == list_new:
        print("Победа")
        print(" ".join(list_new))
        break