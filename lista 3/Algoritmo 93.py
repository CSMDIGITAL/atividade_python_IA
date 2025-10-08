import math

# Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo e o quadrado do número caso ele seja negativo.
num = float(input("Digite um número: "))

if num >= 0:
    print("Raiz quadrada:", math.sqrt(num))
else:
    print("Quadrado:", num ** 2)