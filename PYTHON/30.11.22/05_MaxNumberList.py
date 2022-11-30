"""
list1 = [10, 20, 4, 45, 16]
list1.sort()
print("Largest number is:", list1[-1])
"""
n =[5,8,77,8,9]
def maxValue(n):
    sus = None
    
    for value in n:
        if sus == None or value > sus:
            sus = value
    return sus

print("Largest number is:", maxValue(n))