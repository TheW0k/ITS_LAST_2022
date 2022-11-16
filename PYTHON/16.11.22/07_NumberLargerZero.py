"""
# "Num > 0? Yes or no?"
# @author: TheW0k
# @version: 1.0 2022-11-16
"""
num = int(input("Give me a number: "))

if num > 0:
    print("Positive")
elif num  < 0:
    print("Negative")
else:	
    print("Zero")
    
"""
# Alternative:

if num > 0:
    print("Positive")
else:
    if num  < 0:
        print("Negative")
    else:	
        print("Zero")
"""