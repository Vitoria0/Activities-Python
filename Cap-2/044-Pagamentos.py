from time import sleep
print(f'{" AVON ":=^30}')
Preco = float(input('Digite o preço: R$:'))
Pagamento = int(input('Digite o método de pagamento: \n 1: à vista dinheiro/cheque \n 2: à vista cartão \n 3: 2x cartão \n 4: 3x ou + cartão \n '))

if Pagamento == 1:
    print('Pagamento à vista: dinheiro/cheque... ')
    sleep(1)
    print(f'Preço = R$:{Preco*0.9:.2f}')
elif Pagamento == 2:
    print('Pagamento à vista: cartão... ')
    sleep(1)
    print(f'Preço = R$:{Preco*0.95:.2f}')
elif Pagamento == 3:
    print('Pagamento em 2x no cartão... ')
    sleep(1)
    print(f'Preço = R$:{Preco:.2f}')
elif Pagamento == 4:
    print('Pagamento em 3x ou mais no cartão... ')
    sleep(1)
    print(f'Preço = R$:{Preco*1.2:.2f}')
else:
    print('Operação inválida.')
print('Obrigado pela preferencia, volte sempre!')