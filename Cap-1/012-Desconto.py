p1 = float(input('Qual o preço do produto? R$'))
p2 = p1 * 5 / 100
p3 = p1 - p2
print("Você tem R${} de desconto, sendo assim R${} o preço do produto".format(p2, p3))