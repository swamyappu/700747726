# Take two numbers from user and perform at least 4 arithmetic operations on them

val1 = float(input("Enter Value 1 \n"))
val2 = float(input("Enter value 2 \n"))
print('Addition : ', (val1 + val2))
if val1 >= val2:
    print('Subtraction : ', (val1 - val2))
else:
    print('Subtraction : ', (val2 - val1))
print('Multiplication : ', (val1 * val2))
if val2 != 0.0:
    print('Division : ', (val1 / val2))
else:
    print('Division : Infinity')
