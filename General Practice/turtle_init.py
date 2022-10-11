import turtle;
import time;
import random;
import traceback;
import pickle;
import os;
import numpy as np;

# def move_player():
#     if player.direction == "up":
#         y_pos = player.ycor();
#         player.sety(y_pos + player_speed);
#     elif player.direction == "down":
#         y_pos = player.ycor();
#         player.sety(y_pos - player_speed);
#     elif player.direction == "right":
#         x_pos = player.xcor();
#         player.setx(x_pos + player_speed);
#     elif player.direction == "left":
#         x_pos = player.xcor();
#         player.setx(x_pos - player_speed);

def move_player():
    if player.direction == "up":
        player.goto(player_x_pos , player_y_pos + player_speed);
    elif player.direction == "down":
        player.goto(player_x_pos ,player_y_pos - player_speed);
    elif player.direction == "right":
        player.goto(player_x_pos + player_speed, player_y_pos );
    else:
        player.goto(player_x_pos  - player_speed,  player_y_pos );

def go_up():
    if player.direction != "down":
        prev_direction = player.direction;
        player.direction = "up";
        curr_direction = player.direction;

        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);


def go_down():
    if player.direction != "up":
        prev_direction = player.direction;
        player.direction = "down"
        curr_direction = player.direction;

        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);

def go_left():
    if player.direction != "right":
        prev_direction = player.direction;
        player.direction = "left";
        curr_direction = player.direction;

        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);

def go_right():
    if player.direction != "left":
        prev_direction = player.direction;
        player.direction = "right";
        curr_direction = player.direction;

        player.tilt(tilt_dict[prev_direction] - tilt_dict[curr_direction]);

def reset_game():
    global GAME_STOPPED;
    global player_high_score;
    
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
        
        player_x_pos = player.xcor();
        player_y_pos = player.ycor();
        
        abs_player_x_pos = abs(player_x_pos);
        abs_player_y_pos = abs(player_y_pos);
        
        move_player();
        
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
