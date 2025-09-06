#Atividade avaliativa- 05/09/2025
#Limpar terminal

import os
os.system("cls")


A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


if A == B:
    C = A + B   
else:
    C = A * B  

print("O valor de C é:", C)