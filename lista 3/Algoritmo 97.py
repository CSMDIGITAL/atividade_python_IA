# Entrar com um número e informar se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes.

numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print("Divisível por 10")
elif numero % 5 == 0:
    print("Divisível por 5")
elif numero % 2 == 0:
    print("Divisível por 2")
else:
    print("Não é divisível por 10, 5 ou 2")
