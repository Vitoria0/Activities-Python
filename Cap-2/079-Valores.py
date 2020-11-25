num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adcionado com sucesso')
    else:
        print('Valores duplicados não serão adcionados')
    r = str(input('Quer continuar? S/N: ')).upper()
    if r in 'N':
        break
print('-' * 30)
print(f'Você digitou os valores: {num}')