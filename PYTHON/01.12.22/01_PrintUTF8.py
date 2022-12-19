def print_utf8(start, end):
    for i in range(start, end+1):
        print(chr(i), end="")
    
print_utf8(32, 128)