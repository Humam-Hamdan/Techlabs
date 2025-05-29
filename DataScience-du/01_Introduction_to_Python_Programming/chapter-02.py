# 1. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. Print your computed pay.
# Use the built-in input method to read hours and rate per hour separately.
# Typecast both inputs to floats.
# Use an if-condition to test whether the hours are below or equal to 40 hours.
# Print the result by multiplying the hours with their rate per hour using the *-operator.

hours = input("How Many hours: ")
try:
    fhours = float(hours)
except:
    print('NaN')
rate = input("What is the Rate: ")
try:
    frate = float(rate)
except:
    print('NaN')
if fhours <= 40:
    print('The Pay is:', fhours*frate)
elif fhours > 40:
    tem_hours = fhours - 40
    print('The Pay is:', (tem_hours*frate*1.5)+frate*40)

# 2. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following scheme: >= 0.9 A; >= 0.8 B; >= 0.7 C; >= 0.6 D; < 0.6 F. For the test, enter a score of 0.85.
# Check whether the input score is out of range first.
# Check for the different grade levels in descending order.
# Remind yourself of elif-conditions.

rawscore = input('What is the score? ')
try:
    fscore = float(rawscore)
except:
    print('Nan')
try:
    0.0 <= fscore <= 1.0
except:
    print('Out of range')

if fscore >= 0.9:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    print('D')
else:
    print('F')
