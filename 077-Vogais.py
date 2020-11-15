#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

texto = ('preparem-se', 'pois', 'esta', 'na', 'hora', 'vamos', 'aprender', 'ler', 'escrever', 'desenhar', 'com', 'estes', 'livrinhos', 'divertidos')
vogais = ('a', 'e', 'i', 'o', 'u')

#"palavra" recebe um índice por vez de "texto".
for palavra in range(0, len(texto)):
	print(f'\nNa palavra {texto[palavra].upper()} temos: ', end='')
	#"letra" recebe um índice por vez de "palavra". ele irá varrer um letra por vezes, depois passa para a próxima palavra.
	for letra in texto[palavra]:
		#"teste" recebe a vogal do momento, fazendo um loop pela tuplas "vogais".
		for teste in vogais:
			#testar se a vogal "teste" é igual a "letra".
			if teste == letra:
				print(f'{teste} ', end='')