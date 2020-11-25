jogadores, jogador = [], dict()
repetir = 'S'
while repetir == 'S':
    print('-' * 40)

    while True:
        jogador['Nome'] = input('Nome do jogador: ').capitalize().strip()
        if not jogador['Nome'].isnumeric():
            break
        print('Erro. Digite um nome válido!')

    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = [int(input(f'   Gols {n + 1}ª partida: ')) for n in range(partidas)]

    jogador['Total'] = sum(jogador['Gols'])

    jogador['Média'] = round(jogador['Total'] / partidas, 2)

    jogadores.append(jogador.copy())

    # O copy não faz diferença quando o dicionário é definido novamente.
    # Dessa forma se jogadores = dict() fosse colocado dentro da estrutura de repetição, ou se o dicionário
    # fosse definido com os valores dentro na estrutura de repetição, o copy não seria necessário.

    print('-' * 40)

    repetir = ''
    while len(repetir) != 1 or repetir not in 'SN':
        repetir = input('Cadastrar outro jogador? [S/N] ').upper().strip()
        if len(repetir) != 1 or repetir not in 'SN':
            print('Digite S para Sim e N para Não.')

print('-=' * 30)

# Cria descrição da tabela
print('| cod ', end='')
for k in jogador.keys():
    print(f'| {k:^10} ', end='')
print('|')

print('-' * 59)

# Imprime informação de cada jogador na tabela
for n, j in enumerate(jogadores):

    # 1ª maneira: (Formatação é quebrada a partir de 6 partidas)
    print(f'| {n:^3} ', end='')
    for v in j.values():
        # A função interna isinstance verifica se o valor passado como primeiro argumento é do tipo
        # recebido no segundo argumento => isinstance(value, type)
        if not isinstance(v, list):
            print(f'| {v:^10} ', end='')
        else:
            print(f'| {(" ".join(str(va) for va in v)):^10} ', end='')
    print('|')

    '''
    # 2ª maneira: (Formatação é quebrada a partir de 4 partidas)
    print(f'| {n:^3} | {j["Nome"]:^10} | {str(j["Gols"]):^10} | {j["Total"]:^10} | {j["Média"]:^10} |')
    # Havia formatado a lista de gols para não aparecer os colchetes e vírgulas:
    # (" ".join(str(g) for g in j["Gols"])):^10
    '''

num = 0
while num != 999:
    print('-' * 59)
    num = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    # 1ª solução para mostrar dados usando as funções range e len:
    if num in range(len(jogadores)):
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogadores[num]["Nome"]}:')
        for n, gol in enumerate(jogadores[num]['Gols'], 1):
            print(f'   No {n}º jogo fez {gol} gol(s).')
    elif num != 999:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')

    # 2ª solução c/ Try Except:
    '''
    try:
        assert num >= 0
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[num]["nome"]}')
        for jogo, gol in enumerate(jogadores[num]['gols'], 1):
            print(f'   No jogo {jogo} fez {gol} gols.')
    except:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')
    '''

    # 3ª solução usando for else e break:
    '''
    for n, j in enumerate(jogadores):
        if num == n:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[num]["nome"]}')
            for jogo, gol in enumerate(jogadores[num]['gols'], 1):
                print(f'   No jogo {jogo} fez {gol} gols.')
            break
    else:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')
    '''

print('\n<< VOLTE SEMPRE >>')


# Conforme solução do vídeo:
'''
time = list()
# Não pode fazer partidas = time = list(), pois isso irá criar uma relação entre as listas.
jogador = dict()
partidas = list()
# Ler o dado de vários jogadores (com validação)
while True:
    # jogador.clear()
    # Desnecessário, pois após a primeira iteração os valores anteriores são sobrepostos por novos.
    partidas.clear()
    jogador['nome'] = input('Nome do Jogador: ').capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(tot):
        partidas.append(int(input(f'    Quantos gol(s) na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
# Mostrar os resultados com a análise de dados:
# Faz o cabeçalho, mostrando o nome dos campos
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
# Imrpime a informação de cada jogador
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        # Função str() evita erro na hora de formatar os gols que são uma lista, caso não fosse usada
        # ocorreria erro de tipagem, pois a formatação não funciona com coleções.
        # Com tipos primitivos como numerais isso é desnecessário, pois a formatação é feita normalmente.
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    # Flag (valor de parada)
    if busca == 999:
        break
    # if busca >= len(time):
    # Funciona apenas para valores positivos maiores que o da lista. Se for negativo não funciona.
    # Para resolver isso usei a função range que cria uma lista, e fiz isso em relação ao len(time):
    if busca not in range(len(time)):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols'], 1):
            print(f'    No jogo {i} fez {g} gol(s).')
            # print(f'    No jogo {i+1} fez {g} gols')
            # i+1 é substituído pelo segundo argumento passado na função enumerate que se refere ao valor
            # inicial que terá os índices atribuídos à lista.
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
'''