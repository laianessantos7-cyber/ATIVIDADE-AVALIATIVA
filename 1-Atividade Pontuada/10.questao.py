#Atividade avaliativa- 05/09/2025
#Limpar terminal
import os
os.system("cls")

print("====TABELA DE DESCONTOS=====")
print("""
        Combustível \t     \t Quantidade Vendida (litros) \t Desconto por litro
1\t Álcool    \t Até 25 litros                     \t 10%   
2\t Álcool       \t Acima de 25 litros             \t 20%
3\t Gasolina    \t Até 25 litros                   \t 15%
4\t Gasolina   \t R$ Acima de 25 litros            \t 30%
      

""")
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()
preco_alcool= 3.79
preco_gasolina= 6.59




match tipo:
    case "A":
        if litros <= 25:
            desconto = 0.10
        else:
            desconto = 0.20
        valor_bruto = litros * preco_alcool
        valor_desconto = valor_bruto * desconto
        valor_final = valor_bruto - valor_desconto
        print(f"\n--- Álcool ---")
        print(f"Valor bruto: R$ {valor_bruto:.2f}")
        print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
        print(f"Valor final a pagar: R$ {valor_final:.2f}")

    case "G":
        if litros <= 25:
            desconto = 0.15
        else:
            desconto = 0.30
        valor_bruto = litros * preco_gasolina
        valor_desconto = valor_bruto * desconto
        valor_final = valor_bruto - valor_desconto
        print(f"\n--- Gasolina ---")
        print(f"Valor bruto: R$ {valor_bruto:.2f}")
        print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
        print(f"Valor final a pagar: R$ {valor_final:.2f}")

    
    case _:
        print("Tipo de combustível indisponivel!")
    
