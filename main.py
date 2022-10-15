import random
import string
print("Welcome to Password Generator")

adjectives = ['wide', 'oval', 'dinky', 'huge', 'little', 'narrow', 'clean', 'spoiled', 'wee', 'glow', 'strange', 'wild', 'cold', 'brutal', 'shy']
nouns = ['cat', 'shoe', 'bevy', 'peace', 'team', 'mountain', 'camping', 'jellyfish', 'knowledge']

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("You Password is : %s" % password)

    response = input("Would you like another password? Type Y or N: ")
    if response == 'N':
        break 