import re

def is_password_secure(password):
    # Must be at least 8 characters long
    password_length = len(password)
    
    if password_length < 8:
        return False
    
     # Must contain both uppercase and lowercase letters
    upper_case = r'[A-Z]'
    lower_case = r'[a-z]'

    if not re.search(upper_case, password) or not re.search(lower_case, password):
        return False

    # Must contain at least one digit
    digit = r'\d'
    
    if not re.search(digit, password):
        return False

    return True
