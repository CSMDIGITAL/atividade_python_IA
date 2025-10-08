# Construir um algoritmo que leia dois números e efetue a adição.
# Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
# Caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 20:
    resultado = soma + 8
else:
    resultado = soma - 5

print("Resultado:", resultado)