user_input = input("Enter your input: ")

try:
    user_input = int(user_input)
    print( user_input,"is an accepted value")
except ValueError:
    print("Invalid input: Please enter an integer.")
