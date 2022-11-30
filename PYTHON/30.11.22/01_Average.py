def average(sum,n):
    av = sum/n
    return av;

num = str(input("Insert the first number: "))
i = 1
risp = str('s')
while(risp in 'sS'):
    prnum = int(input("Insert next number: "))
    num += prnum
    i += 1
    risp = str(input("Continuare? (S/N"))
print (average(num, i))
