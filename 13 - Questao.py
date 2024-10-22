peso = float(input("Digite o peso do peixe: "))
limite = 50

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
    print(f"Voce deve pagar R$ {multa:.2f} por passar o limite de peso.")
else:
    print("Não é preciso pagar multa.")