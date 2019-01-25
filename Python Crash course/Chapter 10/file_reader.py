file_name = 'C:/Users/James/Documents/Python/Python Crash course/Chapter 10/TextFiles/pi_digits.txt'
"""Reading an entire file/File paths"""
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

"""Reading line by line"""
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip()) #rstrip removes the black space as the lines print

"""Making a list"""
with open(file_name) as file_object:
	lines = file_object.readlines() # object is read as list from the files
                                    # list items ends at return carriage
for line in lines:
    print(line.rstrip())
