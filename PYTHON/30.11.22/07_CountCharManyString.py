def count_char(s1, s2):
    count = 0
    for c1 in s2:
        for c2 in s1:
            if(c1 == c2):
                count += 1
    return count

print(count_char("SUS Big chungus","cu"))