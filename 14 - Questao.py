ganhoHora = float(input("Digite quanto você ganha por hora: "))
horasTrabalho = float(input("Digite o número de horas trabalhadas no no mês: "))

salarioBruto = ganhoHora * horasTrabalho

# Qanto pagou:
inss = salarioBruto * 0.08
ir = salarioBruto * 0.11
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - (inss + ir + sindicato)

print(f"Salario Bruto: R$ {salarioBruto:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"IR: R$ {ir:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"salario Liquido: R$ {salarioLiquido:.2f}")