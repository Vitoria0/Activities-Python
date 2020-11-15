#Crie um programa que tenha uma tupla única com nomes de produtos
#E seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular

lista = ('Rosa Vermelha', 5.99,
         'Ursinho pequeno', 10.00,
         'Ursinho gigante', 299.99,
         'Colar', 37.00,
         'Pulseira', 19.99,
         'Anel', 50.00,
         'Buquê de Rosas', 19.99,
         'Bom Bons', 16.50,
         'Balão de coração', 34.99,
         'Caneca', 32.75,
         'Meias Fofinhas', 12.99)

nome = 'LOJA DE PRSSENTES'

print('-' * 40)
print(f'{nome:^40}')
print('-' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<31}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')

print('-' * 40)