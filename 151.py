# without 'with' function:
# my_file = open('input.txt', 'r')
# names = my_file.read().splitlines()
# for name in names:
#     print(name)
# my_file.close()

import requests

with open("names.txt", "r") as my_file:  # with = context manager
    names = my_file.read().splitlines()
    for name in names:
        print(name)
with requests.get("https://en.wikipedia.org/wiki/Main_Page") as response:
    response.raise_for_status()
