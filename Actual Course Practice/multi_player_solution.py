#this is used to create many players
#as this is a multiplayer game each player playing separately each time
#we need to get each player details separately
from player_profile import PlayerProfile;

player_1 = PlayerProfile();



if (player_1.age <= 15):
    print(f"Hello {player_1.name}. Welcome to Python Game. Your Age {player_1.age} is within playable limit. Your expertise level is {player_1.expertise_level} . You are from {player_1.country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_1.name}!! Only for Age below 15 !!!");
    
# if (player_2_age <= 15):
#     print(f"Hello {player_2_name}. Welcome to Python Game. Your Age {player_2_age} is within playable limit. Your expertise level is {player_2_expertise_level} . You are from {player_2_country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_2_name}!! Only for Age below 15 !!!");
    
# if (player_3_age <= 15):
#     print(f"Hello {player_3_name}. Welcome to Python Game. Your Age {player_3_age} is within playable limit. Your expertise level is {player_3_expertise_level} . You are from {player_3_country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_3_name}!! Only for Age below 15 !!!");
    
# if (player_4_age <= 15):
#     print(f"Hello {player_4_name}. Welcome to Python Game. Your Age {player_4_age} is within playable limit. Your expertise level is {player_4_expertise_level} . You are from {player_4_country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_4_name}!! Only for Age below 15 !!!");
    
