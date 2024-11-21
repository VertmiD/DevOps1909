from venv import create
from pathlib import Path


# Assignment #1+2:
try:
    a = 1 / 0
    print("1. The answer is :", a)
except:
    print("1. Cannot divide by zero")

# Assignment #3:
# The code is legal but there is only a "try" block and regardless of its success the "finally" block will be performed.

# Assignment #4:
# Except can handel all exceptions to a "try" block.

# Assignment #5:
# The exception handler above is general type of exception without testing particular exception.

# Assignment #6:
# except IOError: handle with wrong files, writing, or reading from files.
# except ZeroDivisionError handle zero value division.

# Assignment #7:
try:
    with open("words.txt", "x") as my_file:
        print("7. The file ", my_file.name, " created")
except FileExistsError:
    print("7. File still exists!")
    user_choice = input("Do you want to delete the old content from file? (y/n): ")
    if user_choice.lower() == 'y':
        user_choice = "w"
    else:
        user_choice = "a"
# Assignment #8:
with open("words.txt", user_choice) as my_file:
    content = input("8. Please enter your name: ")
    my_file.write(content+"\n")

# Assignment #9:
def read_file():
    with open("words.txt", "r", encoding="utf-8") as my_file:
        contents = my_file.read().splitlines()
        for line in contents:
            print(line)
print("9. File output: ")
read_file()

# Assignment #10:
with open('words.txt', "a", encoding="utf-8") as my_file:
    HEB_content = input("10. Please enter somthing in Hebrew: ")
    my_file.write(HEB_content+"\n")

print("-> File output: ")
read_file()