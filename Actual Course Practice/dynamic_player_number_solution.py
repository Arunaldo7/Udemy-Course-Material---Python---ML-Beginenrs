from player_profile import PlayerProfile;

def check_eligibility(player):
    if (player.age <= player.age_eligibility):
        print(f"Hello {player.name}. Welcome to Python Game. Your Age {player.age} is within playable limit. Your expertise level is {player.expertise_level} . You are from {player.country} country.");
        print("Enjoy The Game !!!");
    else:
        print(f"Sorry {player.name}!! Only for Age below {player.age_eligibility} !!!");

player_list = [];

#if the number of players is 4, then we cannot keep on adding below code each time
#this is a hinderance
#so let us configure that also

#first try using range from 1 to 4
#it will take only 3 times
#then explain that the right number in range or list or array in python is always n-1

#initially player profile constriuctore wont take player_number as input
for i in range(1, 5):
    print(f"Enter Details for Player Number {i}");
    player_list.append(PlayerProfile());
    
#first wantedly make it as 4
#do not give total_players in range
#then error "IndexError: list index out of range" pops up when number of players is less than 4
#then give total_players in range
check_eligibility(player_list[0]);
check_eligibility(player_list[1]);
check_eligibility(player_list[2]);
check_eligibility(player_list[3]);

# if (player_list[0].age <= 15):
#     print(f"Hello {player_list[0].name}. Welcome to Python Game. Your Age {player_list[0].age} is within playable limit. Your expertise level is {player_list[0].expertise_level} . You are from {player_list[0].country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_list[0].name}!! Only for Age below 15 !!!");
    
# if (player_list[1].age <= 15):
#     print(f"Hello {player_list[1].name}. Welcome to Python Game. Your Age {player_list[1].age} is within playable limit. Your expertise level is {player_list[1].expertise_level} . You are from {player_list[1].country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_list[1].name}!! Only for Age below 15 !!!");
    
# if (player_list[2].age <= 15):
#     print(f"Hello {player_list[2].name}. Welcome to Python Game. Your Age {player_list[2].age} is within playable limit. Your expertise level is {player_list[2].expertise_level} . You are from {player_list[2].country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_list[2].name}!! Only for Age below 15 !!!");
    
# if (player_list[3].age <= 15):
#     print(f"Hello {player_list[3].name}. Welcome to Python Game. Your Age {player_list[3].age} is within playable limit. Your expertise level is {player_list[3].expertise_level} . You are from {player_list[3].country} country.");
#     print("Enjoy The Game !!!");
# else:
#     print(f"Sorry {player_list[3].name}!! Only for Age below 15 !!!");


