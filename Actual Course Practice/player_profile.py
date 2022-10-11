class PlayerProfile:
    
    age_eligibility = 15;
    def __init__(self):
        
        self.name = input("Hello! Your Name Please...");
        
        self.age = int(input("Thank You ! Now Please Provide Your Age : "));

        self.expertise_level = input("Enter your expertise level : ");

        self.country = input("Enter your country name : ");
        
    
    def check_eligibility(self):
        if (self.age <= self.age_eligibility):
            print(f"Hello {self.name}. Welcome to Python Game. Your Age {self.age} is within playable limit. Your expertise level is {self.expertise_level} . You are from {self.country} country.");
            print("Enjoy The Game !!!");
        else:
            print(f"Sorry {self.name}!! Only for Age below {self.age_eligibility} !!!");