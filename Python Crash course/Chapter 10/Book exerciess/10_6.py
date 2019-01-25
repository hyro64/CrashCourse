# TODO: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you'll get a "ValueError". Write a program that prompts for two numbers. Add them together and print the result. Catchthe "ValueError" if either input value is not a number, and print a friendly error message. Test your program by entering some text instea of a number.

def valueCatch():
    while True:
        try:
            first_number = int(input("First number:\n"))
            if first_number == 'q':
                print("Ending program")
                break
            second_number = int(input("Second number:\n"))
            if second_number == 'q':
                print("Ending program")
                break
            answer = first_number / second_number
        except ValueError as e:
            print("Please enter numbers only")
        else:
            print(answer)

valueCatch()
