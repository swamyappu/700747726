# Use the if statement conditions to write a program to print the letter grade based on an input class score. Use
# the grading scheme we are using in this class

scr = int(input('Enter the Score \n'))
if scr > 90:
    print('Grade A')
elif 90 >= scr > 80:
    print('Grade B')
elif 80 >= scr > 70:
    print('Grade C')
elif 70 >= scr > 60:
    print('Grade D')
else:
    print('Grade F')
