import random 
import string

def create_a_password():
     char = string.ascii_letters + string.digits

     password = ""
     has_uppercase = False
     has_lowercase = False
     has_digit = False
     
     for _ in range(8):
        character = random.choice(char)
        password += character
        if character in string.ascii_uppercase:
             has_uppercase = True
        elif character in string.ascii_lowercase:
             has_lowercase = True
        elif character in string.digits:
             has_digit = True

     if has_uppercase and has_lowercase and has_digit:
          return password
     else:
          return create_a_password()

result = create_a_password()  
print("Generated Password:", result)
 

