# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# E o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

titulo = 'CAIXA ELETRÔNICO'

print('#' * 25)
print(f'{titulo:^25}')
print('#' * 25)

valor = int(input('Que valor você quer sacar? R$'))
ced = 50
total = 'valor'
totced = 0
while True:
    if total >= 'ced':
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} células de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break