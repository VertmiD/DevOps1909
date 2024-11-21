e = [1,2,3,4,5,6,7,8,9,10]
f = []
ee = ""
if not ee:
    print("ee empty")
if len(e) > 8:
    print("Enough items in the list")

if e:
    print("e is not empty")

if not f:
    print("f is empty")

# "in" operation
names = ["Vladi" , "Diana" , "Otir" , "Ofir"]
if "Otir" in names:
    print("Otir is in the list")
else:
    print("Otir is not in the list")

# Type of variable
if e is list:
    print("e is a list")
else:
    print("e is not a list")

if type(e) is list:
    print("e is a list 2")

print("e is a ", type(e))

if isinstance(e, list):
    print("e is a list 3")





