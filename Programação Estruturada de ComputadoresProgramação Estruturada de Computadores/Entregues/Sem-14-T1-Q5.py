def main():
	#INICIALIZAÇÃO DE DADOS
	nomes = []
	idades = []
	alturas = []
	
	#PROCESSAMENTO DE DADOS
	for i in range(30):
		#ENTRADA DE DADOS
	    nome = input(f'Nome do aluno {i+1}: ')
	    idade = int(input(f'Idade de {nome}: '))
	    altura = float(input(f'Altura de {nome} em metros: '))
	    nomes.append(nome)
	    idades.append(idade)
	    alturas.append(altura)
	
	media_altura = round(sum(alturas) / len(alturas),2)
	
	alunos_acima_13_abaixo_media = []
	for i in range(len(idades)):
	    if idades[i] > 13 and alturas[i] < media_altura:
	        alunos_acima_13_abaixo_media.append((nomes[i], alturas[i]))
	
	#SAÍDA DE DADOS
	print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
	for aluno in alunos_acima_13_abaixo_media:
	    print(f'{aluno[0]}')
	
if __name__=="__main__":
   main()