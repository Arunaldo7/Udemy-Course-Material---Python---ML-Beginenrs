#this is used to create many players
#as this is a multiplayer game each player playing separately each time
#we need to get each player details separately
from player_profile import PlayerProfile;

player_1 = PlayerProfile();
player_2 = PlayerProfile();
player_3 = PlayerProfile();
player_4 = PlayerProfile();



if (player_1.age <= 15):
    print(f"Hello {player_1.name}. Welcome to Python Game. Your Age {player_1.age} is within playable limit. Your expertise level is {player_1.expertise_level} . You are from {player_1.country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_1.name}!! Only for Age below 15 !!!");
    
if (player_2.age <= 15):
    print(f"Hello {player_2.name}. Welcome to Python Game. Your Age {player_2.age} is within playable limit. Your expertise level is {player_2.expertise_level} . You are from {player_2.country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_2.name}!! Only for Age below 15 !!!");
    
if (player_3.age <= 15):
    print(f"Hello {player_3.name}. Welcome to Python Game. Your Age {player_3.age} is within playable limit. Your expertise level is {player_3.expertise_level} . You are from {player_3.country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_3.name}!! Only for Age below 15 !!!");
    
if (player_4.age <= 15):
    print(f"Hello {player_4.name}. Welcome to Python Game. Your Age {player_4.age} is within playable limit. Your expertise level is {player_4.expertise_level} . You are from {player_4.country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_4.name}!! Only for Age below 15 !!!");
    
