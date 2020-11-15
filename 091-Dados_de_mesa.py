from random import randint
from time import sleep
from operator import itemgetter

tabela = {}
jogo = {'Jogador-1': randint(1, 6),
        'Jogador-2': randint(1, 6),
        'Jogador-3': randint(1, 6),
        'Jogador-4': randint(1, 6)}
print('-' * 50)
print(f'{"PRONTOS? JOGAR!":^50}')
print('-' * 50)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.8)
print('-' * 50)
print(f'{"HANKING DOS JOGADORES":^50}')
print('-' * 50)
tabela = sorted(jogo.items(), key=itemgetter(1), reverse= True)
for i, v in enumerate(tabela):
    print(f'{i+1}º lugar: {v[0]}')
print('-' * 50)