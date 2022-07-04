import random
print("Hi!! It is math game.You must solve 20 math examples! Good Luck ,guy!")
n=1
count=0
while n <= 20:
    left_num=random.randint(1,10)
    right_num=random.randint(1,10)
    print(n,").",left_num,"+",right_num,"=")
    answer=int(input(""))
    n+=1
    if left_num+right_num==answer:
        count+=1
print(count,"correct out of 20")
