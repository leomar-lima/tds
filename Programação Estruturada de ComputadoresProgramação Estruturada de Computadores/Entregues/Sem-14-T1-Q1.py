#a) Função comprimento():
def comprimento(lista):
    contador = 0
    for item in lista:
        contador += 1
    return contador

#b) Função inverter():
def inverter(lista):
    nova_lista = []
    for item in lista:
        nova_lista.insert(0, item)
    return nova_lista

#c) Função minimo():
def minimo(lista):
    if not lista:
        return None
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

#d) Função maximo():
def maximo(lista):
    if not lista:
        return None
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

#e) Função soma():
def soma(lista):
    total = 0
    for item in lista:
        total += item
    return total

def main():
    #INICIALIZAÇÃO DE DADOS
	valores=[]

    #PROCESSAMENTO DE DADOS
	while True:
        #ENTRADA DE DADOS
	    valor = int(input("Digite um número inteiro (0 para terminar): "))
	    if(valor==0):
	    	break
	    valores.append(valor)

	#SAÍDA DE DADOS
    #Imprime os resultados
	print(f'Lista de valores: {valores}')
	print(f'Comprimento da lista: {comprimento(valores)}')
	print(f'Lista invertida: {inverter(valores)}')
	print(f'Valor minimo da lista: {minimo(valores)}')
	print(f'Valor maximo da lista: {maximo(valores)}')
	print(f'Soma dos valores da lisat: {soma(valores)}')
	
	
if __name__=="__main__":
   main()