a = int(input("цифра:"))

# while
i = 1
while i < 21:
    if i == a:
        break
    i += 1
    if i % 2 == 0:
        print(i)
# for

for x in range(1, 21):
    if x % 2 == 0:
        print(x)
    if x == a:
        break
else:
    print('we are done!')
