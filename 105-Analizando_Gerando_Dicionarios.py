def notas(*n, sit=False):
    """
    -> Analiza notas e situações
    :param n: uma ou mias notas (aceita varias)
    :param sit: opcional, indicando se deve ou não adcionar a situação
    :return: dicionario com varias informações
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r ['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'ruim'
    return r


#------Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)