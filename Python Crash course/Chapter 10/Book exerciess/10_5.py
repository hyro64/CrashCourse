# TODO: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

filename= 'reasons.txt'

while True:
	guestReason = input("Please enter why you like programming:\n (q to quit)\n")
	if guestReason == 'q':
		print("Quiting...")
		break
	elif guestReason != 'q':
		with open(filename,'w') as file_object:       # creates the files in write mode ('w' = write mode, 'r' = readmode, 'a' = append
			file_object.write(guestReason + "\n")
