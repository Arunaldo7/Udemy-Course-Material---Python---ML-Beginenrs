#just get the details from the input console
a = input("Hello! Your Name Please...");

#get age as string input itself first
#thus we can explaing different data types once storing as string and checking for age eligibility in IF fails
b = int(input("Thank You ! Now Please Provide Your Age : "));

#check if age is less than 10
#keep only if condition at first
#then write else condition and explain that if not 10 what to display to user

#also try to break indent and show an example
if (b <= 10):
    print("Hello " + a + ". Welcome to Python Game. Your Age " + str(b) + " is within playable limit.");
    print("Enjoy The Game !!!");
else:
    print("Sorry !! Only for Kids !!!");
    
