current_name = "Moshe"
while current_name != "quit":
    current_name = input("What is your name? ")
    if current_name == "Eden":
        continue # Skip to the next iteration of the loop without executing the rest of the code
    if current_name == "Ronen":
        break  # Stop the loop and exit the program
    print(f"Hello, {current_name}!")
    current_name = input("What is your name? ")
else:
    print("Goodbye!")

for i in range(5):
    print(i)

print("****************************")
print(i)
print("****************************")
