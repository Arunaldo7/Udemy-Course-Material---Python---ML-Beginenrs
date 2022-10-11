#this is used to create many players
#as this is a multiplayer game each player playing separately each time
#we need to get each player details separately
from player_profile import PlayerProfile;

player_list = [];


#first try using range from 1 to 4
#then in PlayerProfile init method it will slow enter player number from 0
#so, then explain that range need not start from 0, it can start from any number unless we are referring to some indexed variables(like List, arrays)
for i in range(1, 5):
    player_list.append(PlayerProfile());


if (player_list[0].age <= 15):
    print(f"Hello {player_list[0].name}. Welcome to Python Game. Your Age {player_list[0].age} is within playable limit. Your expertise level is {player_list[0].expertise_level} . You are from {player_list[0].country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_list[0].name}!! Only for Age below 15 !!!");
    
if (player_list[1].age <= 15):
    print(f"Hello {player_list[1].name}. Welcome to Python Game. Your Age {player_list[1].age} is within playable limit. Your expertise level is {player_list[1].expertise_level} . You are from {player_list[1].country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_list[1].name}!! Only for Age below 15 !!!");
    
if (player_list[2].age <= 15):
    print(f"Hello {player_list[2].name}. Welcome to Python Game. Your Age {player_list[2].age} is within playable limit. Your expertise level is {player_list[2].expertise_level} . You are from {player_list[2].country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_list[2].name}!! Only for Age below 15 !!!");
    
if (player_list[3].age <= 15):
    print(f"Hello {player_list[3].name}. Welcome to Python Game. Your Age {player_list[3].age} is within playable limit. Your expertise level is {player_list[3].expertise_level} . You are from {player_list[3].country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_list[3].name}!! Only for Age below 15 !!!");
    
