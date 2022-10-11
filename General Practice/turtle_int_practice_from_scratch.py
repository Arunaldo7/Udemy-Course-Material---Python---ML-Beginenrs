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

def add_player_body(player, player_body):
    body_part = turtle.Turtle();
    body_part.shape("square");
    body_part.color("yellow");
    body_part.penup();
    
    player_body.append(body_part);
    
    if len(player_body) > 1:
        body_part.goto(player_body[-2].xcor() , player_body[-2].ycor());
    else:
        body_part.goto(player.xcor() , player.ycor());

def move_player(player, player_body):
    player_x_pos = player.xcor();
    player_y_pos = player.ycor();
    
    move_body(player_body, player_x_pos, player_y_pos);
    
    if player.direction == "up":
        player.goto(player_x_pos , player_y_pos + player_speed);
    elif player.direction == "down":
        player.goto(player_x_pos ,player_y_pos - player_speed);
    elif player.direction == "right":
        player.goto(player_x_pos + player_speed, player_y_pos );
    else:
        player.goto(player_x_pos  - player_speed,  player_y_pos);
        
def move_body(player_body, player_x_pos, player_y_pos):
    #move all body part except first one
    #move first one to head(player)
    if len(player_body) > 0:
        for i in range(len(player_body) - 1, 0, -1):
            current_body_part = player_body[i];
            next_body_part = player_body[i - 1];
            
            current_body_part.goto(next_body_part.xcor() , next_body_part.ycor());
            
        player_body[0].goto(player_x_pos , player_y_pos);

def check_player_hit_wall(current_abs_player_x_pos, current_abs_player_y_pos):
    if ((current_abs_player_x_pos + turtle_radius) > screen_width_half) or ((current_abs_player_y_pos + turtle_radius) > screen_height_half):
        print("player hit wall - abs_player_x_pos:",current_abs_player_x_pos)
        return True;
    else:
        return False;
    
def check_player_hits_block(player, blocks):
    for block in blocks:
        if find_distance(player,block) < (2 * turtle_radius): 
            return True;
    
    return False;
    
def check_player_eats_food(player, food):
    if find_distance(player,food) <= (2*turtle_radius): 
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

def random_position_generator():
    x_pos = random.randint(-screen_width_half + turtle_radius, screen_width_half - turtle_radius);
    y_pos = random.randint(-screen_height_half + turtle_radius, screen_height_half - turtle_radius);
    
    return x_pos, y_pos;

def random_position_generator_outside_bounding_box(x_length, y_length):
    x_pos = random.randint(-screen_width_half + turtle_radius, screen_width_half - turtle_radius);
    y_pos = random.randint(-screen_height_half + turtle_radius, screen_height_half - turtle_radius);
    
    return x_pos, y_pos;

def exit_game():
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
player.goto(0, 0);
player.direction = "right";

#set player speed
turtle_radius = 10;
player_speed = 15;

#food props
food = turtle.Turtle();
food.shape("circle");
food.color("lightgreen");
food.speed(0);
food.penup();
# food.shapesize(1,1,10)
x_pos, y_pos = random_position_generator();
food.goto(x_pos, y_pos);

game_window.listen();
game_window.onkey(go_up, 'Up');
game_window.onkey(go_left, 'Left');
game_window.onkey(go_right, 'Right');
game_window.onkey(go_down, 'Down');
game_window.onkey(exit_game, 'Escape');

play_game = True;

delay = 0.08;

pause_game = False;

blocks = [];

number_of_blocks = 5;

for i in range(0, number_of_blocks):
    block = turtle.Turtle();
    block.shape("square");
    block.color("red");
    block.penup();
    x_pos, y_pos = random_position_generator();
    block.goto(x_pos, y_pos);
    
    blocks.append(block);
    

player_body = [];

while play_game:
    game_window.update();
    time.sleep(delay);
    
    if not pause_game:
        
        move_player(player, player_body);
        
        current_player_x_pos = player.xcor();
        current_player_y_pos = player.ycor();
        
        current_abs_player_x_pos = abs(current_player_x_pos);
        current_abs_player_y_pos = abs(current_player_y_pos);
        
        if check_player_hit_wall(current_abs_player_x_pos, current_abs_player_y_pos):
            pause_game = True;
            
        if check_player_hits_block(player, blocks):
            pause_game = True;
            
        if check_player_eats_food(player, food):
            add_player_body(player, player_body);
            x_pos, y_pos = random_position_generator();
            food.goto(x_pos, y_pos);
        
print("Game Over");
    
