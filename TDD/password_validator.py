def is_password_secure(password):
    # Must be at least 8 characters long
    password_length = len(password)
    
    if password_length < 8:
        return False
    
    return True
