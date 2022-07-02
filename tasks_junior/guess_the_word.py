import random
words = ['hello', 'cat', 'camel', 'cookie', 'cooler', 'cool', 'queue', 'quote']
secret_word = random.choice(words)
n=1
print("Guess my word!")
print("What is letter number: "+str(n))
right_letters=[]

print(secret_word)
for letter in secret_word:
    i=input("leter:")
    while(letter!=i):
        if letter!=i:
            print("No")
            i=input("leter:")    
    else:
        right_letters.append(i)
        print("Right [",("".join(right_letters)),"]")
        n=n+1
        print("What is letter number: ",n)

print("You are the winner! The word is:","".join(right_letters))
    


# Program chooses the random word from 'words' array
# As a user you should guess this word

# Example of programm interface. Let's say programm guessed the word 'camel'
# P: Programm
# U: User

# P: Guess my word! 
# P: What is letter number: 1?
# U: s
# P: No
# U: h
# P: No
# U: c
# P: Right! [c]
# P: What is letter number: 2?
# U: a
# P: Right! [ca]
# P: What is letter number: 3?
# U: t
# P: No
# U: m
# P: Right! [cam]
# P: What is letter number: 4?
# U: e
# P: Right! [came]
# P: What is letter number: 5?
# U: l
# P: Right! [camel]
# You are the winner! The word is: [camel]