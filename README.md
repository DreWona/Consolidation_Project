#Tuple out game

##Rules: Let luck be on your side
1. **Maximum player is 3 but 1-3 can play. Each player enters their name.
2. **Players set a winning score. highest score at the end of how ever many turn wins
3. **Rolling two of the same number allows you to reroll if you want.
4. **Tuple [4,4,4] out mean you earn 0 points
5. **If 3 die are unique [1,2,3], player can reroll 3 die once or choose not to
6. **If you choose to reroll 3 "unique" number and get [3,5,3]. You cant reroll

## Module random for dice rolling

## There are 4 functions
1. short_rule: Prints the game directions/rules when it starts
2. dice_roll: For rolling random numbers for a 1-6 die
3. players_turn: To manage what happens when a tuple occurs, a loop for fixed dice, and to promt the player  to reroll or not. Then calculate the players socre per round
4. start_game: For starting the game and enter player #/name and score to win. (Run this to play)

## To start game
1. Open miniconda
2. Navigate to the location of the repository
3. type python Dice_game.py
4. pyhton start_game() function
5. Enter player count
6. Name each player
7. Reroll when prompter IF you want

## ADVANCE Features
1. Imported Time as clock to add a slight delay between players turn and roll so that it obvious whos turn it is.
