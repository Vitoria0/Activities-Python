#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = []
resp = 's'
cont = 0
med = 0
while resp == 's':
    num.append(int(input("Digite um número: ")))
    resp = input("Quer continuar? [s] ou [n] ").lower()
    cont += 1
num.sort()
med = sum(num) / cont
print(f'Você digitou {cont} números \nO menor é {num[0]} \nO maior é {num[-1]} \nA média é {med} \nE a soma é {sum(num)}.')