dados = {}
dados['nome'] = str(input("Nome do jogador: "))
qtPartidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
totalgols = 0
gols = []
for i in range(0, qtPartidas):
    numgols = int(input(f"Quantos gols na partida {i}? "))
    totalgols += numgols
    gols.append(numgols)
dados['gols'] = gols
dados['total'] = totalgols
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}.")
print('-=' * 30)
print(f"O jogador {dados['nome']} jogou {qtPartidas} partidas.")
for i in range(0, qtPartidas):
    print(f"  => Na partida {i}, fez {gols[i]} gols.")
print(f"Foi um total de {totalgols} gols!")

