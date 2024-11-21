# age = int(input("Enter your age: "))
# if 31 < age < 41:
#     print("You are a OK")
#
# years_of_experience = int(input("Enter your years of experience: "))
# if 2 < years_of_experience < 10:
#     print("You have experience")

# def check_in_interval(what_to_ask, min_value, max_value, what_to_print):
#     current_value = int(input(what_to_ask))
#     if min_value < current_value < max_value:
#         print(what_to_print)

def check_in_interval(what_to_ask, min_value, max_value):
    current_value = int(input(what_to_ask))
    if min_value < current_value < max_value:
        return True
    return False

result = check_in_interval("Enter your age: ",
                           0,
                           20)

if result:
    print("Your age was entered correctly")


def square(n):
    print(n * n)

square(5)

check_in_interval("Enter your age: ",
                  0,
                  20)
check_in_interval("Enter your experience: ",
                  2,
                  10)


