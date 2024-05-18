"""
Generate a strong password of desired length without repeating any characters.

Password requirements:
    - Should contain at least one lowercase letter
    - Should contain at least one uppercase letter
    - Should contain at least one digit 0-9
    - Should contain at least one special or user defined character !#$%&()*+,-.:;<=>?@[]^_`{|}~

Example:
    >>> Password Length: 12
    >>> Provide Special Characters (optional):
    >>> A#v!10_kJzxL
    >>> Password Length: 14
    >>> Provide Special Characters (optional): &*#@()
    >>> F4fEyR(m50DxJ#

.. module:: password_generator
   :platform: Unix, Windows
   :synopsis: This module provides functions to generate strong passwords.

.. moduleauthor:: Kshitij Satpute <kshitij_satpute@live.com>

"""

import string
import random


def generate_password(
    password_length: int, special_chars: str = "!#$%&()*+,-.:;<=>?@[]^_`{|}~"
) -> str:
    """
    Generate a strong password of the given length without repeating any
    characters.

    :param password_length: The desired length of the password.
    :param special_chars: User defined special characters.

    :return: The generated password.
    """
    if not special_chars:
        special_chars = "".join(c for c in string.punctuation if c not in "\\/\"'")

    password_characters: str = string.ascii_letters + string.digits + special_chars
    password: str = "".join(random.sample(password_characters, password_length))

    # Check if the generated password meets the strict password requirements.
    while not __is_strict_password(password, special_chars):
        password = generate_password(password_length)

    return password


def __is_strict_password(password: str, special_chars: str) -> bool:
    """
    Check if a given password meets the strict password requirements.

    Password requirements:
    - Should contain at least one lowercase letter
    - Should contain at least one uppercase letter
    - Should contain at least one digit `(0-9)`
    - Should contain at least one special or user defined character !#$%&()*+,-.:;<=>?@[]^_`{|}~

    :param password: The password to be checked.
    :param special_chars: User defined special characters.

    :return: True if the password meets the requirements, False otherwise.
    :rtype: bool
    """
    lowercase: bool = any(char.islower() for char in password)
    uppercase: bool = any(char.isupper() for char in password)
    digits: bool = any(char.isdigit() for char in password)
    special_characters: bool = any(char in special_chars for char in password)
    return lowercase and uppercase and digits and special_characters


def main() -> None:
    """
    The main function that prompts the user for the desired password length
    and optional user defined special characters.
    Generates a strong password satisfying the strict password requirements.

    Password requirements:
    - Password length >=8, <=18
    - Should contain at least one lowercase letter
    - Should contain at least one uppercase letter
    - Should contain at least one digit 0-9
    - Should contain at least one special or user defined character !#$%&()*+,-.:;<=>?@[]^_`{|}~

    Example:
        >>> Password Length: 12
        >>> Provide Special Characters (optional):
        >>> A#v!10_kJzxL
        >>> Password Length: 14
        >>> Provide Special Characters (optional): &*#@()
        >>> F4fEyR(m50DxJ#
    """
    print("Password requirements:")
    print("- Should contain at least one lowercase letter")
    print("- Should contain at least one uppercase letter")
    print("- Should contain at least one digit 0-9")
    print(
        "- Should contain at least one special character !#$%&()*+,-.:;<=>?@[]^_`{|}~"
    )

    pass_len: int = int(input("Password Length (8-18): "))

    if pass_len < 8 or pass_len > 18:
        print("Password length should be >=8 and <=18")

        # Re-prompt the user for the password length.
        pass_len = int(input("Password Length (8-18), Ctrl+C to exit: "))

    special_chars = input("Provide Special Characters (optional): ")
    password: str = generate_password(pass_len, special_chars)
    print(password)


if __name__ == "__main__":
    main()
