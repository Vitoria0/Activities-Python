s = 0
c = 0
for n in range(1, 7):
    num = int(input('Qual o {} valor: '.format(n)))
    if num % 2 ==0:
        s += num
        c += 1
print('Você informou {} números pares e a soma foi {}'.format(c, s))