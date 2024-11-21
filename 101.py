current_name = input("What is your name?")

my_file = open('names.txt', 'a') #a = append (write after the old content without deleting the old content)
my_file.write(current_name + '\n')
my_file.close()

my_file = open("names.txt", 'r')
for name in my_file.readlines(): #Return list for the string in line
    if "n" in name:  # show only name with 'n'
        print(f"Hello {name.strip()}")
my_file.close()