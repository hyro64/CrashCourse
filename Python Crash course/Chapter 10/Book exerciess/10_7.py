# TODO: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if the make a mistake and enter text instea of a number.

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
