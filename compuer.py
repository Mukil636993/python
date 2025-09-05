from random import choice
import sys
from enum import Enum
class RPS(Enum):
  ROCK=1
  PAPER=2
  SCISSOR=3
def rps():
  game_count=0
  python_win=0
  playerg=0
  def play_rps():
    nonlocal python_win
    nonlocal playerg
    nonlocal game_count
    user_choice=input("Enter.....\n 1 for rock \n 2 for paper \n 3 for scissor\n\n")
    if user_choice not in ('1','2','3'):
      print('enter the correct input')
      return play_rps()
    player=int(user_choice)
    print("player choice is "+ str(RPS(player)).replace('RPS.',''))
    bot_choice=choice("123")
    bot=int(bot_choice)
    print ("bot choice is " + str(RPS(bot)).replace('RPS.','')+"\n")
    if(player==bot):
      print("match draw")
      print('')
    elif(player==1 and bot==3) or (player==2 and bot==1) or (player==3 and bot==2):
      print("player won 🎉")
      print('')
      playerg+=1
    else:
      print("python wins🐍")
      print('')
      python_win+=1
    game_count+=1
    print(f'game played {game_count}')
    print(f'player win {playerg}')
    print(f'bot win {python_win}')
    print('want to play again?')

    while True:
      player_input=input('y for play again\n q for quit')
      if player_input.lower() not in ('y','q'):
        continue
      else:
        break
    if player_input=='y':
     play_rps()
    else:
     sys.exit('bye 🤞✌✌')
  return play_rps
play=rps()
play()