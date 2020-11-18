from random import randint

def sorteia(lista):
    print('Sorteando 5 números da lista: \n', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('\nPronto!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = []
sorteia(numeros)
somapar(numeros)