import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobre de R${p} é R${moeda.dobro(p)}')
print(f'aumentando 10% temos R${moeda.aumentar(p, 10)}')