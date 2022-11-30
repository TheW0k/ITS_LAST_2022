"""
@author: TheW0k
@version 1.0 2022-11-24
"""
h = int(input("Altezza: "))
char = input("Carattere: ")
n_char = 1

for i in range(h):
    print(" " * (h - i - 1), end="")
    print(char * n_char)
    n_char += 2  
    