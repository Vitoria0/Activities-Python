import random
a1 = str(input("Digite o nome de um aluno: "))
a2 = str(input("Digite o nome de um aluno: "))
a3 = str(input("Digite o nome de um aluno: "))
a4 = str(input("Digite o nome de um aluno: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem será: ")
print(lista)