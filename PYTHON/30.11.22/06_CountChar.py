def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print(count_char("il dio bastardio!", "i"))