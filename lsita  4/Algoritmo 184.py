import math

for i in range(8):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > 0:
        log10 = math.log10(num)
        print(f"O logaritmo na base 10 de {num} é {log10}")
    else:
        print("Número inválido para cálculo do logaritmo (deve ser maior que zero).")
