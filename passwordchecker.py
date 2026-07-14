#4 conditions
'''1. 5 digits - very weak password'''
'''2. At least one uppercase letter - weak password'''
'''3. At least one lowercase letter - medium password'''
'''4. At least one special character - strong password'''
'''5. At least one digit - moderate password'''
'''if all conditions are satisfied, then the password is valid,
 '''

import re

def check_password_strength(password):
    score=0
    suggestions=[]

    # Check for length
    if len(password) < 5:
        suggestions.append("Password should be at least 5 characters long.")
    else:
        score += 1

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    # Check for special character
    if re.search(r'[_!@#$%^&*()-+]', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    # Check for digit
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Password should contain at least one digit.")

    return score, suggestions

#Main Program

password= input("Enter your password: ")
strength, suggestions= check_password_strength(password)

print("\nPassword Strength: ")

if strength == 5:
    print("Password is very strong. The password is valid")
elif strength >= 4 or strength >= 3:
    print("Password is medium.")
elif strength <= 2:
    print("Password is weak.")
else:
    print("Password is very weak.")

if suggestions:
    print("Suggestions to improve your password:")
    for i in suggestions:
        print(f"- {i}")