
# 1. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data. Print your computed pay.
# Use the built-in input method to read hours and rate per hour separately.
# Typecast both inputs to floats.
# Print the result by multiplying the hours with their rate per hour using the *-operator.

hours = float(input("How many hours?\n"))
rate = float(input("What is the hourly rate?\n"))
print("The pay is", hours * rate)
