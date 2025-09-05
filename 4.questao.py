#Limpar terminal

#Atividade avaliativa- 05/09/2025

import os
os.system("cls")

morango=float(input ("Digite o valor em Kg de morangos: ") )
maca=float(input ("Digite o valor em Kg de maçãs: ") )
print(" ")
print("====TABELA DE PREÇOS====")
print(" ")
print("""
        Fruta \t    Até 5 Kg \t \t Acima de 5 Kg
1\tMorango\tR$2,50 por Kg     \t R$ 2,50 por Kg
2\tMaçã \t R$ 1,80 por Kg \t R$ 1,50 por Kg

""")


if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20

if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50


valor_total = preco_morango + preco_maca


peso_total = morango + maca


if peso_total > 10 or valor_total > 15:
    valor_total = valor_total * 0.90 

print("====NOTA FISCAL====")
print(f"Valor a pagar: R$ {valor_total:.2f}")

