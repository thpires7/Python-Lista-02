import os

numeros = []

for i in range(2):
    inteiro = int(input(f"Digite o {1 + i}º numero inteiro: "))
    numeros.append(inteiro)

real = float(input("Digite um numero real: "))
os.system('cls')

produto = (2 * numeros[0]) * (numeros[1] / 2)
soma = (3 * numeros[0]) + real
terceiroCubo = real**3

print(f"O produto do dobro do primeiro com metade do segundo: {produto}")
print(f"Soma do triplo do primeiro com o terceiro: {soma}")
print(f"O terceiro elevado ao cubo: {terceiroCubo}")