"""
Generate a strong password of desired length without repeating any characters.

.. module:: password_generator
   :platform: Unix, Windows
   :synopsis: This module provides functions to generate strong passwords.

.. moduleauthor:: Your Name <your.email@example.com>

"""

import string
import random


def generate_password(password_length):
    """
    Generate a strong password of the given length without repeating any
    characters.

    :param password_length: The desired length of the password.
    :type password_length: int
    :return: The generated password.
    :rtype: str
    """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(password_characters, password_length))
    return password


def is_strict_password(password):
    """
    Check if a given password meets the strict password requirements.

    :param password: The password to be checked.
    :type password: str
    :return: True if the password meets the requirements, False otherwise.
    :rtype: bool
    """
    lowercase = any(char.islower() for char in password)
    uppercase = any(char.isupper() for char in password)
    digits = any(char.isdigit() for char in password)
    punctuations = any(char in string.punctuation for char in password)
    return lowercase and uppercase and digits and punctuations


def main():
    """
    The main function that prompts the user for the desired password length
    and generates a strong password satisfying the strict password requirements
    """
    pass_len = int(input("Password Length: "))
    password = generate_password(pass_len)
    while not is_strict_password(password):
        password = generate_password(pass_len)
    print(password)


if __name__ == "__main__":
    main()
