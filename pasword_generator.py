"""
 Generate a strong password of desired length without repeating any
 characters
"""
import string
import random


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


def is_strict_password(password):
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
    if not is_strict_password(password):
        generate_password(password_length)

    return password


def main():
    """
    Main. Running the code
    """
    pass_len = int(raw_input("Password Length: "))
    print generate_password(pass_len)

if __name__ == "__main__":
    main()
