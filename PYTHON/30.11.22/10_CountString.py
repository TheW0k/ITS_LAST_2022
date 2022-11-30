def count_string(s1,s2):
    count = 0
    for c1 in range(len(s1)):
        ver = True
        if c1 + len(s2) < len(s1):
            for c2 in range(len(s2)):
                if s1[c1 + c2] != s2[c2]:
                    ver = False
            if ver:
                count += 1
    return count

print(count_string("Bella  Ciao Ciao iaiaiaia", "iai"))