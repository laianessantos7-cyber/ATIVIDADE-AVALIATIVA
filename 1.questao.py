#Limpar terminal

#Atividade avaliativa- 05/09/2025

import os
os.system("cls")

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A + B < C:
    print("A + B é menor que C.")
else:
    print("A + B é maior ou igual a C.")