#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#E também indique o menor e o maior valor que estão na tupla.

from random import randint

n = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))
print(f'Os valores sorteados foram: {n}')
print(f'O maior número sorteado foi {max(n)}')
print(f'O menor número sorteado foi {min(n)}')