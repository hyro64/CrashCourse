# TODO: Write a while loop that propmts the user for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

filename= 'guest_book.txt'

while True:
	guestName = input("Please enter your name:\n (q to quit)\n")
	if guestName == 'q':
		print("Quiting...")
		break
	elif guestName != 'q':
		with open(filename,'w') as file_object:       # creates the files in write mode ('w' = write mode, 'r' = readmode, 'a' = append
			file_object.write(guestName + "\n")
