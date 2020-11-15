# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')),)

print(f'Você digitou os números: {n}')
print(f'O número 9 aparece {n.count(9)} vezes')
print(f'O valor 3 está na {n.index(3)+1} posição')
print('Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
