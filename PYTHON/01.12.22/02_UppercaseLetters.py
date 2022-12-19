def count_uppercase_letters(s):
    count = 0
    
    for char in s:
        if char >= "A" and char <="z":
            count += 1
            
    return count

count_uppercase_letters