for i in range(101):
    if i%7 == 0 or '7' in str(i):
        continue
    else:
        print(i)

result = [i for i in range(1,101) if i % 7 != 0 and '7' not in str(i)]
print(result)

names = ["natan", "shay", "ronen", "aharon"]
result = [name for name in names if "n" in name]
print(result)

names = ["natan", "shay", "ronen", "aharon"]
result = [name.upper() for name in names if "n" in name]
print(result)

names = ["natan", "shay", "ronen", "aharon"]
result = [name.capitalize() for name in names if "n" in name]
print(result)