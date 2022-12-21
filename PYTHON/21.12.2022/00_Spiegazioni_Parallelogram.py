base = int(input("Quanto è largo il parallelograma? "))
height = int(input("Quanto è alto il parallelogramma? "))
char = str(input("Quale carattere si vuole usare? "))
form = str(input("Quale forma si vuole avere? 1, 2? "))

space = ' '
build = char * base
if (form == '1'):
    for j in range(0, height):
        print(space * j + build)
if (form == '2'):
    for j in range(height,0,-1):
        print(space * j + build)
