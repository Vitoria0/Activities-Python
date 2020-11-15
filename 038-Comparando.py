n1 = int(input('Digite um número interiro: '))
n2 = int(input('Digite mais um número: '))
if n1 < n2:
    print('O valor {} é o maior'.format(n2))
elif n1 > n2:
    print('O valor {} é o maior'.format(n1))
elif n1 == n2:
    print('Os dois valores são iguais')