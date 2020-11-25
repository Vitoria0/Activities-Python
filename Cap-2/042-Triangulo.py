l1 = float(input('Informe o primeiro lado do triangulo: '))
l2 = float(input('Informe o segundo lado do  triangulo: '))
l3 = float(input('Informe o terceiro lado do triangulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 == l2 and l2 == l3:
    print('Ok, suas medidas formam um triangulo EQUILATERO')

elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 != l2 and l2 != l3 and l1 != l3:
    print('Ok, suas medidas formam um triangulo  ESCALENO.')
elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2:
    print('Ok, suas medidas formam um triangulo ISOCELES.')
else:
    print("Suas medidas nao formam um triangulo.")