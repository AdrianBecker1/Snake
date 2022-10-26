from Snake import play, generate_apple, find_snake, grow_snake, move_body
from ui_Snake import ui_print, ui_key,  ui_msg_gameover, play_again, choose_map


# @ -> snake
# A -> apples
# . -> empty spaces
# | and - -> walls


def play_snake ():

    player = True

    ############### loop that runs as long as the player wants to play ###############
    while player:
        
        # Get the map the player wants to play
        map = choose_map()
        
        # list where snake locations are saved
        snake_locations = []

        # starting values
        snake_length = 1
        turns = 0
        grow = False
        game_finished = False

        ########### loop that runs until the player dies #############################
        while not game_finished:
            
            # place an apple if there is none
            generate_apple(map)

            # get the location of the snake and store it in list
            snake_x, snake_y = find_snake(map)
            new_locations = [snake_x, snake_y]
            snake_locations.append(new_locations)

            # add one tile if snake ate an apple
            if grow == True:
                
                snake_length = snake_length + 1
                grow_snake(map, snake_locations, snake_length)

            # Print map ###
            ui_print(map) #
            ###############

            # get the next key
            key = ui_key()

            #######################################################################################
            # move snake
            valid_key, snake_alive, grow = play(map, key)  # the three booleans from play_function

            # move body
            move_body(map, snake_locations, snake_length, turns)
            #######################################################################################

            # add one turn
            turns = turns + 1

            # check if snake dies
            if (not snake_alive) :

                map_gameover = [

                "BBB.BBB.B.B.BBB..BBB.B.B.BBB.BBB",
                "B...B.B.BBB.B....B.B.B.B.B...B.B",
                "B.B.BBB.BBB.BBB..B.B.B.B.BBB.BBB",
                "B.B.B.B.B.B.B....B.B.B.B.B...BB.",
                "BBB.B.B.B.B.BBB..BBB..B..BBB.B.B"
                ]

                ui_print(map_gameover) 
                ui_msg_gameover(snake_length)

                game_finished = True
        
        player = play_again()


###############################
play_snake() # Play Function
###############################