from tkinter import Y


country=["USA","Ukraine","France","Germany","China","USA","Belgium"]
length=len(country)
print(length)

first_country=country[0]
print(first_country)

last_country=country[-1]
print(last_country)

USA=country.count("USA")
print(USA)

index=country.index("Ukraine")
print(index)

y=country.copy()
y.sort()
print(y)

x=country.copy()
x.reverse()
print(x)

country.append("Sweden")
print(country)

country.pop(3)
print(country)

country.remove("China")
print(country)

# country.clear()
# print(len(country))

country[2]= "Poland"
print(country)

country.insert(3 , "England")
print(country)