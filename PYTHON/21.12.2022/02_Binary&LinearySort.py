def binary_search(value, values):
    import copy
    values2 = copy.deepcopy(values)
    values2.sort()

    start = 0
    end = len(values2) - 1

    while start <= end:
        index = (start + end) // 2

        if value == values2[index]:
            return index
        if value > values2[index]:
            start = index + 1
        else:
            end= index - 1


    return -1

def linear_search(value, values):
    for i in range(len(values)):
        if value == values[i]:
            return i
    return i-1
    

binary_list = binary_search(4, [5, 2, 4, 1, 3, 8, 99, 15])
linear_list = linear_search(3, [5, 3, 2, 4, 1, 3, 8, 99, 15])

print(binary_list)  # [1, 2, 3, 4, 5]
print(linear_list)  # [1, 2, 3, 4, 5]
