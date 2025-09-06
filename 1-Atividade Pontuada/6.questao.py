#Atividade avaliativa- 05/09/2025
#Limpar terminal
import os
os.system("cls")

print('=====BOLETIM ESCOLAR=====')

nome= input("Digite Seu Nome: ")
idade= float(input("Digite Sua Idade:"))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2
print(f"Média do aluno:{media:.1f}")
if media >=6.0:
    print("Aprovado, Parabéns!")
elif media <= 4.1  and media <=5.9:
   print("Recuperação.")
else:
    print("REPROVADO.")