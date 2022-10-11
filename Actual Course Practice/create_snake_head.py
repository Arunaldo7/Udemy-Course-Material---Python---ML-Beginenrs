import turtle;
import time;

game_window = turtle.Screen();
game_window.setup(width = 500, height = 500);
game_window.bgcolor("black");

#create player
player = turtle.Turtle();
player.color("blue");
player.shape("triangle");

while True:
    game_window.update();
    
    
