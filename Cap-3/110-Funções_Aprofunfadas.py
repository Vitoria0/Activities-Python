def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Número digitado não é valido')
            continue
        else:
            return n


num = leia_int('Digite um valor: ')
print(f'O valor digitadi foi {num}')