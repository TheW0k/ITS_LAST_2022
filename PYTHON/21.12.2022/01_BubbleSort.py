def bubble_sort(str1):
    swaps_made = True
    while swaps_made:
        swaps_made = False
        for i in range(len(str1) - 1):
            if str1[i] > str1[i + 1]:
                str1[i], str1[i + 1] = str1[i + 1], str1[i]
                swaps_made = True
    return str1

sorted_list = bubble_sort([5, 2, 4, 1, 3, 8, 99, 15])
print(sorted_list)  # [1, 2, 3, 4, 5]
