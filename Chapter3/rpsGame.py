import random, sys

print('ROCK, PAPER, SCISSORS')

# These varaibles keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

while True: # This is the main game loop.
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    while True: # This is the play input loop.
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input('> ')
        if player_move == 'q': # Player wants to quit.
            sys.exit() # Quits the program.
        if player_move in ['r','p','s']:
            break # Move is valid, so break out of input loop.
        print('Invalid move. Type one of r, p, s or q.')

        # Display the player's chosen move.
        if player_move == 'r':
            print('ROCK versus...')
        elif player_move == 'p':
            print('PAPER versus...')
        elif player_move == 's':
            print('SCISSORS versus...')

        # Display the computer's move.
        move_number = random.randint(1, 3)
        if move_number == 1:
            print('ROCK')
            computer_move = 'r'
        elif move_number == 2:
            print('PAPER')
            computer_move = 'p'
        elif move_number == 3:
            print('SCISSORS')
            computer_move = 's'

        # Determine the winner.