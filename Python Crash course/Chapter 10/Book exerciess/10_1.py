file_path = 'C:/Users/James/Documents/Python/Python Crash course/Chapter 10/TextFiles/learning_python.txt'

with open(file_path) as fObj:
    content = fObj.read()       # reads all data as one object
    print(content)

with open(file_path) as fObj:
    for line in fObj:
        print(line.strip())
print("\n")

with open(file_path) as fObj:
    lines = fObj.readlines()    # stores data as lists
for line in lines:
    print(line.rstrip())
