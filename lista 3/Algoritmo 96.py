# Entrar com um número e informar se ele é divisível por 3 e por 7.

# Entrar com um número e informar se ele é divisível por 3 e por 7.

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 7 == 0:
    print(f"{numero} é divisível por 3 e por 7.")
else:
    print(f"{numero} não é divisível por 3 e por 7.")