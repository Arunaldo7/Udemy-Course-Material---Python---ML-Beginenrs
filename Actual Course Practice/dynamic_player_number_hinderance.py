from player_profile import PlayerProfile;

player_list = [];

#if the number of players is dynamic, then we cannot keep on adding below code each time
#this is a hinderance
#so let us configure that also

#And also in the player input, it does not ask for which player number,
#so we improve that also in solution
player_list.append(PlayerProfile());
player_list.append(PlayerProfile());
player_list.append(PlayerProfile());
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


