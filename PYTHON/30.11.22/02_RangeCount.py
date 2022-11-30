def count_in_range(a,b):
    count = 0
    value = int(input("Number? "))
    
    while value != 0:
        if value >= a and value <= b:
            count += 1
        value = int(input("Next? "))
    return count


print ("numero dal 3 al 10", count_in_range(3,10))
