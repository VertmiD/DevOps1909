import datetime
# import mydep
# import my_other_dep
from mydep import test as my_dep_test
from my_other_dep import test as my_other_dep_test
print(datetime.datetime.now())

my_other_dep_test()
my_dep_test()

def wait_for_print():
    from time import sleep
    sleep(3) # in sec.
    print("Hello World")

# TODO: test 123
print("This is the first change after GIT commited")
wait_for_print()
print("Hello World")
