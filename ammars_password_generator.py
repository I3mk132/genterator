# imports
import random
import string

def user_question():
    while True:
        min_length = input("What is the minimum length of the password you want to make?")
        if min_length.isdigit():
            min_length = int(min_length)
            break
        else:
            print('please enter a number ')
    while True:
        max_length = input("What is the maximum length of the password you want to make?")
        if max_length.isdigit():
            max_length = int(max_length)
            break
        else:
            print('please enter a number ')
    while True:
        has_numbers = input("Do you want numbers in the password? (yes/no)").lower()
        if has_numbers == "yes":
            has_numbers = True
            break

    while True:
        has_special = input("Do you want special characters in the password? (yes/no)").lower()
        if has_special == "yes":
            has_special = True
            break
    return min_length, max_length, has_numbers, has_special




def password_generation(min_length, max_length, has_numbers=False, has_special_numbers=False):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    character = letters

    if has_numbers:
        character += numbers
    if has_special_numbers:
        character += special

    pwd = ""
    pass_length = random.randint(min_length, max_length)
    for _ in range(pass_length):
        char = random.choice(character)
        pwd += char

    return pwd

q_min, q_max, q_numbers, q_special = user_question()
passowrd = password_generation(q_min, q_max, q_numbers, q_special)
print("your password is: ", passowrd)