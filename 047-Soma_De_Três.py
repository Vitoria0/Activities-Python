s = 0
co = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        co = co + 1
print('A soma dos {} valores solicitados é {}'.format(co, s))