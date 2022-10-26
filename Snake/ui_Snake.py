# Sprites
ui_wall = [
    "######",
    "######",
    "######",
    "######"
]

ui_snake_head = [
    "......",
    ".@..@.",
    "......",
    "......"
]

ui_snake_body = [
    "......",
    "......",
    "......",
    "......"
]


ui_empty = [
    "      ",
    "      ",
    "      ",
    "      "
]

ui_apple = [
    "      ",
    " .--. ",
    " '--' ",
    "      "
]

######################################################################################################################################################################################################

# Function that prints the map
def ui_print(map):
    for row in map:
        for piece in range(4):
            for column in row:
                if column == 'A':
                    print(ui_apple[piece], end='')
                if column == '@':
                    print(ui_snake_head[piece], end='')
                if column == '.':
                    print(ui_empty[piece], end='')
                if column == '-' or column == '|':
                    print(ui_wall[piece], end='')
                if column  == "B":
                    print (ui_snake_body[piece], end='')

            print("")

# Function that gets the key-input from the player
def ui_key():
    key = str(input())

    # check wrong input
    while key != "w" and key != "a" and key != "s" and key != "d":
        key = str(input())

    return key

# Function that shows the gameover screen
def ui_msg_gameover(snake_length):
    print("---")
    print("Game over!")
    final_score = (snake_length -1)*100
    print ("Final Score: " + str(final_score) + " Points")
    print("---")

# Function that asks the player if he would like to play again
def play_again():
    print("Do you want to play again? (Y or N)")
    answer = str(input())
    
    # check for wrong input
    while answer != "Y" and answer != "N":
        print("---")
        print("Please try again:")
        answer = str(input())

    if answer =="Y":
        return True
    else:
        return False

# Function that asks the play which map he would play
def choose_map():

    map_large = [
    "|------------------------------------|",
    "|....................................|",
    "|....................................|",
    "|....................................|",
    "|....................................|",
    "|................@...................|",
    "|....................................|",
    "|....................................|",
    "|....................................|",
    "|....................................|",
    "|....................................|",
    "-------------------------------------|"
    ]

    map_corridor = [
    "|------------------------------------|",
    "|....................................|",
    "|................@...................|",
    "|....................................|",
    "-------------------------------------|"
    ]

    map_small = [
    "|----------|",
    "|..........|",
    "|..........|",
    "|..........|",
    "|..........|",
    "|....@.....|",
    "|..........|",
    "|..........|",
    "|..........|",
    "|..........|",
    "|..........|",
    "|----------|"
    ]

    map_obstacle = [
    "|----------|",
    "|..........|",
    "|..........|",
    "|..--..--..|",
    "|..--..--..|",
    "|....@.....|",
    "|..........|",
    "|..--..--..|",
    "|..--..--..|",
    "|..........|",
    "|..........|",
    "|----------|"
    ]   
    
    print("Welcome to Snake! Please choose your Map-Size:")
    print(" *small* | *obstacle* | *corridor* | *large* ")

    map_nr = str(input())

    # check wrong input
    while map_nr != "small" and map_nr != "obstacle" and map_nr != "corridor" and map_nr != "large":
        print("---")
        print("Please try again!")
        print("---")
        map_nr = str(input())

    if map_nr == "small":
        map = map_small

    elif map_nr == "obstacle":
        map = map_obstacle

    elif map_nr == "corridor":
        map = map_corridor

    elif map_nr == "large":
        map = map_large

        
    return map

