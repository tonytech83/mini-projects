import random

computer_options = ['r', 'p', 's']

player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')
your_wins = 0
your_loses = 0
draws = 0

while player_move != 'e':
    computer_move = random.choice(computer_options)
    if player_move == computer_move:
        draws += 1
        print('Draw!')
    elif player_move == 'r' and computer_move == 's' \
            or player_move == 'p' and computer_move == 'r' \
            or player_move == 's' and computer_move == 'p':
        your_wins += 1
        print('You win!')
    else:
        your_loses += 1
        print('You lose!')

    player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')

if player_move == 'e':
    print('---------------------')
    print('Result is:')
    print(f'Wins: {your_wins}')
    print(f'Loses: {your_loses}')
    print(f'Draws: {draws}')
