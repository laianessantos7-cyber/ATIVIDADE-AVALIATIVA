#Limpar terminal

#Atividade avaliativa- 05/09/2025

import os
os.system("cls")

A = float(int(input("Digite o valor de A: ")))
operador= input("Digite a operação (+,-,*,/): ")
B = float (int(input("Digite o valor de B: ")))



if operador == "+":
    resultado = A + B
elif operador == "-":
    resultado = A - B
elif operador== "*":
    resultado = A * B
elif operador == "/":
    if B != 0:
        resultado = A / B
    else:
        resultado = "Erro divisão por zero."
else:
    resultado = "Operação inválida."


print("Resultado:", resultado)