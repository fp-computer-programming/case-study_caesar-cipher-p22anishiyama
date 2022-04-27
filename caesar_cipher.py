# Author: ATN 4/27/22

# Imports
from string import ascii_uppercase

original_file = open('alma_mater.txt')
line = original_file.readline().strip()

# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))


def shift_line(line, dict_key):
    new_line = ""
    # Add code here
    return new_line


def encrypt_message(filename, dict_key):
    # Add code here
    pass

# Main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)
