# Entrar com um número e informar se ele é ou não divisível por 5.

num = int(input("Digite um número: "))

if num % 5 == 0:
    print(f"{num} é divisível por 5.")
else:
    print(f"{num} não é divisível por 5.")