from english_words import english_words_set
from random import choice

# words = ['tomato', 'cucumber', 'lettuce', 'banana', 'strawberry', 'watermelon', 'grapefruit', 'pineapple', 'apple']
turns = 5
reset = '\033[0m'
blue = '\033[1;34m'
green = '\033[1;32m'
red = '\033[1;31m'

def display(this_list):
    print(' '.join(this_list))
    
def set_color(text, color):
    return f'{color}{text}{reset}'

answer = choice(list(english_words_set))
game_word = list('_' * len(answer))
display(game_word)
    
while turns > 0:

    correct = False
    guess = input('Guess a letter: ')
    if len(guess) > 1:
        print(set_color('Only one letter allowed at a time', red))
        continue

    for index, char in enumerate(answer):
        if guess.lower() == char:
            game_word[index] = set_color(char.upper(), blue)
            correct = True
    
    display(game_word)
    
    if correct:
        print(set_color('Good guess!', green))
        if ''.join(game_word).count('_') == 0:
            print(set_color('You win!', green))
            break
    else:
        turns -= 1
        if turns == 0:
            print(set_color(f'Game over. The word was {answer}.', red))
            break
        else:
            turn_word = 'turn' if turns == 1 else 'turns'
            print(set_color(f'Try again {turns} {turn_word} remaining', red))
    