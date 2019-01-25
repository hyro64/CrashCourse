file_path = 'C:/Users/James/Documents/Python/Python Crash course/Chapter 10/TextFiles/learning_python.txt'

with open(file_path) as fObj:
    lines = fObj.readlines()       # reads all data as one object

txtString = ''

for line in lines:
    line.replace('python','C')
    txtString += line.strip()
    print(txtString)
# TODO: replace is not working in the replace method of the loop. check sytax 
