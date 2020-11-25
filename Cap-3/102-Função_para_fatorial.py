def fatorial(numero,show=0):
    from math import factorial
    fatorial_numero = factorial(numero)
    print(f'O fatorial de {numero} é {fatorial_numero}.')

    if show==1:
        print('O cálculo desse fatorial é:')
        for c in range(numero,0,-1):
            print(f'{c}',end='')
            if c > 1:
                print('.',end='')
            else:
                print('=',end='')
        print(fatorial_numero)
    else:
        print('Cálculo não exibido.')

#Programa Principal
numero = int(input('Informe um número inteiro para o cálculo de seu fatorial:'))
show = int(input('Deseja ver o cálculo desse fatorial [0/1]?'))
if show != 1 and show !=0:
    show = int(input('Opção inválida.Deseja ver o cálculo desse fatorial [0/1]?'))

fatorial(numero,show)