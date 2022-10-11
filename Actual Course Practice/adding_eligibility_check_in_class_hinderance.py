from player_profile import PlayerProfile;

player_list = [];

total_players = int(input("Enter Number Of Players"));

for i in range(1, total_players + 1):
    player_list.append(PlayerProfile(i));


#here explain that class need not just be used to store attributes
#it could also be used to do the class/object specific funtions
for i in range(0, total_players):
    if (player_list[i].age <= 15):
        print(f"Hello {player_list[i].name}. Welcome to Python Game. Your Age {player_list[i].age} is within playable limit. Your expertise level is {player_list[i].expertise_level} . You are from {player_list[i].country} country.");
        print("Enjoy The Game !!!");
    else:
        print(f"Sorry {player_list[i].name}!! Only for Age below 15 !!!");
    
