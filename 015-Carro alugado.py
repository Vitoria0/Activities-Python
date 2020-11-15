marcaCarro = str(input("Informe a marca do carro: "))
aluguel = int(input("Informe quantidade de dias: "))
kmRodado = int(input("Informa a quantidade de KM rodado: "))
valorDiaria = 60.00
valorKmRodado = 0.15

auxValorDiaria = (valorDiaria * aluguel)
auxValorKmRodado = (valorKmRodado * kmRodado)
valorTotalPagarAluguel = (auxValorDiaria + auxValorKmRodado)

print(" ")
print("...:::SAÍDA DE DADOS:::...")
print('A marca do carro é: ' + marcaCarro)
print('Total de dias do aluguel: {}' .format(aluguel))
print('Valor total de diária: {:.2f}' .format(auxValorDiaria))
print('Valor total de KM rodado: {:.2f}' .format(auxValorKmRodado))
print('VALOR TOTAL A PAGAR PELO ALUGUEL DO CARRO: {:.2f}' .format(valorTotalPagarAluguel))