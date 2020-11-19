import moeda2

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}')
print(f'O dobre de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.dobro(p))}')
print(f'aumentando 10% temos R${moeda2.moeda(moeda2.aumentar(p, 10))}')