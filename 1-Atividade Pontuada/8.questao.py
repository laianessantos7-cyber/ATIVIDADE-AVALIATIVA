#Atividade avaliativa- 05/09/2025
#Limpar terminal
import os
os.system("cls")

print("====TABELA DE PREÇOS=====")
print("""
        Cor \t      \t Preço
1\tVerde      \t R$ 10,00   
2\tAzul        \t R$ 20,00
3\tAmarelo     \t R$ 30,00
4\tVermelho     \t R$ 40,00
      

""")

cor=input("Digite a cor do CD: ")
match cor:
    case "Verde":
        preco = 10.00
    case "Azul":
        preco = 20.00
    case "Amarelo":
        preco = 30.00
    case "Vermelho":
        preco = 40.00
    case _:
        preco = None  

if preco is not None:
    print(f"O preço do CD {cor} é R$ {preco:.2f}")
else:
    print("Cor inválida! Digite uma das opções: Verde, Azul, Amarelo ou Vermelho.")