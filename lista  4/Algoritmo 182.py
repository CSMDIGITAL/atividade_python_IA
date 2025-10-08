# Entrar com 10 números e imprimir a metade de cada número

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    print(f"A metade de {num} é {num / 2}")