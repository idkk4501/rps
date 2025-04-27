import random

print('starting RPS...')

print('loading...Done')

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

if user == 'q':
 print('stopping your RPS session...Done')

if user not in pcch:
 print('you typed in an invalid option. please try again')

exit = input('thaks for playing press e to exit:')
 
if exit == 'e':
 print('closing now')




