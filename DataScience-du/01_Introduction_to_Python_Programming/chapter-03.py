# 1. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and 1.5 for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. Print your computed pay.
# Your function needs two arguments: hours and rate.
# Can you reuse code you have already written?

def pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
    return pay


rhours = input("How Many hours: ")
try:
    hours = float(rhours)
except:
    print('NaN')
rrate = input("What is the Rate: ")
try:
    rate = float(rrate)
except:
    print('NaN')

print('Pay is', pay(hours, rate))
