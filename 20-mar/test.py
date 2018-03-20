'''
Programa que calcula as raízes quadradas da 
equação a * (x ** 2) + b * (x) + c = 0, se estas forem reais.

Instruções:
    Para executar digite: python test.py
    ou                    python3 test.py

Entrada:
    A primeira entrada corresponde ao valor da variável 'a',
    A segunda entrada corresponde ao valor da variável 'b' e
    A terceira entrada corresponde ao valor da variável 'c'.
Saída:
    A menor raiz da equação
    A maior raiz da equação
'''

import math

a = int(input())
b = int(input())
c = int(input())

determinante = b**2 - 4*a*c
x1 = (-b - math.sqrt(determinante)) / (2*a)
x2 = (-b + math.sqrt(determinante)) / (2*a)

print (x1)
print (x2)
