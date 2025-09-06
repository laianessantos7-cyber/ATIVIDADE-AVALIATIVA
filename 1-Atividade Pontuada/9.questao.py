#Atividade avaliativa- 05/09/2025
#Limpar terminal

import os
os.system("cls")

renda = float(input("Digite a sua renda mensal (R$): "))
emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))
parcelas = int(input("Digite o número de prestações desejadas: "))

prestacao = emprestimo / parcelas


limite_emprestimo = renda * 10
limite_prestacao = renda * 0.30

if emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print("Empréstimo aprovado.")
    print(f"Valor do empréstimo: R$ {emprestimo:.2f}")
    print(f"Número de parcelas: {parcelas}")
    print(f"Valor da prestação: R$ {prestacao:.2f}")
else:
    print("Empréstimo negado.")
    if emprestimo > limite_emprestimo:
        print("Motivo: valor do empréstimo excede 10 vezes a renda.")
    if prestacao > limite_prestacao:
        print("Motivo: valor da prestação excede 30% da renda.")