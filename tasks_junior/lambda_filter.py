from posixpath import split


def filter_and_print(arr: list[str], filter: lambda:bool):
    print([element for element in arr if filter(element)])


fruits = ['apple', 'raspberry', 'strawberry', 'banana', 'mango', 'peach', 'cherry', 'pear', 'papaya']

# Filter the following array of fruits using python lambda

# all fruits with first letter 'p' => [peach pear papaya]
filter_and_print(fruits,lambda fruit : fruit[0]=="p")
# all fruits with word lenght 5 => [apple mango peach]
filter_and_print(fruits,lambda fruit : len(fruit)==5)
# all fruits ended with 'berry' => [raspberry strawberry]
x=lambda a:str(a)
print(type(x(4)))