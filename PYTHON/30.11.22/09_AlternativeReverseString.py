def rev_char(s):
    result = ""
    for char in range(len(s)-1, -1, -1):
        result = char + s[char]
    return result
print(rev_char("SUS Big chungus"))