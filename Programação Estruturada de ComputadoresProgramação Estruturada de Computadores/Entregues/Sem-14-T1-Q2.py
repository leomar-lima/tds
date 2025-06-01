#PROCESSAMENTO DE DADOS
def count(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

def main():
	#INICIALIZAÇÃO DE DADOS
	valores=[]

	#ENTRADA DE DADOS
	while True:
	    valor = int(input("Digite um número inteiro (0 para terminar): "))
	    if(valor==0):
	    	break
	    valores.append(valor)
	   
	pesquisado=int(input("Digite o número a ser pesquisado: "))
	
	#SAÍDA DE DADOS
	#Imprime os resultados
	print(f'Lista de valores: {valores}')
	print(f'Numero pesquisado: {pesquisado}')
	print(f'Quantidade de repetições na lista: {count(valores,pesquisado)}')
	
	
if __name__=="__main__":
   main()