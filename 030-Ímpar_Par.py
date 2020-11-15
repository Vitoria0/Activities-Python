n = float(input('Digite um número qualquer: '))
r = n % 2
if r == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))