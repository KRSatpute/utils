"""
 generate a strong password of desired length
"""

import string
import random

PASS_LEN = int(raw_input("Password Length: "))
PASSWORD = ''


def randomizer():
    """ randomize characters of ascii letters """
    password_characters = (
        string.ascii_lowercase + string.ascii_uppercase +
        string.digits + string.punctuation
        )
    return "".join(random.choice
                   (
                       password_characters
                   )
                   for _ in range(len(password_characters)))


def password_is_strict(password):
    """ check password strictness """
    lowercase = False
    uppercase = False
    digits = False
    punctuations = False

    for character in password:
        # for every character check if
        if character in string.ascii_lowercase:
            # at least one character is lower[a-z]
            lowercase = True
        elif character in string.ascii_uppercase:
            # at least one character is upper[A-Z]
            uppercase = True
        elif character in string.digits:
            # at least one character is a number[0-9]
            digits = True
        elif character in string.punctuation:
            # at least one character is special character
            # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            punctuations = True
        else:
            return False

    return lowercase and uppercase and\
        digits and punctuations


def generate_password(password_length):
    """ generate strong password """
    # Logic for password strength
    password = ''.join(random.choice
                       (
                           randomizer()
                       ) for _ in range(password_length))
    # Logic for password strictness
    if password_is_strict(password):
        return password
    else:
        return generate_password(password_length)

PASSWORD = generate_password(PASS_LEN)
print PASSWORD
