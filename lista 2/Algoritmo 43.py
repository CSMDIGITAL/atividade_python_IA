# – Entrar com um número e imprimir o logaritmo desse número na base 10.

import math

numero = float(input("Digite um número: "))
if numero > 0:
    logaritmo = math.log10(numero)
    print(f"O logaritmo de {numero} na base 10 é {logaritmo}")
else:
    print("O número deve ser maior que zero para calcular o logaritmo.")