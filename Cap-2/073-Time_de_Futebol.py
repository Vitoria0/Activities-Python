#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Bahia.

brasileirao = ('Internacional', 'Atletico-MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras',
               'Santos', 'Grêmio', 'Sport Recife', 'Corinthians', 'Fortaleza', 'Ceará SC',
               'Atletico-GO', 'Bahia', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Vasco',
               'Athletico-PR', 'Goias')

print(f'Lista de times do Brasileirão: {brasileirao}')
print('~'*90)
print(f'Os cinco primeiros times são: {brasileirao[0:5]}')
print('~'*90)
print(f'Os quatro ultimos colocados são: {brasileirao[16:]}')
print('~'*90)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('~'*90)
print(f'O time da Bahia está na {brasileirao.index("Bahia")+1} posição')