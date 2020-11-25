casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Em quantos anos deseja pagar? '))
p = casa / (ano * 12)
m = salario * 40 / 100
print('Para pagar uma casa de R${:.2f} em {} anos \na prestação será de R${:.2f}'.format(casa, ano, p))
if p <= m:
    print('Empréstimo pode ser ser concedido!')
else:
    print('Empréstimo negado!')