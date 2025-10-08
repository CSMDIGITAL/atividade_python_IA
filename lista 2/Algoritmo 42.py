# Entrar com um ângulo em graus e imprimir: seno, co-seno,
# tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math.

# Entrar com um ângulo em graus e imprimir: seno, co-seno,
# tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math.

import math

angulo_graus = float(input("Digite o ângulo em graus: "))
angulo_rad = math.radians(angulo_graus)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Evitar divisão por zero
secante = 1 / cosseno if cosseno != 0 else float('inf')
cosecante = 1 / seno if seno != 0 else float('inf')
cotangente = 1 / tangente if tangente != 0 else float('inf')

print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")
print(f"Secante: {secante}")
print(f"Cosecante: {cosecante}")
print(f"Cotangente: {cotangente}")