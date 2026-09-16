
# There are two ways to open and read a file.

# ---FILE MODES---
# "r" - Read Mode.
# "w" - Write Mode.
# "a" - Append 
# "x" - Create

# Those are for reading files. 

# File Writing - Overwrites whatever has been written from the attached file.
with open("output.txt", "w") as file:
    file.write("Hello, world!")

#Appending Files - Adds new typing without overriding the file text. 
with open("output.txt", "a") as file:
    file.write("This line gets added.")

# The Manual Way
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# The Modern Way Using Context Managers
# with open("example.txt", "r") as file:
    # content = file.read()
    # print(content)
