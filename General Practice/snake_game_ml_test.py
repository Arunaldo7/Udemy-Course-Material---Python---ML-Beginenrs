import turtle;
import time;
import random;
import traceback;
import pickle;
import os;
import numpy as np;
import pandas as pd;

def capture_game_state(current_direction, new_direction):
    global game_state_list;
    
    game_state_dict = {};
    
    player_pos_x = player.xcor();
    player_pos_y = player.ycor();
    
    #capture player stats
    # game_state_dict["player_pos_x"] = player_pos_x;
    # game_state_dict["player_pos_y"] = player_pos_y
    game_state_dict["player_move_direction"] = current_direction;
    
    #reward stats
    # game_state_dict["food_pos_x"] = food.xcor();
    # game_state_dict["food_pos_y"] = food.ycor();
    
    #relative reward player pos
    food_player_x_pos_diff = player_pos_x - food.xcor();
    food_player_y_pos_diff = player_pos_y - food.ycor();
    
    game_state_dict["food_player_x_pos_diff"] = food_player_x_pos_diff;
    game_state_dict["food_player_y_pos_diff"] = food_player_y_pos_diff
    
    #distance stats
    game_state_dict["player_food_distance"] = round(player.distance(food));
    
    #to calc wall distance we need to see which direction player faces
    if current_direction == "up":
        player_wall_distance = screen_height_half - player_pos_y;
    elif current_direction == "down":
        player_wall_distance = abs(-screen_height_half - player_pos_y);
    elif current_direction == "left":
        player_wall_distance = abs(-screen_width_half - player_pos_x);
    elif current_direction == "right":
        player_wall_distance = screen_width_half - player_pos_x;
        
    game_state_dict["player_wall_distance"] = player_wall_distance
    
    #action
    game_state_dict["new_direction"] = new_direction;
    
    game_state_list.append(game_state_dict);

def move_player():
    if player.direction == "up":
        y_pos = player.ycor();
        player.sety(y_pos + player_speed);
    elif player.direction == "down":
        y_pos = player.ycor();
        player.sety(y_pos - player_speed);
    elif player.direction == "right":
        x_pos = player.xcor();
        player.setx(x_pos + player_speed);
    elif player.direction == "left":
        x_pos = player.xcor();
        player.setx(x_pos - player_speed);


def go_up():
    if player.direction != "down":
        prev_direction = player.direction;
        
        #capture state before player changes direction
        capture_game_state(prev_direction, "up");
        
        player.direction = "up";
        curr_direction = player.direction;
        
        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);


def go_down():
    if player.direction != "up":
        prev_direction = player.direction;
        
        #capture state before player changes direction
        capture_game_state(prev_direction, "down");
        
        player.direction = "down"
        curr_direction = player.direction;
        
        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);

def go_left():
    if player.direction != "right":
        prev_direction = player.direction;
        
        #capture state before player changes direction
        capture_game_state(prev_direction, "left")
        
        player.direction = "left";
        curr_direction = player.direction;

        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);

def go_right():
    if player.direction != "left":
        prev_direction = player.direction;
        
        #capture state before player changes direction
        capture_game_state(prev_direction, "right")
        
        player.direction = "right";
        curr_direction = player.direction;
        
        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);

def reset_game():
    global GAME_STOPPED;
    global player_high_score;
    global game_state_list;
    
    time.sleep(0.5);
    
    GAME_STOPPED = True;
    
    player_scores_list.append(player_score);
    
    if player_score > player_high_score:
        player_high_score = player_score;
        
        if os.path.exists(player_stats_file):
            player_stats = pickle.load(open(player_stats_file, "rb"));
        else:
            player_stats = {};
            
        player_stats["player_scores_list"] = player_scores_list;
        player_stats["player_high_score"] = player_high_score;    
        pickle.dump(player_stats, open(player_stats_file, "wb"))

    score_card.clear();

    score_card.write(f"Score : {player_score} High Score : {player_high_score}", align="center",
                    font=("candara", 24, "bold"));
    
    for segment in player_body:
        segment.goto(2 * screen_width, 2 * screen_height);
        del segment;
    player_body.clear();
    
    #resetting player position    
    player_speed = 0;
    player.speed(player_speed);
    player.goto(0,0);
    
    prev_direction = player.direction;
    player.direction = "right";
    curr_direction = player.direction;

    player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);
    
    #remove last action as it leads to game end
    game_state_list = game_state_list[0 : -1];
    
    print("game_state_list:",game_state_list);


def toggle_pause_resume():
    global GAME_PAUSED;
    global GAME_STOPPED;
    
    global player_score;
    global player_high_score;
    global score_card;
    global player_speed;
    
    
    if GAME_STOPPED:
        GAME_STOPPED = False;
        GAME_PAUSED = False;
        
        player_score = 0;
        
        score_card.clear()

        score_card.write(f"Score : {player_score} High Score : {player_high_score}", align="center",
                            font=("candara", 24, "bold"));
    else:
        GAME_PAUSED = not GAME_PAUSED;
    
    if GAME_PAUSED:
        player_speed = 0;
        player.speed(player_speed);
        for pause_symbol_object in pause_symbol:
            pause_symbol_object.showturtle();
            
        print("Game Paused");
    else:
        player_speed = playable_player_speed;
        player.speed(player_speed);

        for pause_symbol_object in pause_symbol:
            pause_symbol_object.hideturtle();
            
        print("Game Resumed")
            
def exit_game():
    global RUN;
    RUN = False;
    turtle.bye();
    
    game_state_dataset = pd.DataFrame(game_state_list);
    game_state_dataset.to_excel("game_state_dataset.xlsx", index = False);
    
    
    print("game_state_list:", game_state_list)

screen_width = 500;
screen_height = 500;

screen_width_half = screen_width / 2;
screen_height_half = screen_height / 2;

GAME_STOPPED = False;
GAME_PAUSED = False;

delay = 0.1;

playable_player_speed = 20;
paused_player_speed = 0;

player_speed = playable_player_speed;

player_stats_file = "player_stats.pkl"

player_score = 0;

game_state_list = [];

if os.path.exists(player_stats_file):
    player_stats = pickle.load(open(player_stats_file, "rb"));
    
    player_scores_list = player_stats["player_scores_list"];
    player_high_score = player_stats["player_high_score"];
else:
    player_high_score = 0;
    player_scores_list = [];

food_size = 1;
food_points = 10;

tilt_dict = {};
tilt_dict["up"] = 0;
tilt_dict["right"] = 90;
tilt_dict["down"] = 180;
tilt_dict["left"] = 270;

try:
    # Creating a window screen
    game_window = turtle.Screen();
    game_window.title("Feed the Turtle");
    game_window.bgcolor("blue");

    # the width and height can be put as user's choice
    game_window.setup(width = screen_width, height = screen_height);
    game_window.tracer(0);

    # head of the snake
    player = turtle.Turtle();
    player.shape("triangle");
    player.color("black");
    player.penup();
    player.goto(0, 0);
    player.direction = "right";

    # food in the game
    food = turtle.Turtle();
    food.speed(0);
    food.shape("circle");
    food.color("red");
    food.penup();
    food.goto(0, screen_height_half / 2);
    

    #score card properties
    score_card = turtle.Turtle();
    score_card.speed(0);
    score_card.shape("square");
    score_card.color("white");
    score_card.penup();
    score_card.hideturtle();
    score_card.goto(0, screen_height_half - 50);
    score_card.write(f"Score : {player_score} High Score : {player_high_score}", align="center",
                     font=("candara", 24, "bold"));

    #pause symbol
    pause_symbol = [];

    pause_symbol_width = 0.5;
    pause_symbol_height = 2;
    

    for i in range(1,3):
        pause_symbol_object = turtle.Turtle();
        pause_symbol_object.speed(0);
        pause_symbol_object.shape("square");
        pause_symbol_object.color("white");  # tail colour
        pause_symbol_object.penup();
        pause_symbol_object.shapesize(pause_symbol_height, pause_symbol_width)
        pause_symbol_object.goto(screen_width_half - (i * 25), screen_height_half - 30);
        pause_symbol_object.hideturtle();
        pause_symbol.append(pause_symbol_object);

    
    #blocks
    block_list = [];
    
    num_of_blocks = 3;
    block_min_height = 5;
    block_max_height = 10;
    
    block_min_width = 0.7;
    block_max_width = 1.5;
    
    # for i in range(1, num_of_blocks + 1):
    #     block_width = random.choice(np.arange(block_min_width, block_max_width, 0.1));
    #     block_height = random.choice(np.arange(block_min_height, block_max_height, 0.5));
        
    #     rand_pos_x = random.randint(- screen_width_half , screen_width_half);
    #     rand_pos_y = random.randint(- screen_height_half, screen_height_half);
        
    #     block_object = turtle.Turtle();
    #     block_object.speed(0);
    #     block_object.shape("square");
    #     block_object.color("white");  # tail colour
    #     block_object.penup();
        
    #     block_object.shapesize(block_height, block_width);
    #     print("width:", block_object.width);
    #     # print("height:", block_object.height);
    #     block_object.goto(rand_pos_x, rand_pos_y);
    #     # block_object.hideturtle();
    #     block_list.append(block_object);    

    game_window.listen()
    game_window.onkeypress(go_up, "Up");
    game_window.onkeypress(go_down, "Down");
    game_window.onkeypress(go_right, "Right");
    game_window.onkeypress(go_left, "Left");
    game_window.onkeypress(exit_game, "Escape");
    game_window.onkeypress(toggle_pause_resume, "space");


    RUN = True;
    
    player_body = [];

    print("GAME_PAUSED:", GAME_PAUSED);
    
    while RUN:
        game_window.update();
        if (not GAME_PAUSED) and (not GAME_STOPPED) :
            if player.distance(food) < playable_player_speed:
                #move food to different position
                food_pos_x = random.randint(-(screen_width_half - 10),
                                            screen_width_half - 10);
                food_pos_y = random.randint(-(screen_width_half - 10),
                                            screen_height_half - 10);

                food.goto(food_pos_x, food_pos_y);

                new_segment = turtle.Turtle();
                new_segment.speed(0);
                new_segment.shape("square");
                new_segment.color("grey");  # tail colour
                new_segment.penup();
                player_body.append(new_segment);
                player_score = player_score + food_points;

                score_card.clear();

                score_card.write(f"Score : {player_score} High Score : {player_high_score}", align="center",
                        font=("candara", 24, "bold"));



            #for other than 0th segment of player body, move those segments to end of each segment
            for i in range(len(player_body) - 1, 0, -1):
                prev_segment_x_pos = player_body[i - 1].xcor();
                prev_segment_y_pos = player_body[i - 1].ycor();

                player_body[i].goto(prev_segment_x_pos, prev_segment_y_pos);

            if len(player_body) > 0:
                x = player.xcor();
                y = player.ycor();
                player_body[0].goto(x, y);

            move_player();
        
            player_pos_x_abs = abs(player.xcor());
            player_pos_y_abs = abs(player.ycor());
            
            #check for game over
            if (player_pos_x_abs >= screen_width_half) or (player_pos_y_abs >= screen_height_half):
                print("Player Hit Wall");
                reset_game();
            else:
                for segment in player_body:
                    if segment.distance(player) < playable_player_speed:
                        print("Player hit own body");
                        reset_game();
                        
                for block_object in block_list:
                    if block_object.distance(player) < playable_player_speed:
                        print("Player hit block");
                        reset_game();
                        
            time.sleep(delay);
except Exception:
    traceback.print_exc();
    # turtle.bye()
