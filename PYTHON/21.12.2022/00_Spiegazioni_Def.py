def ContaCararatteri(stringa,charC):
    count = 0
    for char in stringa:
        if (char == charC):
            count += 1
    return count

print(ContaCararatteri("Ciao italia","i"))    