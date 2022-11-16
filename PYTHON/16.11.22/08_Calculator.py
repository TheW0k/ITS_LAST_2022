"""
# Calculator
# @author: TheW0k
# @version: 1.0 2022-11-16
"""
a = int(input("First value: "))
b = int(input("Second value: "))
sel = input("Select one option:" + "\n" + "1: Addition" + "\n" + "2: Subtraction" + "\n" + "3: multiplication" + "\n" + "4: division" + "\n" + "5: Exponentiation" + "\n" + "Options: ")

if sel == 1:
    print(a+b)
elif sel == 2:
    print(a-b)
elif sel == 3:
    print(a*b)
elif sel == 4:
    print(a/b)
else:
    print(a**b)
    