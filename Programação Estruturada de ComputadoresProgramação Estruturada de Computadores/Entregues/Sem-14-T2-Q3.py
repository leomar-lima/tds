def main():
    #ENTRADA DE DADOS
    numeros = []
    print('Digite 20 números inteiros:')
    for i in range(20):
        numero = int(input())
        numeros.append(numero)

    #PROCESSAMENTO DE DADOS
    numeros_unicos = []
    for numero in numeros:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)

    #SAIDA DE DADOS
    # Imprime os elementos da lista sem repetições
    print('Elementos da lista sem repetições:', numeros_unicos)

if __name__=="__main__":
   main()