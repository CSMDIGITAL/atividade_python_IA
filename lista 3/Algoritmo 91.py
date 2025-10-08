# Construir um algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.
a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
soma = a + b
if soma > 10:
    print("Resultado:", soma)