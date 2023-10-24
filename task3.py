#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

evenNum = False
while not evenNum:
    num = int(input("enter a number: "))
    if num % 2 != int(0):
        print("That is not an even integer")
    else:
        evenNum = True
        print("that is an even integer")
        break
