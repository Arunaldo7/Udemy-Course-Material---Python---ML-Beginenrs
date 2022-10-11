#just get the details from the input console
a = input("Hello! Your Name Please...");

b = int(input("Thank You ! Now Please Provide Your Age : "));

#adding more variables so that it gets difficult to track which is which just by name
#as name is just a,b,c...

c = input("Enter your expertise level : ");

d = input("Enter your country name : ");


if (b <= 15):
    #wantedly interchange c and d so that it demonstrates why it is important to have apt variable names
    print("Hello " + a + ". Welcome to Python Game. Your Age " + str(b) + " is within playable limit." + "Your expertise level is " + d + ". You are from " + c + " country.");
    print("Enjoy The Game !!!");
else:
    print("Sorry !! Only for Kids !!!");
    
