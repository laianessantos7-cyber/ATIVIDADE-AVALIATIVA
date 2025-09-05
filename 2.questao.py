#Limpar terminal

#Atividade avaliativa- 05/09/2025

import os
os.system("cls")


nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite o estado civil: ")

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = input("Digite o tempo de casada (em anos): ")
else:
    tempo_casada = "Não se aplica"

print("\n--- DADOS DO USUÁRIO ---")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
print("Tempo de casada:", tempo_casada)