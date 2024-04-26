import numpy as np

def create_matrix():
    while True:
        try:
            # Get the input from the user
            n = int(input("Enter an integer number: "))

        
            if n < 1:
                print("Error: n must be greater than zero.")
                continue  
            #crean an array 
            column = np.arange(1, n + 1)
            
            array = np.ones((n, 1), dtype=int) * column

            return array

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

result = create_matrix()

print(result)
