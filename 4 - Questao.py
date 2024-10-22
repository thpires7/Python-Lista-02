notas = []

for i in range(4):
    nota = float(input(f"Digite a {1 + i}º nota do aluno: "))
    notas.append(nota)

media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print(f"A media do aluno é: {media:.2f}")

# media = 0

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print(f"A Sua media é: {media:.2f}")