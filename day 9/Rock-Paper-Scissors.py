import time, pyinputplus, random

import outcome

possible_choices = ("Rock", "Paper", "Scissors")


def Rock_paper_scissors():
    global outcome
    player_choice = pyinputplus.inputMenu(possible_choices, prompt="What\'s your move?\n", numbered=True)
    player_move = possible_choices.index(player_choice)
    computer_move = random.randrange(0, 3)
    while computer_move == player_move:
        computer_move = random.randrange(0, 3)
    time.sleep(.5)
    print(f"Player move is {possible_choices[player_move]}")
    time.sleep(.5)
    print(f"Computer move is {possible_choices[computer_move]}")
    time.sleep(1)
    # print('\n')
    if player_move == computer_move:
        outcome = 0
    elif player_move == 0 and computer_move == 1:
        outcome = -1
    elif player_move == 0 and computer_move == 2:
        outcome = 1
    elif player_move == 1 and computer_move == 0:
        outcome = 1
    elif player_move == 1 and computer_move == 2:
        outcome = -1
    elif player_move == 2 and computer_move == 0:
        outcome = -1
    elif player_move == 2 and computer_move == 1:
        outcome = -1
    else:
        print("Can't decide who won, check the code again!")
    return outcome

player_score = 0
computer_score = 0

while True:
    for i in range(3):
        Rock_paper_scissors()
        if 1 == outcome:
            print("Player Wins")
            player_score += 1
        elif -1 == outcome:
            print("Computer Wins")
            computer_score += 1
        else:
            print("draw")
        print(f"Player: {player_score}\nComputer: {computer_score}")
        print("\n")
        i += 1
    d = pyinputplus.inputYesNo("Play again? ")
    if d == 'No':
        print(f"Player: {player_score}\nComputer: {computer_score}")
        time.sleep(.5)
        print("End of the game")
        break
