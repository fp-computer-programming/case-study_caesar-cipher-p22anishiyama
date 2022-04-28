# Author: ATN 4/27/22

# Imports
from string import ascii_uppercase

# Main

# defining the two variables as inputs
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

# opening the text to be accessed
original_file = open('alma_mater.txt')
line = original_file.readline().strip()

# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))


# opening the text as a file and reading the lines
with open(user_file, 'r') as my_file:
    lines = my_file.readlines()
    for x in lines:
        line = x



# translating each line 
def shift_line(line, dict_key):
    new_line = ""
    for x in line:
        for (key, val) in dict_key.items():
            if key == x:
                new_line += x
    return new_line


# appending each line that has been translated to its corresponding area
def encrypt_message(filename, dict_key):

    new_file = open(filename, "w")
    new_file.write(new_line + "\n")
    new_file.close()


key = cipher_key(shift_value)

encrypt_message(user_file, key)
