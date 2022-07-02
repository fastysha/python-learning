# Implement function that returns:
# count of numbers
# sum of numbers
# max number of numbers

# Use python math functions
# python function can return more than 1 value

def getLenSumMax(*ints):
    return len(ints),sum(ints),max(ints)
     
# len,sum,max=getLenSumMax(4,5,2,3,7)

# print(len, sum, max) # 5 21 7
####################################

# Init list of numbers from 0 to 5 and print it
# Do it in one line. You can use Google
my_list_of_numbers = [i for i in range(11) if i%2==0]
# numbers= range(6)
# for number in numbers:
    # my_list_of_numbers.append(number)
print(my_list_of_numbers) # [0, 1, 2, 3, 4, 5]


####################################

# Implement function that makes list immutable (read-only)
def make_immutable(list):
    return tuple(list)

my_list = [1,2,3]
print('Init list:', my_list)

# change first element
my_list[0] = 4
print('First element changed:', my_list)

immutable_my_list = make_immutable(my_list)
# change first element again, should throw an error
print('Immutable:', immutable_my_list)
# immutable_my_list[0] = 1


###########################
 