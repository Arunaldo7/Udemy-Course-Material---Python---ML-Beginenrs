#just get the details from the input console
name = input("Hello! Your Name Please...");

age = int(input("Thank You ! Now Please Provide Your Age : "));

#adding more variables so that it gets difficult to track which is which just by name
#as name is just a,b,c...

expertise_level = input("Enter your expertise level : ");

country = input("Enter your country name : ");


if (age <= 15):
    #wantedly interchange c and d so that it demonstrates why it is important to have apt variable names
    print("Hello " + name + ". Welcome to Python Game. Your Age " + str(age) + " is within playable limit." + "Your expertise level is " + expertise_level + 
          ". You are from " + country + " country.");
    print("Enjoy The Game !!!");
else:
    print("Sorry !! Only for Kids !!!");
    
