def main():
	#INICIALIZAÇÃO DE DADOS
	a = []
	b = []
	c = []
	
	#PROCESSAMENTO DE DADOS
	for i in range(20):
		#ENTRADA DE DADOS
	    a.append(int(input(f'Digite {i + 1} item da lista A: ')))
	for i in range(20):
		#ENTRADA DE DADOS
	    b.append(int(input(f'Digite {i + 1} item da lista B: ')))
	
	for i in range(20):
	    c.append(a[i]+b[i])

	#SAÍDA DE DADOS
    #Imprime as listas	
	print(f'Lista A: {a}')
	print(f'Lista B: {b}')
	print(f'Lista C: {c}')
		
if __name__=="__main__":
   main()