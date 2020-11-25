from random import randint
lista = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
a = randint(1,9)
print('\033[35m~'*50)
game = input('Olá, gostaria de jogar um jogo de adivinhação? ').strip().upper()
print('~'*50)
print('\n')
if game == 'SIM':
    print('\033[34mEstou pensando em um número de 1 á 9...')
    n = int(input('Em qual número estou pensando? '))
    if n == a:
        print('\033[33mNossa! você é bom nisso o número que eu escolhi realmente foi {}'.format(a))
        print('Parabéns! Você ganhou!')
    else:
        print('\033[31m\nErrado! o número que eu escolhi foi {}'.format(a))
        print('Fim de jogo')
elif game == 'NÃO':
    print('\033[36mOK! Volte quando quiser')