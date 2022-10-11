#this is used to create many players
#as this is a multiplayer game each player playing separately each time
#we need to get each player details separately
from player_profile import PlayerProfile;

def check_eligibility(player):
    if (player.age <= player.age_eligibility):
        print(f"Hello {player.name}. Welcome to Python Game. Your Age {player.age} is within playable limit. Your expertise level is {player.expertise_level} . You are from {player.country} country.");
        print("Enjoy The Game !!!");
    else:
        print(f"Sorry {player.name}!! Only for Age below {player.age_eligibility} !!!");

player_list = [];

total_players = int(input("Enter Number Of Players"));

#first try using range from 0 to total_players,
#then in PlayerProfile init method it will slow enter player number from 0
#so, then explain that range need not start from 0, it can start from any number unless we are referring to some indexed variables(like List, arrays)
for i in range(1, total_players + 1):
    player_list.append(PlayerProfile(i));

#wantedly give range 2nd argument as 3, it will only ask 3 times
#then explain in python, the second argument we give for list/range it will take only n-1 number
for i in range(0, total_players):
    if (player_list[i].age <= 15):
        print(f"Hello {player_list[i].name}. Welcome to Python Game. Your Age {player_list[i].age} is within playable limit. Your expertise level is {player_list[i].expertise_level} . You are from {player_list[i].country} country.");
        print("Enjoy The Game !!!");
    else:
        print(f"Sorry {player_list[i].name}!! Only for Age below 15 !!!");
    
