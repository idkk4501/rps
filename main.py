import random

print('starting RPS...')

user = input('rock paper or scissors?:')  
pcch = ["rock", "paper", "scissors]
program = random.choice(pcch)

print(f'yo dumbahh chose{user}, the computer chose{program'})

if user == program:
print('tied')

elif user == 'rock':
if program == 'scissors':
print('you win u want a damn medal or smth?')

elif user == 'rock':
if program == 'paper':
print('you lost faggotino')

elif user == 'paper':
if program == 'rock':
print('u win u want a damn medal or smth?')


