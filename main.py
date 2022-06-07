import random

print("ROCK PAPER SCISSORS GAME: \n")
print("Winning Rules of the Rock Paper Scissors game as follows: \n"
                                +"Rock vs Paper->Paper wins \n"
                                + "Rock vs Scissors->Rock wins \n"
                                +"paper vs Scissors->Scissors wins \n")

user_choice = ""
computer_choice = ""

while user_choice == computer_choice:  
    #declaring possible options
    possible_options = ["R", "P", "S"]
    game_dict = {
        'R': "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    #Record user input in uppercase
    user_input = input('Enter your choice (R for Rock, P for Paper, S for Scissors): ')
    upper_input = user_input.upper()

    #Check if input is valid
    while upper_input not in possible_options:
        new_input = input('Invalid input, Please enter a valid option: ')
        upper_input = new_input.upper()

    #Make choice for computer
    computer_input = random.choice(possible_options)

    #Convert letter inputs to words
    user_choice = game_dict.get(upper_input)
    computer_choice = game_dict.get(computer_input)

    print(f"Player({user_choice}) : CPU({computer_choice}) \n")

    if user_choice == computer_choice:
        print(f"Both Players chose {user_choice}, it's a tie.")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print(f"Paper covers Rock, CPU wins!")
        else:
            print(f"Rock smashes Scissors, You win! \n")

    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"Paper covers Rock, You win!")
        else:
            print(f"Scissors cuts paper, Computer wins!")

    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print(f"Scissors cuts Paper, You win!")
        else:
            print(f"Rock smashes Scissors, CPU wins!")
            

