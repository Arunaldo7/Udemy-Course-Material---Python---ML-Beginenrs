#this is used to create many players
#as this is a multiplayer game each player playing separately each time
#we need to get each player details separately

print("Please enter Player 1 Details");

player_1_name = input("Hello! Your Name Please...");

player_1_age = int(input("Thank You ! Now Please Provide Your Age : "));

player_1_expertise_level = input("Enter your expertise level : ");

player_1_country = input("Enter your country name : ");

print("Please enter Player 2 Details");

player_2_name = input("Hello! Your Name Please...");

player_2_age = int(input("Thank You ! Now Please Provide Your Age : "));

player_2_expertise_level = input("Enter your expertise level : ");

player_2_country = input("Enter your country name : ");

print("Please enter Player 3 Details");

player_3_name = input("Hello! Your Name Please...");

player_3_age = int(input("Thank You ! Now Please Provide Your Age : "));

player_3_expertise_level = input("Enter your expertise level : ");

player_3_country = input("Enter your country name : ");

print("Please enter Player 4 Details");

player_4_name = input("Hello! Your Name Please...");

player_4_age = int(input("Thank You ! Now Please Provide Your Age : "));

player_4_expertise_level = input("Enter your expertise level : ");

player_4_country = input("Enter your country name : ")


if (player_1_age <= 15):
    print(f"Hello {player_1_name}. Welcome to Python Game. Your Age {player_1_age} is within playable limit. Your expertise level is {player_1_expertise_level} . You are from {player_1_country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_1_name}!! Only for Age below 15 !!!");
    
if (player_2_age <= 15):
    print(f"Hello {player_2_name}. Welcome to Python Game. Your Age {player_2_age} is within playable limit. Your expertise level is {player_2_expertise_level} . You are from {player_2_country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_2_name}!! Only for Age below 15 !!!");
    
if (player_3_age <= 15):
    print(f"Hello {player_3_name}. Welcome to Python Game. Your Age {player_3_age} is within playable limit. Your expertise level is {player_3_expertise_level} . You are from {player_3_country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_3_name}!! Only for Age below 15 !!!");
    
if (player_4_age <= 15):
    print(f"Hello {player_4_name}. Welcome to Python Game. Your Age {player_4_age} is within playable limit. Your expertise level is {player_4_expertise_level} . You are from {player_4_country} country.");
    print("Enjoy The Game !!!");
else:
    print(f"Sorry {player_4_name}!! Only for Age below 15 !!!");
    
