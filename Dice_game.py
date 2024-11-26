#Tuple out game

#Current Rules: Score the most points/ Set point specified. Players take turn rolling
#Each turn, the active player rolls three dice.
#Printed_Rules = ["Max of 3 players. \n" "Score the most points/ Set point specified. Players take turn rolling "]
#print(Printed_Rules)

#Module for random dice rolls
import random

print("Rolling two of the same number allows you to reroll if you want.\n")
print("Tupleing out mean you earn 0 points")
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

    #Tuple check, if dice role 1,2,3 are the same
    if dice[0] == dice[1] == dice[2]:
        print("All dice are the same number, You earn 0 points this turn.")
        return 0
    
    #When a tuple occurs allow a reroll of the non tuple die..
    while True:
        fixed_dice = [die for die in dice if dice.count(die) > 1]
        free_dice_count = 3 - len(fixed_dice)


