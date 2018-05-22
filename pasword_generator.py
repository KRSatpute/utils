"""
 Generate a strong password of desired length without repeating any
 characters
"""
import string
import random


def randomizer(password_length):
    """ randomize characters of ascii letters """
    password_characters = (
        string.ascii_lowercase + string.ascii_uppercase +
        string.digits + string.punctuation
        )

    random_chars = "".join(random.choice(password_characters)
                           for _ in range(len(password_characters)))

    passw = ""
    for _ in range(password_length):
        char = random.choice(random_chars)
        random_chars = [c for c in random_chars if c != char]
        passw += char

    return passw


def is_strict_password(password):
    """ check password strictness """
    lowercase = False
    uppercase = False
    digits = False
    punctuations = False

    for character in password:
        # for every character check if
        if (not lowercase) and (character in string.ascii_lowercase):
            # at least one character is lower[a-z]
            lowercase = True
        elif (not uppercase) and (character in string.ascii_uppercase):
            # at least one character is upper[A-Z]
            uppercase = True
        elif (not digits) and (character in string.digits):
            # at least one character is a number[0-9]
            digits = True
        elif (not punctuations) and (character in string.punctuation):
            # at least one character is special character
            # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            punctuations = True

    return lowercase and uppercase and\
        digits and punctuations


def generate_password(password_length):
    """ generate strong password """
    # Logic for password strength
    password = randomizer(password_length)

    # Logic for password strictness
    if not is_strict_password(password):
        password = generate_password(password_length)

    return password


def main():
    """
    Main. Running the code
    """
    pass_len = int(input("Password Length: "))
    print(generate_password(pass_len))


if __name__ == "__main__":
    main()
