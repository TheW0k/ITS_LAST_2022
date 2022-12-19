def in_range(values, start, end):
    result = []
    for value in values:
        if value >= start and value <= end:
            result.append(value)
    return result

def median(values):
    values.sort()
    
    n = len(values)
    
    if n % 2 == 0:
        return values[n // 2 - 1] + values[n // 2] / 2
    else:
        return values[n // 2]

def mode(values):
    result = []
    occurrences = []
    
    for value1 in values:
        count = 0
        
    for value2 in values:
        if value1 == value2:
            count += 1
            
    occurrences.append(count)
    
    mode_counter = max(counters)
    for i in range(len(counters)):
        if counter[i] == mode_counter and not values[i] in result:
            result.append(values[i])
    return result

values = [9,7,6,3,5,5,8]
print(in_range(values, 6, 8))
