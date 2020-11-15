from time import sleep
from random import randint
n=int(input('Quantos jogos você quer que eu sorteie? '))
print()
print((17*'*')+'<Sorteio realizado!>'+(17*'*'))
jogos=[]
for c in range(0,n):
    jogos.append(list())
    for num in range(0,6):
        sorteado=randint(0,60)
        if num==0:
            jogos[c].append(sorteado)
        else:
            while sorteado in jogos[c]:
                sorteado = randint(0, 60)
            jogos[c].append(sorteado)
    print(f'Jogo {c+1}:',end=' ')
    print(f'{sorted(jogos[c])}')
    sleep(0.5)
print((21*'*')+'<Boa sorte!>'+(21*'*'))