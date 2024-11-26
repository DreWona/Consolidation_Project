#Tuple out game

#Module for random dice rolls
import random

def short_rule():
    print("""
    Tupple out game.
        Rules: Let luck be on your side
        1. Maximum player is 3 but 1-3 can play. Each player enters their name.
        2.Players set a winning score. highest score at the end of 3 turn wins
        3.Rolling two of the same number allows you to reroll if you want.
        4.Tuple out mean you earn 0 points
        5.If you dont tuple you cant reroll for that turn,(you get what you deserve).
        6.Each player gets 3 turns
          """)

#Function for rolling a 6 sided die

#Three dice with values ranging from 1-6 for random rolls
def dice_roll(dice_count=3):
    return[random.randint(1,6) for _ in range(dice_count)] 


#For players turn
def players_turn(player_name):
    print(f"{player_name}'s turn")
    
    #Passes the  dice role func to the variable dice
    dice = dice_roll()
    print(f"You rolled: {dice}")

    #Tuple check, if dice role 1,2,3 are the same = 0 points
    if dice[0] == dice[1] == dice[2]:
        print("All dice are the same number, You earn 0 points this turn.")
        return 0
    
    #When a tuple occurs allow a reroll of the non tuple die..
    while True:
        fixed_dice = [die for die in dice if dice.count(die) > 1]
        free_dice_count = 3 - len(fixed_dice)

        #print(f"Fixed dice: {fixed_dice}. You can reroll {free_dice_count} dice.")
        #If no Fixed dice/no reroll on turn 
        if free_dice_count == 0:       #or input("Reroll free dice? (y/n): ").strip().lower() != "y":
            print("All dice have a different value. Turn ends.")
            break

        print(f"Fixed dice: {fixed_dice}. You can reroll {free_dice_count} dice.")
        roll_or_not = input("Reroll free dice? (y/n): ").strip().lower()
        #if plyer dont want to reroll, end.
        if roll_or_not != "y":
            break

        #Reroll free dice
        #Dice roll func + free dice thats not a tuple/fixed for new value.
        new_roll = dice_roll(free_dice_count)
        print(f"You rerolled: {new_roll}")
        dice = fixed_dice + new_roll

        #Check if its a tuple again
        if dice[0] == dice[1] == dice[2]:
            print("All dice are the same number, You earn 0 points this turn.")
            return 0
        
        #Calc score
        score = sum(dice)
        print(f"{player_name}'s score for this turn: {score}")
        return score

def start_game():
    #print the rules
    short_rule()
    print("Welcome to Tuple out.\n" )
    player_count = int(input("How many player (1-3): "))
    player_name = (input("Enter name: "))
    win_condition = int(input("Set score to reach for win: "))

    scores = [0] * player_count

    while True:
        for p in range(player_count):
            print(f"player {p + 1}'s current score: {scores[p]}")
            scores[p] += players_turn(f"Player {p + 1}")

    
start_game()


