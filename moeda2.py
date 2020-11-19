def aumentar(preço=0, taxa=0):
    resp = preço + (preço * taxa/100)
    return resp

def diminuir(preço=0, taxa=0):
    resp = preço - (preço * taxa/100)
    return resp

def dobro(preço=0):
    resp = preço * 2
    return resp

def metade(preço=0):
    resp = preço / 2
    return resp

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')