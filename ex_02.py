
"""
    2𝑥ˆ2 + 2𝑥 − 6
    -b +- sqrt(b²-4ac) / 2a"""

import numpy as np

def resolve(a,b,c):
    delta = b**2 - 4*a*c
    if delta<0:
        print("essa função não tem raízes")
        return None
    if delta == 0:
        print(f"a raíz unica desa função vale {-b/(2*a):.2f}")

    x1 = (-b + (delta)**0.5) / (a*2)
    x2 = (-b - (delta)**0.5) / (a*2)
    print(f"os valores das raízes são {x1:.2f} e {x2:.2f}")
    return x1,x2

funcao = input("digite a função no formato Ax²+Bx+C:\n")

a,b,c = funcao.replace('²', '').replace('+', '').split('x')
a = int(a)
b = int(b)
c = int(c)
print(a,b,c)


x1, x2 = resolve(a,b,c)
