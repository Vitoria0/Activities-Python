a = int(input('O primeiro valor: '))
b = int(input('O segundo valor: '))
c = int(input('O terceiro valor: '))
if a<b  and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
if a>b  and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))