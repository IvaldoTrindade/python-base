#!usr/bin/env python3
'''
Imppython3 tabuada.py
 ao 10.

----Tabuada do 1------
        1x1 = 1
        1x2 = 2
        1x3 = 3
        1x4 = 4
....
###########
-----Tabuada do 2------
        2x1 = 2
        2x2 = 4
        2x3 = 6
        2x4 = 8
...
'''

__version__ = "1.1.0"
__author__ = "Ivaldo"

#base = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))


for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2        
        print("{:^20}".format(f"{n1} x {n2} = {resultado}"))
    print("#"*20)