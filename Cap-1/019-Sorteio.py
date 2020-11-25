import random
a1 = str(input("Digite o nome de um aluno: "))
a2 = str(input("Digite o nome de um aluno: "))
a3 = str(input("Digite o nome de um aluno: "))
a4 = str(input("Digite o nome de um aluno: "))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print("\n O aluno escolhido foi {}".format(escolhido))
