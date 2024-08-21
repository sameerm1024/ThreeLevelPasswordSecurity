import getpass
from PIL import Image

def level_one_password():
    correct_password = "PasswordisKey"
    attempts = 3
    
    while attempts > 0:
        password = getpass.getpass("Enter your password: ")
        if password == correct_password:
            print("Password correct!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.")
    
    return False

def level_two_graphical():
    correct_pattern = "43210"
    pattern = input("First 5 whole numbers in reverse: ")
    
    if pattern == correct_pattern:
        print("Graphical password correct!")
        return True
    else:
        print("Incorrect graphical password.")
        return False

def level_three_security_question():
    correct_answer = "MyFirstPet"
    answer = input("What was the name of your first pet? ")
    
    if answer == correct_answer:
        print("Security question correct!")
        return True
    else:
        print("Incorrect answer.")
        return False

def three_level_authentication():
    if not level_one_password():
        print("Failed at Level 1.")
        return False
    
    if not level_two_graphical():
        print("Failed at Level 2.")
        return False
    
    if not level_three_security_question():
        print("Failed at Level 3.")
        return False
    
    print("Authentication successful!")
    return True


three_level_authentication()
