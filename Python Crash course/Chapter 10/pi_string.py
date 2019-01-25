file_name = 'C:/Users/James/Documents/Python/Python Crash course/Chapter 10/TextFiles/pi_digits.txt'
# with open(file_name) as file_object:
# 	lines = file_object.readlines() # object is read as list from the files
#                                     # list items ends at return carriage
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()       # strip used to take off all white space
 										# before and after list items
#
# print(pi_string)
# print(len(pi_string))

"""Large Files: One Million Digits"""S
# file_name = 'C:/Users/James/Documents/Python/Python Crash course/Chapter 10/TextFiles/pi_million_digits.txt'\
#
# with open(file_name) as file_object:
# 	lines = file_object.readlines() # object is read as list from the files
#                                     # list items ends at return carriage
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()       # strip used to take off all white space
# 										# before and after list items
#
# print(pi_string[:52] + "...")       # stops the print statement after 52 characters
# print(len(pi_string))

"""Is your birthday contained in Pi?"""
with open(file_name) as file_object:
	lines = file_object.readlines() # object is read as list from the files
                                    # list items ends at return carriage
pi_string = ''
for line in lines:
    pi_string += line.strip()       # strip used to take off all white space

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
