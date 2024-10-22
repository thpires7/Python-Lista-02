sexo = input("Digite o seu sexo ('M' para masculino e 'F' para feminino): ")
altura = float(input("Digite sua altura: "))

if sexo.lower() == 'm':
    peso = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com {altura} de altura é: {peso:.2f} kg")
elif sexo.lower() == 'f':
    peso = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com {altura} de altura é: {peso:.2f} kg")
else:
    print("Sexo Invalido!")