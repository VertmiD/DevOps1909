a = "Aviel"
for i in range(5):
    print(i+1,") ",a)

print(a*5)

print(list(range(5)))
print(list(range(0, 50, 10)))
print(list(range(100, 50, -10)))

names = ["Dvir", "Adi", "Tal"]
for name in names:
    if name == "Dvir":
        name = "roi" # changing name only for the current iteration
    print(f"Hello {name}")

for moshe in range(5):
    print(moshe)
    print(a)

for i in range (len(names)):
    print(f"Hello {names[i]}")

