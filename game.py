#Import the random library
import random

#Add the code to create a list containing the three actions of the game.
list = ['rock','paper','scissors']

#Add the code to set the scores of players to 0
score1 = 0
score2 = 0

#Add the code to ask the user how many rounds they want to play
print("rounds?")
rounds = input()

#Write a for loop and put the game inside
for i in range(int(rounds)):

  #Add the code to select a random action for each player
  result1 = random.choice(list)
  result2 = random.choice(list)

  #Add the code to print the players choices
  print(result1)
  print(result2)

  if result1 == result2:
    print("Tie! Both players chose the same action.")
  elif result1 == "paper" and result2 == "rock":
    print("player 1!")
    score1 += 1
  elif result1 == "paper" and result2 == "scissors":
    print("player 2!")
    score2 += 1
  elif result1 == "scissors" and result2 == "rock":
    print("player 2!")
    score2 += 1
  elif result1 == "scissors" and result2 == "paper":
    print("player 1!")
    score1 += 1
  elif result1 == "rock" and result2 == "paper":
    print("player 2!")
    score2 += 1
  elif result1 == "rock" and result2 == "scissors":
    print("player 1!")
    score1 += 1

  #print the score
print("Player 1: " + str(score1))
print("Player 2: " + str(score2))

