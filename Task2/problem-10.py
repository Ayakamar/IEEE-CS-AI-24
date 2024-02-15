import random

def guessing_game():
    secret_number = random.randint(1, 100)
    while True:
        
        user_input = input("Enter your guess : ")
        
        try:
            user_input = int(user_input)
            
            if user_input>=1 and user_input <=100:
                
                if user_input == secret_number:
                    print("Congratulations! ")
                    break
               
                else:
                    print("Try guessing again.")
            else:
                print("Please enter a number between 1 and 100.")
        
        except ValueError:
            print("Invalid input: Please enter an integer.")

if __name__ == "__main__":
    guessing_game()
