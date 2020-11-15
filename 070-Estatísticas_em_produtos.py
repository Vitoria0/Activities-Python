#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

nome_da_loja = 'KITTY'

print('~' * 50)
print(f'{nome_da_loja:^50}')
print('~' * 50)

from math import fsum
lista_produtos = []
lista_preços = []
produtos_1000 = 0
while True:
    produto = str(input("Qual o nome do produto? "))
    lista_produtos.append(produto)
    preço = float(input("Qual o preço do produto? R$"))
    lista_preços.append(preço)
    if preço > 1000:
        produtos_1000 += 1
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input("Adicionar mais produtos?[S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break
mais_barato = (lista_produtos[lista_preços.index(min(lista_preços))])
print("*" * 25)
print(f"\nO total gasto na compra foi R${fsum(lista_preços):.2f}")
print(f"{produtos_1000} produtos custaram mais de R$1000")
print(f"O produto mais barato é {mais_barato} custando R${min(lista_preços)}\n\n")


print("*" * 25)
print("nota fiscal:")
for i in range(len(lista_preços)):
    print(f"{lista_produtos[i]}-R${lista_preços[i]}")
print(f"\nTotal.....R${fsum(lista_preços)}")
print("*" * 25)