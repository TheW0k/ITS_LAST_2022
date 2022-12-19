for line in open("data\lezioni_americane.txt"):
    #print(line, end="")
    count = 0 
    
    for char in line:
        if char in "aA":
            count += 1

print("A:", count)