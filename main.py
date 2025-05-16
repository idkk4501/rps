import random

print('YOU ARE PLAYING AGAINST THE COMPUTER')

player = input('rock, paper, or scissors? or q to quit>')
pos = 'rock', 'paper', 'scissors'
computer = random.choice(pos)

print('THE COMPUTER CHOSE' , computer)

while True:
    if computer == player:
        print('TIE')
        
    elif computer == 'rock':
        if player == 'paper':
            print('U WIN')
            
    elif computer == 'rock':
        if player == 'scissors':
            print('U LOST')
            
    elif computer == 'paper':
        if player == 'rock':
            print('U WIN')
            
    elif computer == 'paper':
        if player == 'scissors':
            print('U LOST')
            
    elif computer == 'scissors':
        if player == 'paper':
            print('U LOST')
            
    elif computer == 'scissors':
        if player == 'rock':
            print('U WIN')
            
    if player == 'q':
        break



