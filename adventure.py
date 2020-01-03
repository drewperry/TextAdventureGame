# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Drew Perry
"""
__version__ = 8

# 2) print_introduction: Print a friendly welcome message for your game
def print_introduction():
    print("I have so many bills to pay!"
          "\nWe have to get a picture of something juicey!")
# 3) get_initial_state: Create the starting player state dictionary
def get_initial_state():
    playerStates = {"game status": "playing",
                    "location": "plaza",
                    "broken camera": False,
                    "scoop": False,
                    "best picture": False}
    return playerStates

# 4) print_current_state: Print some text describing the current game world
def print_current_state(the_player):
    print("We are in the " + the_player["location"])
    
# 5) get_options: Return a list of commands available to the player right now
def get_options(the_player):
    #Plaza options
    if(the_player["location"] == 'plaza'):
        currOptions = ["visit restaurant", "join crowd" , "quit"]
        return currOptions
    
    #Crowd options
    elif(the_player['location'] == "crowd"):
        currOptions = ["leave crowd", "get closer" , "quit"]
        return currOptions
    
    #Restaurant options
    elif(the_player['location'] == "restaurant"):
        currOptions = ["leave restaurant", "ask around", "quit"]
        return currOptions
    
    #Bar options
    elif(the_player['location'] == "bar"):
        currOptions = ["return to plaza", "go to VIP room", "quit"]
        return currOptions
    
    #VIP room options
    elif(the_player['location'] == "VIP room"):
        currOptions = ["take picture", "quit"]
        return currOptions
        
        
# 6) print_options: Print out the list of commands available    
def print_options(available_options):
    print("Geez....what should I do?")
    print("********************************")
    for a in available_options:
        print(a)
        
# 7) get_user_input: Repeatedly prompt the user to choose a valid command
def get_user_input(available_options):
    chosen_command = ""
    while (chosen_command not in available_options):
        chosen_command = input("THINK QUICK! ")
        #Finds quit in command
        if('quit' in chosen_command):
            return "quit"
        
    return chosen_command
        
# 8) process_command: Change the player state dictionary based on the command
def process_command(chosen_command, the_player):
    print("********************************")
    #Quit decision
    if(chosen_command == "quit"):
        the_player['game status'] = "quit"
        print("Sorry to see you go!")
        
    elif(chosen_command == "visit restaurant"):
        the_player['location'] = "restaurant"
        print("Wow! So many people in here!"
              "\ntoo bad none of them are celebs..."
              "\nwait...I think I hear some gossip..")
        
    elif(chosen_command == "join crowd"):
        print("So much going on!!"
              "\nI can't quite see the front...")
        the_player['location'] = "crowd"
        
    elif(chosen_command == "leave crowd"):
    
        print("Oh geez that was too much!"
              "\nPerhaps somewhere else?")
        the_player['location'] = "plaza"
            
    elif(chosen_command == "leave restaurant"):
        print("Back to square one.....")
        the_player['location'] = "plaza"
        
    elif(chosen_command == "ask around"):
        print("ALAS! A lead! People say Jay Z is cheating again!"
              "\nOff to the bar we go!")
        the_player['location'] = "bar"
        the_player['scoop'] = True
        
    elif(chosen_command == "return to plaza"):
        print("Ahhh...back again..")
        the_player['location'] = "plaza"
        
    elif(chosen_command == "go to VIP room"):
        if(the_player['scoop']):
          print("I see him! Should I spare him? Or get the big bucks?")
          the_player['location'] = "VIP room"
    
    #Final win decision
    elif(chosen_command == "take picture"):
        the_player['best picture'] = True
        if(the_player['best picture']):
            print("YES! A GOLDEN SHOT!"
                "\nThis is gonna make BIG bucks!")
            the_player['game status'] = "win"
    
    #Final lose decison
    elif(chosen_command == "get closer"):
        the_player['broken camera'] = True
        if (the_player['broken camera']):
            print("NO!!! My camera was knocked from my hands!"
                "\nIt is broken!")
            the_player['location'] = "restaurant"
            the_player['game status'] = "lose"
    else:
        pass
        
    
# 9) print_game_ending: Print a victory, lose, or quit message at the end
def print_game_ending(the_player):
    print(the_player['game status'])
# Command Paths to give to the unit tester
WIN_PATH = ["visit restaurant", "ask around", "go to VIP room", "take picture"]
LOSE_PATH = ["join crowd", "get closer"]

# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)

# Executes the main function
if __name__ == "__main__":
    '''
    You might comment out the main function and call each function
    one at a time below to try them out yourself '''
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    #print_introduction()
    #print(get_initial_state())
    #print_current_state(the_player)
    # ...