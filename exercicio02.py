# Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ouzero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo (deltanegativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a zero.

import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a == 0:
    print("Não é uma equação do segundo grau.")
else:
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print("As raízes da equação são:", raiz1, "e", raiz2)
    elif delta == 0:
        raiz = -b / (2*a)
        print("A única raiz real da equação é:", raiz)
    else:
        print("Não há raízes reais.")
