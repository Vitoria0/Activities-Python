from datetime import date
a = date.today().year
tm = 0
tn = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = a - nasc
    if idade >= 21:
        tm += 1
    else:
        tn += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE {} pessoas menores de idade'.format(tm, tn))