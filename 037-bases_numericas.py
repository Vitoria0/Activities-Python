# Apresentando um número para converção
n = int(input('Digite um número inteiro: '))

# Menu
print(''' Escolha uma das bases para converção:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')

# Escolhendo opção do menu
o = int(input('Sua opção: '))

# Funcionalidades menu
if o == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido em octal é igual a {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida!')
print('Obrigada pela preferencia! Volte sempre!')
