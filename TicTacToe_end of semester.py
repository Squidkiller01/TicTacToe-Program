#CIT end of course program
#Create a function game of TicTacToe using everything you have learned
'''
Michael Porter
CIT 144
'''
#############################
'''
ideas for implementation:
✓ Required: Build a program that works
✓ Required: Use classes and methods if possible
X Required: Make a flow chart for the program
✓ Use an Array or list (update values on the array and print newline after value [3] and [6])
✓ Coordinate with letters and numbers - maybe rows are letters and columns are numbers?
✓ Represent each position on the board as a 3x3 grid of dashes or underscores
✓ Make different modes for singleplayer and multiplayer (Mr.Gray suggested)
✓ Make as good as possible user interface using Python3
✓ implent if & try and except statements to prevent incorrect inputs and errors within program
'''
import random #imports the python random module
import time #imports the python time module

class wins: #declares a class named "wins" that is used to check for winning conditions
    def __init__(self,playerx,playero,tiles): #class method that initializes all variables passed inside the class
        self.playerx = playerx
        self.playero = playero
        self.game_over = False
        self.tiles=tiles
    def winning_checks(self): #class method that initiates the process for checking winning conditions
        for i in range(2): #causes the indented code below to repeat twice to check for both players
            hori_wins=[[1,2,3],[4,5,6],[7,8,9]] #declares possible values for horizontal, verticle, and diagonal wins
            vert_wins=[[1,4,7],[2,5,8],[3,6,9]] # ^
            dia_wins=[[1,5,9],[3,5,7]]          # ^
            if i == 0: #will check for player x's conditions if the i value from the above for loop is equal to 0
                player = playerx #declares the player variable equal to the passed in playerx variable
                Player = "Player X" #decleares the Player variable equal to the current player's name for later printing use
            else: #if the i value from before does not equal 0, will use the above indented code except for player O instead of player X
                player = playero
                Player = "Player O"
            for value in player: #repeats for every value in the player's list
                for instance in hori_wins: #repeats for every sub-array inside the hori_wins multi-dimensional array
                    if value in instance: #if the player's number is inside said sub-array
                        index = instance.index(value) #grabs the index of the number inside the sub-array and... 
                        del instance[index] #deletes the value for later use (may be confusing why at first but it will make sense soon)
            for instance in hori_wins: 
                if instance == []: #checks if there is an empty sub-array inside the hori_wins multi-dimensional array
                    self.game_over = True #if there is, declares the game as over
                    print_board(self.tiles) #prints the board one last time
                    print(f"{Player} has won the game with a horizontal win!") #declares that the current player has won due to a horizontal win
                    if self.game_over: #makes one last check to see if the game is over
                        return self.game_over #if the game is for sure over, returns a value to end the program
            for value in player: #from down on repeats the same as the horizontal winning checks except for both verticle and diagonal
                for instance in vert_wins:
                    if value in instance:
                        index=instance.index(value)
                        del instance[index]
            for instance in vert_wins:
                if instance == []:
                    self.game_over = True
                    print_board(self.tiles)
                    print(f'{Player} has won the game with a verticle win!')
                    if self.game_over:
                        return self.game_over
            for value in player:
                for instance in dia_wins:
                    if value in instance:
                        index=instance.index(value)
                        del instance[index]
            for instance in dia_wins:
                if instance == []:
                    self.game_over=True
                    print_board(self.tiles)
                    print(f'{Player} has won the game with a diagonal win!')
                    if self.game_over:
                        return self.game_over
        
positions = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"] #decleares all available positions in the board
tiles = ["-","-","-","-","-","-","-","-","-",] #list of the tiles for print on the board
playerx = [] #declares an empty array for use of storing all of playerx's spots
playero = [] #does the same as the playerx array declaration except for playero
global turn #declares turn as a variable for global use
turn = 2 #declares turn to equal 2 so other modulus checks will work properly for multiplayer mode
turn2 = 2 #declares a turn2 variable for the same purpose as the turn variable except for singleplayer against AI
def print_board(tiles): #defines the function for printing the TicTacToe board with any and all updated values
    print(f'\n    1   2   3\n  _____________ \nA | {tiles[0]} | {tiles[1]} | {tiles[2]} | \n  |―――|―――|―――| \nB | {tiles[3]} | {tiles[4]} | {tiles[5]} | \n  |―――|―――|―――| \nC | {tiles[6]} | {tiles[7]} | {tiles[8]} | \n  -------------')

def player_check(turn): #checks for which player's turn it is
    if turn % 2 == 0: #declares all even numbered turns (including the first turn) as player X's turn
        return ("X")
    else: #if the turn is not even, declares the turn as Player O's turn
        return ("O")

def get_chosen_tile(positions,playerx,playero,mode,turn2,tiles,stalemate): #declares a function where the user will input what spot they want to choose and the program will verify said spot is available
    checkoverall = True 
    number = 0
    while stalemate == False: #will run below indented code if there is no stalemate
        for value in tiles: #iterates through all values in the tiles array to check if there are any free spots
            if value == '-':
                number += 1
        if number !=0: #if there are free spots, the program will continue as normal
            if turn2 % 2 == 0: #checks if it is the player's turn in singleplayer mode as the player will always go first in singleplayer
                while checkoverall: #loops through the below indented code if chosen spots are not available
                    check = True
                    while check: #loops indented code below while check equals True
                        x = input("row: ") #user will choose either row A, B, or C
                        x=x.upper() #capitalizes the user's chosen row
                        if x == "A" or x == "B" or x == "C": #if the chosen exists, program will continue
                            check = False
                        else: #however, if the row does not exist, the user will have to continue choosing a new row until they choose one that exists
                            print("Referenced row value does not exist, please input either A, B, or C")
                    check = True
                    while check: #loops through below indented code for the same checks and inputs as above except for columns this time
                        y = int(input("column: "))
                        if y >= 1 and y <= 3:
                            check = False
                        else:
                            print("Referenced column value does not exist, please input either 1, 2, or 3")
                    x=x.upper()
                    tile = x + str(y) #combines both the row letter and column number to gather the wanted tile
                    index = positions.index(tile) #checks through the print tile array for the value's index
                    if index+1 in playerx or index+1 in playero: #if the chosen value is already taken on the board, repeats the function to make the user choose again
                        print("You cannot overlap positions! Please pick an empty position on the board.")
                    else: #if the chosen position is free
                        checkoverall=False #ends the overall checks and function loop
                        if mode == 1: #if the gamemode is singleplayer
                            turn2+=1 #adds 1 to the turn2 variable to tell the program it is the AI's turn next
                        return tile,turn2 #returns both needed values
            elif turn2%2==1: #if the gamemode is singleplayer and it is the bot's turn
                options = ["A","B","C"] #declares a list of rows for the bot to choose from
                overlap = True #declares a variable for overlap detection
                print("Opponent is picking...") #notifies the bot is choosing the location
                while overlap: #until the bot chooses a position that is not already filled on the board
                    letter = random.randint(0,2) #randomly chooses an index value for the options array
                    x = options[letter] #gathers the random index and assigns x the value of the letter in the index slot
                    y = random.randint(1,3) #assigns y a random value of 1, 2, or 3
                    tile = x + str(y) #combines both x and y to get the full tile
                    index = positions.index(tile) #gathers the index of the chosen tile
                    if index+1 in playerx or index+1 in playero: #checks to see if the chosen tile is already taken or not
                        continue #if the tile already taken, the while loop will repeat
                    else: #until the chosen tile is not taken
                        overlap = False #updates overlap to equal False so the while loop will no longer loop
                seconds=random.randint(1,7) #assigns seconds a random value from 1 to 7
                time.sleep(seconds) #pauses the program for the assigned seconds variable 
                turn2+=1 #adds a value to turn2 to signify the next turn is the player's
                return tile,turn2 #returns both values
        else: #however if there are none, then the program will declare a stalemate and end
            stalemate = True #assigns stalemate to equal True
            print("Game Over. Stalemate (No Winners)") #prints the game is over and there are no winners
            return stalemate, turn2 #returns both values
        

def update_tile(chosen_tile, tiles, positions, turn, playerx, playero): #function to update a tile onto the board
    index = positions.index(chosen_tile) #gathers the index of the chosen_tile's value from the positions array
    tiles[index] = player_check(turn) #assigns the index in the printed array either X or O depending on which player's turn it is
    if player_check(turn) == "X": #if it is player X's turn
        playerx.append(index+1) #adds the tile to player X's list
        playerx.sort()
    elif player_check(turn) == "O": #otherwise, assigns it to player O's list
        playero.append(index+1)
        playero.sort()
    else: #prints an error value if no player's turn can be calculated or assigned
        print("STORE ERROR: Value could not be stored due to no player recognized")
    return playerx,playero,positions,tiles #returns all needed values

def play(no_winner,turn,tiles,positions,playerx,playero,mode,turn2,stalemate): #main function that runs the entire game and makes it functional
    while no_winner: #runs below indented code if there is no winner
        print_board(tiles) #prints the board so players can see available tiles
        chosen_tile,turn2 = get_chosen_tile(positions,playerx,playero,mode,turn2,tiles,stalemate) #gathers all returned variables from the get_chosen_tile function
        if chosen_tile == True: #detects if there is a stalemate
            no_winner = False #declares the game as over
            break #breaks out of the while loop just in case it tries to continue as normal
        playerx,playero,positions,tiles = update_tile(chosen_tile, tiles, positions, turn, playerx, playero) #gathers all returned variables from the update_tile function
        conditions=wins(playerx,playero,tiles) #declares the wins class to the variable: conditions
        check = conditions.winning_checks() #gathers the returned value from the winning_checks class sub-method
        if check: #if a winning condition has been fulfilled
            no_winner = False #declares the game over
            break #breaks from the while loop just in case
        turn += 1 #adds a value to the turn variable for repeated iterations so the program can tell which player's turn

no_winner = True #declares there is no winner yet
string_check = True #declares string_check as True
stalemate = False #declares no stalemate
print("Ready to play some Tic Tac Toe? Before you do that...") #first line to introduce the program when the program is first run
while string_check:
    try: #continues the program unless the next input statement is not an integer
        mode = int(input("Select a mode from the options below: \n   1. 1 Player \n   2. 2 Player \nSelection: ")) #allows the player to choose the gamemode
        if mode != 1 and mode != 2: #if the gamemode is neither singleplayer or multiplayer
            while mode != 1 and mode != 2: 
                print("Invalid option, please pick either 1 or 2.")
                try:
                    mode = int(input("Selection: ")) #continously make the player choose a gamemode until they choose on that is valid
                    string_check = False #breaks out of the gamemode while loop
                except: #if the input value is not an integer, continues the while loop instead of breaking out
                    continue
        else:
            string_check = False
    except:
        print("Invalid option, please select either 1 or 2.")
        continue
play(no_winner,turn,tiles,positions,playerx,playero,mode,turn2,stalemate) #runs the main function to run the program until a winner or a stalemate is declared