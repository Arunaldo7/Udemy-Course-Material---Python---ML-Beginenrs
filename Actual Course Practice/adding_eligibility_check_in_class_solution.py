from player_profile import PlayerProfile;

player_list = [];

total_players = int(input("Enter Number Of Players"));

for i in range(1, total_players + 1):
    player_list.append(PlayerProfile(i));

PlayerProfile.age_eligibility = 40;

#here explain that class need not just be used to store attributes
#it should also be used to do the class/object specific funtions

#first add this method check_eligibility in current file
#then add it inside class thus explaining what is a method and then using it inside class

for i in range(0, total_players):
    player_list[i].check_eligibility();