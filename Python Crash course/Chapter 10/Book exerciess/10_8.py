# TODO: Make two files, cats.txt and dogs.txt. Store at least three nams of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the "FileNotFound" error, and print a friendly message if a file is missing. Move on of the files to a different location on your system, and make sure the code in the except block executes properly.

def readAnimals(fileName):
    try:
        with open(fileName) as f_obj_in:
            contents = f_obj_in.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + fileName +" does not exist in this directory."
        print(msg)
    else:
        print(contents)

fileNames = ['cats.txt','dogs.txt']
for fileName in fileNames:
    readAnimals(fileName)
