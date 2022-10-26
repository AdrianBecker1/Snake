import random
from ui_Snake import ui_print, ui_key

# this function returns two booleans
# the first indicates whether the pressed key was a valid key
# the second indicates whether the snake is still alive
# the third indicates if the snake ate an apple
def play(map, key):
    next_x, next_y = next_position(map, key)  #get the new position

    # check if input is a invalid key
    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key == True:
        return False, True, False  # No movement , Game continues, no apple eaten

    # check if Snake is not within borders
    if not within_borders(map, next_x, next_y) == True:
        return False, False, False  # No movement , Game Finishes, no apple eaten

    # check if snake is inside a wall
    if is_a_wall(map, next_x, next_y) == True:
        return False, False, False  # No movement , Game Finishes, no apple eaten
    
    # check if snake ate herself
    if is_body(map, next_x, next_y) == True:
        return False, False, False  # No movement , Game Finishes, no apple eaten

    # check if the snake ate an apple and move
    if is_a_apple(map, next_x, next_y) == True:
        move_snake(map, next_x, next_y)
        return True, True, True  # Movement, Game continues,  apple eaten 

    # move snake ####################
    move_snake(map, next_x, next_y) #
    #################################

    
    return True, True, False  # Movement, Game continues, no apple eaten

######################################################################################################################################################################################################

# Function that moves the rest of the sanke after the head moved
def move_body(map, snake_locations, snake_length, turns):
    
    # for loop that iterates through the snake body parts
    for body_part_nummer in range(snake_length):
        
        # exits the move_body function once the head is reached which has alredy been moved
        if body_part_nummer == snake_length-1:
            return
        
        # get the coordinates where the body is
        body_coordinates = snake_locations[turns - body_part_nummer -1] 
    
        x_body_coordinates = body_coordinates[0]
        y_body_coordinates = body_coordinates[1]

        # ...and where it will be after the next turn
        next_body_coordinates = snake_locations[turns - body_part_nummer] 

        x_next_body_coordinates = next_body_coordinates[0]
        y_next_body_coordinates = next_body_coordinates[1]

        # move body ########################################################################################################
        move_entities (map, x_body_coordinates, y_body_coordinates, x_next_body_coordinates, y_next_body_coordinates, "B") #
        ####################################################################################################################

######################################################################################################################################################################################################

# function that moeves the snake head
def move_snake(map, next_snake_x, next_snake_y):
    snake_x, snake_y = find_snake(map)

    # move snake head ######################################################
    move_entities (map, snake_x, snake_y, next_snake_x, next_snake_y, "@") #
    ########################################################################

# Finds the location of Snake on the map
def find_snake(map):
    snake_x = -1
    snake_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                snake_x = x
                snake_y = y

    return snake_x, snake_y

# Calaculates the next postion of snake
def next_position(map, key):
    x, y = find_snake(map)
    next_x = -1
    next_y = -1

    if key == 'a':
        next_x = x
        next_y = y - 1
    elif key == 'd':
        next_x = x
        next_y = y + 1
    elif key == 'w':
        next_x = x - 1
        next_y = y
    elif key == 's':
        next_x = x + 1
        next_y = y

    return next_x, next_y

# Move function for body and head (B & @) #
def move_entities(map, x, y, next_x, next_y, symbol): # symbol = @ or = B

     # the place where the entity was is now empty
    everything_to_the_left = map[x][0:y]
    everything_to_the_right = map[x][y+1:]
    map[x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the entity
    everything_to_the_left = map[next_x][0:next_y]
    everything_to_the_right = map[next_x][next_y+1:]
    map[next_x] = everything_to_the_left + str(symbol) + everything_to_the_right

######################################################################################################################################################################################################

# Functions that check the map for certain objects

def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == '|' or map[next_x][next_y] == '-'
    return is_a_wall

def is_a_apple(map, next_x, next_y):
    is_a_apple = map[next_x][next_y] == 'A'
    return is_a_apple

def is_snake(map, next_x, next_y):
    is_snake = map[next_x][next_y] == '@'
    return is_snake

def is_body(map, next_x, next_y):
    is_body = map[next_x][next_y] == 'B'
    return is_body

# Function that checks if snake is inside
def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns

    return x_is_valid and y_is_valid # Returns True or False

######################################################################################################################################################################################################

# generates an apple
def generate_apple(map):

    # if there is no apple, a new one gets created
    apple_generated = check_apple(map)


    if apple_generated == False:

        while apple_generated == False:
            
            #randomly create a position on the map
            x_random = random.randint(1, len(map)-1)
            y_random = random.randint(1, len(map[x_random])-1)

            # check if apple can be placed here
            if map[x_random][y_random] == '.':

                # and replace empty space with apple
                everything_to_the_left = map[x_random][0:y_random]
                everything_to_the_right = map[x_random][y_random+1:]
                map[x_random] = everything_to_the_left + "A" + everything_to_the_right
                return
    
    else:

        return

# checks if there is an apple (True: There is one, False: There is none)
def check_apple(map):

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'A':
                return True
    
    return False

# add a tile to the snake
def grow_snake(map,snake_locations,snake_length):
    
    
    coordinates = snake_locations[(len(snake_locations)-snake_length)]

    x_coordinates = coordinates[0]
    y_coordinates = coordinates[1]

    # place body
    everything_to_the_left = map[x_coordinates][0:y_coordinates]
    everything_to_the_right = map[x_coordinates][y_coordinates+1:]
    map[x_coordinates] = everything_to_the_left + "B" + everything_to_the_right

