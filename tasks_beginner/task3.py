a =str(input("Введите слово:"))
print(a[0])
print(a[len(a)-1])
print(len(a))

str=str("hello,i,am,radik,22,years,old")
print(str[0])
print(str[len(str)-1])
print(len(str))

list = str.split(',')

print(list)

print(len(list))
str = str(input("Слово:"))
b = str(input("Буква:"))
counter=0

for c in a:
    if c==b:
        counter=counter + 1

print(counter)

  