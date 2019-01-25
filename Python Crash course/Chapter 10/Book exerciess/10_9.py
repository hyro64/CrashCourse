# TODO: Modify the except block in Exercise 10_8.py to fail silently if either file is missing.

def readAnimals(fileName):
    """Prints the contents of the files but will fail silently."""
    try:
        with open(fileName) as f_obj_in:
            contents = f_obj_in.read()
    except FileNotFoundError:
        pass                                #Causes to fail silently
    else:
        print(contents)

fileNames = ['cats.txt','dogs.txt']         # create a dictionary for the files
for fileName in fileNames:                  # uses the dictionary for the method.
    readAnimals(fileName)
