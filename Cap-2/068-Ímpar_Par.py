#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitoria = 0
titulo = 'JOGO DE IMPAR OU PAR'

print('~'*50)
print(f'{titulo:^50}')
print('~'*50)
print('\n')


while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Impar ou Par? ')).strip().upper()[0]
    print(f'\nVocê jogou {jogador} e o computador {computador}. O total foi de {total}')

    if tipo == 'P':
        if total %2 == 0:
            print('Você ganhou')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você ganhou')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    print('\nVamos jogar novamente...')
print(f'Você teve um total de {vitoria} vitórias')