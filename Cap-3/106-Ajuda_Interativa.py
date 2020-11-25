def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tamanho = len(msg) +4
    print('~' * tamanho)
    print(msg)
    print('~' * tamanho)


#------Programa Principal

comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PYHELP')
    comando = str(input("Função ou biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('  ATÉ LOGO')