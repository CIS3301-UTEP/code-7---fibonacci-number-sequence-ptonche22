import re
def check_password(password, level):
    # Check password depending on the level
    if level == 0:
        pattern = r'^\S{8}$' 
    elif level == 1:
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'  
    elif level == 2:
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'  
    elif level == 3:
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'  
    else:
        return False  
    if re.match(pattern, password):
        return True  # Password is valid
    else:
        return False  # Password is not valid

# Main program to test the function
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    user_level = int(input("Enter the level to check (0-3): "))
    
    if check_password(user_password, user_level):
        print(f"Password is valid for Level {user_level}.")
    else:
        print(f"Password is NOT valid for Level {user_level}.")