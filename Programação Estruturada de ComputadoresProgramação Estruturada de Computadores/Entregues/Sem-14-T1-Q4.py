def main():
		#INICIALIZAÇÃO DE DADOS
		# Inicializa listas para armazenar os nomes e as alturas dos jogadores
		nomes = []
		alturas = []
		
		#PROCESSAMENTO DE DADOS
		# Lê o nome e a altura de 12 jogadores
		for i in range(12):
			#ENTRADA DE DADOS
		    nome = input(f'Digite o nome do jogador {i + 1}: ').strip()
		    altura = float(input(f'Digite a altura de {nome} em metros: ').strip())
		    nomes.append(nome)
		    alturas.append(altura)
		
		# a. Encontra o jogador mais alto
		indice_maior = alturas.index(max(alturas))
		nome_jogador_mais_alto = nomes[indice_maior]
		altura_jogador_mais_alto = alturas[indice_maior]
		
		# b. Calcula a média de altura do time
		media_altura = round(sum(alturas) / len(alturas),2)
		
		# c. Lista os jogadores com altura superior à média
		jogadores_acima_media = [(nomes[i], alturas[i]) for i in range(len(alturas)) if alturas[i] > media_altura]
		
		#SAÍDA DE DADOS
		# Exibe os resultados
		print("JOGADOR MAIS ALTO DO TIME")
		print(f'O jogador mais alto é {nome_jogador_mais_alto} com altura de {altura_jogador_mais_alto} metros.')
		print(f'A média de altura do time é {media_altura:.2f} metros.')
		print('Jogadores com altura superior à média:')
		print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
		for jogador in jogadores_acima_media:
		    print(f'{jogador[0]}')
		    print(f'{jogador[1]:.2f}')
	
if __name__=="__main__":
   main()