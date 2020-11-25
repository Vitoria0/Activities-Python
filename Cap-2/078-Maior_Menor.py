num = []
maior = 0
menor = 0
for c in range (0, 5):
    num.append(int(input(f'Digite um número para a {c} posição: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num < menor:
            menor = num[c]

print('~' * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior}')
print(f'E o menor valor digitado foi {menor}')