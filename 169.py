import requests
from time import sleep
try:
    response = requests.get("https://www.goole.com")
except ValueError:
    print("ValueError")
except BaseException as moshe:
    print(f"Somthing went wrong: {moshe.args}")


time_to_sleep = int(input("Time to sleep: "))
sleep(time_to_sleep)

a = int(input("first: "))
b = int(input("second: "))
try:
    res = (a / b)
    print(res)
except ZeroDivisionError:
    print("B cant be 0")

