lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? S/N: ')).upper()
    if r in 'N':
        print(f'Você digitou {len(lista)} valores')
        lista.sort(reverse=True)
        print(f'A ordem decrescente desses valores é: {lista}')
        if 5 in lista:
            print('O valor 5 faz parte da lista!')
        else:
            print('O número 5 não foi digitado!')
        break
    if r in 'S':
        continue
    else:
        print('Resposta inválida! Tente novamente')