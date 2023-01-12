# Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the
# resultant string and print it.

text = input("Enter a string \n")
if len(text) <= 5:
    print('String length should be more than 5')
else:
    lis = list(text)
    lis.pop(3)
    lis.pop(3)
    lis = lis[::-1]
    f = ''
    for i in lis:
        f = f + i
    print(f)
