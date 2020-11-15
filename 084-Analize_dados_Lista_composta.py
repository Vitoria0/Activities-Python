#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves

pessoa = []
lista = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    r = str(input('Quer continuar? S/N: ')).upper()[0]
    pessoa.append(lista[:])
    if len(pessoa) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista
        if lista[1] < menor:
            menor = lista


    if r in 'N':
        print(f'No total {len(pessoa)} pessoas')
        print(f'O maior peso registraado foi de {maior}Kg')
        print(f'O menor peso registraado foi de {menor}Kg')
        print(lista)
        break
    if r in 'S':
        continue
    else:
        print('Resposta inválida! Tente novamente')
