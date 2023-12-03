import random

player_wins = 0
machine_wins = 0

options = ["scissors", "rock", "paper"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_input == "q":
        break 
    
    if player_input not in options:  
        continue
    
    random_number = random.randint(0, 2)
    # scissors: 0, rock: 1, paper: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if player_input == "rock" or computer_pick == "scissors":
        print("You won!")
        player_wins += 1
        
    elif player_input == "paper" or computer_pick == "rock":
        print("You won!")
        player_wins += 1
        
    elif player_input == "scissors" or computer_pick == "paper":
        print("You won!")
        player_wins += 1
        
    else:
        print("You lost!")
        machine_wins += 1

        
print("You won", player_wins, "times.")
print("The Machine won", machine_wins, "times.")    
print("Bye bye!")