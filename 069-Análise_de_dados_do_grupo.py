#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantas pessoas foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

nome = [ ]
idade = [ ]
genero = [ ]
maiores = 0

while True:
    nome1 = nome.append(str(input('Nome: ')))
    idade1 = nome.append(int(input('Idade: ')))
    genero1 = nome.append(str(input('Genero: ')))

    rep = str(input('Quer continuar os cadastros? ')).strip().upper()[0]
    if rep == 'S':
        print('~' * 50)
    elif rep == 'N':
        if idade1 > 18:
            maiores += 1