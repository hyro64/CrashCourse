"""Writing to an empty file."""
filename= 'programing.txt'                                                      # this variable saves the file name
# with open(filename,'w') as file_object:                                       # creates the files in write mode ('w' = write mode, 'r' = readmode, 'a' = append)
#     file_object.write("I love programing.")                                   # what is written to the file

"""Writing multiple lines"""

# filename= 'programing.txt'                                                    # this variable saves the file name
#
# with open(filename,'w') as file_object:                                       # creates the files in write mode ('w' = write mode, 'r' = readmode, 'a' = append)
#     file_object.write("I love programing.")                                   # what is written to the file
#     file_object.write("I love creating games.\n")

"""Appending to a file"""
filename= 'programing.txt'                                                      # this variable saves the file name

with open(filename,'a') as file_object:                                         # creates the files in write mode ('w' = write mode, 'r' = readmode, 'a' = append)
    file_object.write("I love finding meaning in large datasets.\n")            # what is writen to the file
    file_object.write("I love creating apps that can run in a browser.\n")      # what is written to the file
