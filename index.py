from english_words import english_words_lower_alpha_set
from random import choice

turns = 6
max_turns = turns
reset = '\033[0m'
blue = '\033[1;34m'
green = '\033[1;32m'
red = '\033[1;31m'

def display(this_list):
    print(' '.join(this_list))
    
def set_color(text, color):
    return f'{color}{text}{reset}'

def show_board():
    print(hangman[max_turns-turns])
    display(game_word)

hangman = ["""
    |
   _|_
  (o O)
   \\0/
  --|--
    |
   / \\
""", 
"""
    |
   _|_
  (o O)
   \\0/
    |--
    |
   / \\
""", 
"""
    |
   _|_
  (o O)
   \\0/
    |--
    |
     \\
     
""", 
"""
    |
   _|_
  (o O)
   \\0/
    |--
    |
     
""", 
"""
    |
   _|_
  (o O)
   \\0/
    |
    |
     
""", 
"""
    |
   _|_
  (o O)
   \\0/
     
""", 
"""
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
"""]


answer = choice(list(english_words_lower_alpha_set))
game_word = list('_' * len(answer))
show_board()
    
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
    
    if correct:
        show_board()
        if game_word.count('_') == 0:
            print(set_color('You win!', green))
            break
        else:
            print(set_color('Good guess!', green))
    else:
        turns -= 1
        if turns == 0:
            for index, char in enumerate(answer):
                if game_word[index] == '_':
                    game_word[index] = set_color(char.upper(), red)
            show_board()
            break
        else:
            show_board()
            turn_word = 'turn' if turns == 1 else 'turns'
            print(set_color(f'Try again {turns} {turn_word} remaining', red))
    