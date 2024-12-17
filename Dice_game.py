#Tuple out game

#Module for random dice rolls
import random
import time as clock
import pandas as pd

def short_rule():
    print("""
    Tupple out game.
        Rules: Let luck be on your side
        1. Maximum player is 3 but 1-3 can play. Each player enters their name.
        2.Players set a winning score. highest score at the end wins
        3.Rolling two of the same number allows you to reroll if you want.
        4.Tuple [4,4,4] out mean you earn 0 points
        6.If 3 die are unique [1,2,3], player can reroll 3 die once or choose not to
        7. If you choose to reroll 3 "unique" number and get [3,5,3]. You cant reroll
        8. Enter 'y' or 'no' when prompted. Failure defaults to a no reroll
          """)

#Function for rolling a 6 sided die

#Three dice with values ranging from 1-6 for random rolls
def dice_roll(dice_count=3):
    return[random.randint(1,6) for reach in range(dice_count)] 


#For players turn
def players_turn(player_name):
    print(f"{player_name}'s turn")
    clock.sleep(1.5)
    
    #Passes the  dice role func to the variable dice
    dice = dice_roll()
    print(f"You rolled: {dice}")

    #Tuple check, if dice role 1,2,3 are the same = 0 points
    if dice[0] == dice[1] == dice[2]:
        print(f"All dice are the same number, {player_name} earn 0 points this turn. \n")
        return 0
    #the culprit that prevents it from breaking when player says 'n'
    score =sum(dice)
    
    #When a tuple occurs allow a reroll of the non tuple die..
    while True:
        fixed_dice = [die for die in dice if dice.count(die) > 1]
        free_dice_count = 3 - len(fixed_dice)

        #print(f"Fixed dice: {fixed_dice}. You can reroll {free_dice_count} dice.")
        #If no Fixed dice/no reroll on turn 
        if free_dice_count == 0:       #or input("Reroll free dice? (y/n): ").strip().lower() != "y":
            print("All dice have a different value. Turn ends.\n")
            break

        print(f"Fixed dice: {fixed_dice}. You can reroll {free_dice_count} dice once.")
        roll_or_not = input("Reroll free dice? (y/n): ").strip().lower()
        
        #if plyer dont want to reroll, end.
        if roll_or_not == "n":
            print("No rerolls, turn ends,\n")
            return score #Ends the player turn when they say no
        elif roll_or_not == "y":
            #Reroll free dice
            new_roll = dice_roll(free_dice_count)
            print(f"You rerolled: {new_roll}.\n")
            dice = fixed_dice + new_roll

            #Check if its a tuple again
            if dice[0] == dice[1] == dice[2]:
                print("All dice are the same number, You earn 0 points this turn.\n")
                return 0
        else:
            print("Enter 'y' or 'n'.")
        
        #Calc score
        score = sum(dice)
        print(f"{player_name}'s score for this turn: {score}.\n")
        return score
    return score

#Function for the main game loop
def start_game():
    #print the rules
    short_rule()
    print("Welcome to Tuple out.\n" )
    
    #Shows the date and time the game starts
    current_time = clock.strftime("%m-%d-%Y %H:%M:%S", clock.localtime())
    print(f"Game started at: {current_time} \n")

    #test
    #scores_stat = []
    #for palyers in player_names:
        #turn_score = players_turn(player)
       
    
    #Set number of player (1-3)
    while True:
        try:
            player_count = int(input("How many player (1-3): "))
            if 1 <= player_count <= 3:
                break
            else:
                print("Players can only range between 1 and 3.\n")
        except ValueError:
            print("Not the required number. Try again")

    #Set player name based on amount of players
    player_names = []
    for number in range(player_count):
        #Uses the player count number as to set specific amount of names
        name = input(f"Name the player {number + 1}: ")
        #Takes the names enter and appends it to the player name list
        player_names.append(name) 
    
    #Scores to set
    while True:
        try:
            win_condition = int(input("Set score to reach for win: \n"))
            if win_condition > 0:
                break
            else:
                print("Score must be higher than 0")
        except ValueError:
            print("zeroes and Negative numbers not allowed.")

    #For scores and score holding
    score_stat = []
    scores = {name: 0 for name in player_names}

    #
    while True:
        for player in player_names:
            #score_stat = []
            #Staggers the rolling popup
            clock.sleep(1.5)
            print(f"{player}'s current score: {scores[player]}")
            turn_score = players_turn(player)
            #Adds up the scores from previous turns
            scores[player] += turn_score 
            score_stat.append({"Player": player, "Turn": len(score_stat) + 1, "Score": turn_score})

            #Testing if it prints
            #print(score_stat)

            if scores[player] >= win_condition:
                print(f"{player} wins with {scores[player]} points")
                #Shows the time the game ended
                current_time = clock.strftime("%m-%d-%Y %H:%M:%S", clock.localtime())
                print(f"Game Ended at: {current_time} \n")
                #for stat in score_stat:
                    #print(stat)
                #Passing score stat to a new function
                score_digest(score_stat, player_names)
                return
#New function to display a table of scores at the end.
def score_digest(score_stat, player_names):
    print("Score Table \n" + "-" * 20)
    table = pd.DataFrame(score_stat)
    
    for player in player_names:
        print(f"{player} Scores:\n")
        player_table = table[table["Player"] == player] 
        total_score = player_table["Score"].sum()
        
        print(player_table.to_string(index = False))
        print(f"{total_score}")
#score_digest()

            

 #Starts the full game   
start_game()


