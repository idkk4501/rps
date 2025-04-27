import random

print('starting RPS...')

user = input('rock paper or scissors?:')  
pcch = ["rock", "paper", "scissors"]
program = random.choice(pcch)

print('the computer picked: ', program)

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

elif user == 'paper':
 if program == 'scissors':
  print('u fucking lost faggot u bad')

elif user == 'scissors':
 if program == 'paper':
  print('HOLY SHIT U WON U SOME KIND OF MIND READER PSYCHIC OR SOME SHIT OR A WITCH?')

elif user == 'scissors':
 if program == 'rock':
  print('U LOST GET BETTER')

if user not in pcch:
 print('OOPS, U MADE A FUCKY WUCKY. PLEASE TRY AGAIN')



