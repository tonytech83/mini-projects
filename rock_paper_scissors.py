import random

computer_options = ['rock', 'paper', 'scissors']

player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')
your_wins = 0
your_loses = 0
draws = 0

while player_move != 'e':
    if player_move == 'r':
        player_move = 'rock'
    elif player_move == 'p':
        player_move = 'paper'
    elif player_move == 's':
        player_move = 'scissors'
    computer_move = random.choice(computer_options)
    print(f'Your chose: {player_move}')
    print(f'Computer chose: {computer_move}')
    if player_move == computer_move:
        draws += 1
        print('>>> Draw! <<<')
    elif player_move == 'rock' and computer_move == 'scissors' \
            or player_move == 'paper' and computer_move == 'rock' \
            or player_move == 'scissors' and computer_move == 'paper':
        your_wins += 1
        print('>>> You win! <<<')
    else:
        your_loses += 1
        print('>>> You lose! <<<')

    player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')

print(f'------------------------\n| The final result is:\n| Wins: {your_wins}\n| Loses: {your_loses}\n| Draws: {draws}\n------------------------')
