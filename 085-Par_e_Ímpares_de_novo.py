#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? S/N: ')).upper()
    if r in 'N':
        for i, v in enumerate(lista):
            if v % 2 == 0:
                pares.append(v)
            else:
                impares.append(v)
        print(f'A lista completa é: {lista}')
        print(f'Os números pares são: {pares}')
        print(f'Os números impares são: {impares}')
        break
    if r in 'S':
        continue
    else:
        print('Resposta inválida! Tente novamente')