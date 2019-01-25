# TODO: Write a program that prompts the user for their name. when they respond,
#   write their name to a file called guest.txt
filename= 'guest.txt'                           # this variable saves the file name
with open(filename,'w') as file_object:       # creates the files in write mode ('w' = write mode, 'r' = readmode, 'a' = append)
    guestName = str(input("Please enter your name:\n"))
    file_object.write(guestName + "\n")
    # TODO: User input not able to taken in atom. (like sublime)
