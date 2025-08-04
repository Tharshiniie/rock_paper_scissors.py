import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper" , "scissors"]

count = 0

while True:
    user_wins = 0
    computer_wins = 0
    count = 0

    print("There are 5 rounds in rock, paper, scissors!\n")
    print("You Vs. Computer!\nBegins!!")

    while count < 5:
        user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        random_number = random.randint(0,2)
        #rock:0, paper:1, scissors:2

        computer_pick = options[random_number]
        print("computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1


        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1


        elif user_wins == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1

        elif user_input == computer_pick:
            print("Draw!")

        else:
            print("You lost!")
        computer_wins += 1

        count += 1

    print("You won", user_wins, "times.")
    print("The computer won", computer_wins, "times.")

    rematch = input("Rematch? Enter 'yes' or Q for quit: ").lower()

    if rematch != "yes":
        print("Goodbye!")
