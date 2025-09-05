#Limpar terminal

#Atividade avaliativa- 05/09/2025

import os
os.system("cls")


produto=input("Digite o nome do produto: ")
quantidade=float(input("Digite a quantidade adquirida: "))
preco_unitario=float(int(input("Digite o valor unitário: ")))


total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05


total_pagar = total - desconto

print("====NOTA FISCAL====")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")