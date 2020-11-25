from time import sleep

def contador(i, f, p):
    print(f'Conatgem de {i} até {f} de {p} em {p}')
    print('-' * 31)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.8)
            cont += p
        print('FIM!')
        print('-' * 31)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        print('-' * 31)

#P.P
contador(1, 10, 1)
contador(10, 0, 2)