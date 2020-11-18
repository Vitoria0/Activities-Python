def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {l} X {c} é de {a}m²')


print(f'{"Controle de terreno":^40}')
print('-' * 40)
l = float(input('Largura do Terreno: [m] '))
c = float(input('Comprimento do terreno: [m] '))
area(l, c)