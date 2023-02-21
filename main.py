import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img = [rock, paper, scissors]

score = [0, 0]

def rps_game():
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    print(img[player])

    print("Computer chose:")

    comp = random.randint(0, 2)

    print(img[comp])
    text = ""
    if player == comp:
        text = "It is a draw"
    elif player == 0:
        if comp == 1:
            text = "You lose"
            score[1] += 1
        else:
            text = "You win"
            score[0] += 1
    elif player == 1:
        if comp == 2:
            text = "You lose"
            score[1] += 1
        else:
            text = "You win"
            score[0] += 1
    elif player == 2:
        if comp == 0:
            text = "You lose"
            score[1] += 1
        else:
            text = "You win"
            score[0] += 1
    else:
        print("Well that was unexpected")
    print(text)
    ending = ""
    if score[0] == score[1]:
        ending = "Total result is Draw"
    elif score[0] > score[1]:
        ending = "you are good at this. Total result is your victory"
    else:
        ending = "Computer is better at this. No wonder, computers even better at chess than humans"

    print(f"You won {score[0]} times, computer won {score[1]} times, {ending}")


play = True

while play is True:
    play = False
    rps_game()
    continue_button = input("If you want to play again, press 1")
    if continue_button == "1":
        play = True
