print('\033[35m~'*30)
print('\033[35mANALIZADOR DE TRIANGULOS')
print('~'*30)
print('\n')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mOs segmentos acima podem formar um triagulo!')
else:
    print('\033[31mOs segmentos acima não podem formar um triangulo')