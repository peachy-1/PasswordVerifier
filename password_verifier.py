##############################
# Password Strength Verifier #
##############################

###############################################################
# Notes : a rating of '10' is 'Very Good', '1' is 'Poor'
#
#   - At least 8 characters (+1 rating)
#   - Contains a special character ( !, $, @, #, or %) (+3 rating)
#   - Contains a number (+1 rating)
#   - Contains a uppercase letter (+1 rating)
#   - Contains a lowercase letter (+ 1 rating)
#   - Contains a white space (+3 rating)
#
#   Password will not exceed 20 characters
###############################################################

def password_strength(password):

    symbols = [ '!', '$', '@', '#', '%' ]
    rating = 0

    # Check the password length; should be between 8 and 20
    if len(password)in range (8, 21):
        rating += 1
        # Check for a uppercase letter
        if any(char.isupper() for char in password):
            rating += 1
        # Check for a lowercase letter
        if any(char.islower() for char in password):
            rating += 1
        # Check for a number
        if any(char.isdigit() for char in password):
            rating += 1
        # Check for white space
        if any(char == ' ' for char in password):
            rating += 3
        # Check for symbols
        if any(char in symbols for char in password):
            rating += 3
    else:
        rating = 0

    return rating
    
    