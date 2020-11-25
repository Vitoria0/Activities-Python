from time import sleep
from random import randint
options = int(input('''Suas opções:

[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura

Qual é a sua jogada? '''))
itens = ('Pedra', 'Papel', 'Tesoura')
robo = randint(0,2)
if options > 2 or options < 0:
    print('\033[1;4;31mJogada Inválida.\033[m')
    exit(0)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
print(f'''Computador jogou {itens[robo]}
Você jogou {itens[options]}''')
print('-='*12)
if options == 0 and robo == 2:
    print(f'\033[1;4;32mVocê VENCEU!\033[m')
elif options == 2 and robo == 1:
    print(f'\033[1;4;32mVocê VENCEU!\033[m')
elif options == 1 and robo == 0:
    print(f'\033[1;4;32mVocê VENCEU!\033[m')
if robo == 0 and options == 2:
    print(f'\033[1;4;31mComputador VENCEU!\033[m')
elif robo == 2 and options == 1:
    print(f'\033[1;4;31mComputador VENCEU!\033[m')
elif robo == 1 and options == 0:
    print(f'\033[1;4;31mComputador VENCEU!\033[m')
elif robo == options:
    print('\033[1;4;33mEMPATE!\033[m')