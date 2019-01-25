"""Handling the ZeroDivisionError Exception"""
# print(5/0)

"""Using try-except blocks"""
# used like the try and catch blocks in java
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zeor!")

"""Using Exceptions to prevent crashes"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
