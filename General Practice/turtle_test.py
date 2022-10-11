import turtle;
import random;
import time;
import math;

TILT_DICT = {};
TILT_DICT["up"] = 0;
TILT_DICT["right"] = 90;
TILT_DICT["down"] = 180;
TILT_DICT["left"] = 270;

# def go_up():
#     if player.direction != "down":
#         player.setheading(90)
#         player.direction = "up";
        
# def go_down():
#     if player.direction != "up":
#         player.setheading(270)
#         player.direction = "down";
        
# def go_right():
#     if player.direction != "left":
#         player.setheading(0);
#         player.direction = "right";
        
# def go_left():
#     if player.direction != "right":
#         player.setheading(180);
#         player.direction = "left";

def go_up():
    if player.direction != "down":
        prev_direction = player.direction;
        player.direction = "up";
        curr_direction = player.direction;

        player.tilt(TILT_DICT[prev_direction] - TILT_DICT[curr_direction]);


def go_down():
    if player.direction != "up":
        prev_direction = player.direction;
        player.direction = "down"
        curr_direction = player.direction;

        player.tilt(TILT_DICT[prev_direction] - TILT_DICT[curr_direction]);

def go_left():
    if player.direction != "right":
        prev_direction = player.direction;
        player.direction = "left";
        curr_direction = player.direction;

        player.tilt(TILT_DICT[prev_direction] - TILT_DICT[curr_direction]);

def go_right():
    if player.direction != "left":
        prev_direction = player.direction;
        player.direction = "right";
        curr_direction = player.direction;

        player.tilt(TILT_DICT[prev_direction] - TILT_DICT[curr_direction]);

def move_player():
    player_x_pos = player.xcor();
    player_y_pos = player.ycor();
    
    if player.direction == "up":
        player.goto(player_x_pos , player_y_pos + player_speed);
    elif player.direction == "down":
        player.goto(player_x_pos ,player_y_pos - player_speed);
    elif player.direction == "right":
        player.goto(player_x_pos + player_speed, player_y_pos );
    else:
        player.goto(player_x_pos  - player_speed,  player_y_pos );


def check_player_eats_food():
    if find_distance(player,food) <= (turtle_radius): 
        print("player.distance(food):",player.distance(food));
        return True;
    else:
        return False;
    
def find_distance(point_1, point_2):
    point_1_x = point_1.xcor();
    point_1_y = point_1.ycor();
    
    point_2_x = point_2.xcor();
    point_2_y = point_2.ycor();
    
    distance = pow(pow(point_1_x - point_2_x, 2) + pow(point_1_y - point_2_y, 2), 0.5);
    
    return distance;

def exit_game():
    # print("play_game:",play_game)
    global play_game;
    play_game = False;

screen_width = 500;
screen_height = 500;

screen_width_half = screen_width / 2;
screen_height_half = screen_height / 2;


game_window = turtle.Screen()
game_window.bgcolor("#93A57E");
game_window.title("Python Game");
game_window.tracer(0);
game_window.setup(width = screen_width, height = screen_height);

axis = turtle.Turtle();
axis.penup();
axis.goto(screen_width_half, 0);
axis.pendown();
axis.goto(-screen_width_half, 0);
axis.penup();
axis.goto(0,screen_height_half);
axis.pendown();
axis.goto(0,-screen_height_half);


#player props
player = turtle.Turtle();
player.shape("triangle");
player.color("black");
player.penup();
player.goto(-230, 0);
player.direction = "right";

#set player speed
player_speed = 10;

#food props
food = turtle.Turtle();
food.shape("circle");
food.penup();
food.speed(0);
food.goto(0, 20);

food1 = turtle.Turtle();
food1.shape("circle");
food1.penup();
food1.speed(0);
food1.goto(0, 40);

game_window.listen();
game_window.onkey(go_up, 'Up')
game_window.onkey(go_left, 'Left')
game_window.onkey(go_right, 'Right')
game_window.onkey(go_down, 'Down')
game_window.onkey(exit_game, 'Escape')

play_game = True;

turtle_radius = 20;

delay = 0.1;

pause_game = False;

print("find_distance:",find_distance(player, food));
print("find_distance:",find_distance(player, food1));
print("find_distance:",find_distance(player, axis));

while True:
    game_window.update();
    
print("Game Over")
    
