def count_in_range(a,b):
    count = 0
    value = int(input("Number? "))
    
    while value != 0:
        if value % 2 == 0:
            count += 1
        value = int(input("Next? "))
    return count


print ("Number between 3 and 10", count_in_range(3,10))
