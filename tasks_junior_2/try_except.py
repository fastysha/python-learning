# Create a programm. Programm asks user for a number and multiplies it by 10

import sys

while (True):
    try:
        number = input("write your number: ") # type = str
        
        if(number == 'хуй'):
            raise NameError('Обзывательство!')

        number = int(number)
    except ValueError:    
        print("Only int value is allowed .Will use default: [1]")
        number = 1
    except NameError:
        print('Программа прерывается... введено плохое слово!')
        sys.exit()
    else:
        print("Your value is correct")
    finally:
        our_num = 10 * number
        print("Operation completed. Result:", our_num)

# If user input is integer, then print message to console 'Your value is correct!'
# If user input is not an integer value (str for example), then print message to console 'Only int value is allowed. Will use default: [1]'
# At the end, programm prints: 'Operation completed. Result: '

# Use: try, except, else, finally 
MULTIPLIER = 10

# 10  => str
# desat => str