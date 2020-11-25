exp = str(input('Digite uma expressão: '))
pa = 0
pf = 0
for a in list(exp):
    if a == '(':
        pa += 1
    if a == ')':
        pf += 1
if pa == pf:
    print('Expessão válida!')
else:
    print('Expressão inválida!')