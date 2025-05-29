
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# "while True" yields an infinite loop.
# One can exit a loop by using the break operator.
# A valid number can be converted to an int.

def input_int():
    sum = 0
    while True:
        x = input("enter an integer: ")

        try:
            xx = int(x)
        except:
            xx = 0
            print("Enter a valid number")
        if (x == 'done'):
            break
        sum = sum + xx
    print("the sum is =", sum)


input_int()
