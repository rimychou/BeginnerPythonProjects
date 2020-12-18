import random

# Play game of rock, paper, or scissors
# Get user input
# Compare user input to choices
# If user input superior, they win. Otherwise, computer wins
# Play game for an X number of times


choices = ('rock', 'paper', 'scissors')
random_choices = random.choice(choices)
user_input = None
user_point = 0
my_point = 0
counter = 1
print("Let's play a game of rock, paper, or scissors\n"
      "We\'ll play a total of 5 rounds.\n")

while counter <= 5:
    user_input = input('Please enter your guess (rock, paper, or scissors): ').casefold()
    while user_input == random_choices:
        random_choices = random.choice(choices)
    if user_input == 'rock' and random_choices == 'paper':
        my_point += 1
        print('Drat! You didn\'t win this round. I guessed {}.'.format(random_choices))
    elif user_input == 'rock' and random_choices == 'scissors':
        user_point += 1
        print('Great job! You win! My choice was {} while your choice was {}'.format(random_choices, user_input))
    elif user_input == 'paper' and random_choices == 'rock':
        user_point += 1
        print('Great job! You win! My choice was {} while your choice was {}'.format(random_choices, user_input))
    elif user_input == 'paper' and random_choices == 'scissors':
        my_point += 1
        print('Drat! You didn\'t win this round. I guessed {}.'.format(random_choices))
    elif user_input == 'scissors' and random_choices == 'paper':
        user_point += 1
        print('Great job! You win! My choice was {} while your choice was {}'.format(random_choices, user_input))
    elif user_input == 'scissors' and random_choices == 'rock':
        my_point += 1
        print('Drat! You didn\'t win this round. I guessed {}.'.format(random_choices))
    else:
        print('This is not a valid choice')
    counter += 1


if my_point > user_point:
    print('\nSorry, you lost! I scored {} while you scored {}.'.format(my_point, user_point))
elif my_point < user_point:
    print('\nYou won! You scored {} while I scored {}.'.format(user_point, my_point))
elif my_point == user_point:
    print('We end at the tie!')