def main():
    #ENTRADA DE DADOS
    numeros = []
    print('Digite 10 números reais:')
    for i in range(10):
        numero = int(input())
        numeros.append(numero)

    #PROCESSAMENTO DE DADOS
    negativos = 0
    soma_positivos = 0
    for numero in numeros:
        if numero < 0:
            negativos += 1
        else:
            soma_positivos += numero
    
    #SAÍDA DE DADOS
    # Imprime os resultados
    print('A lista de números é:', numeros)
    print(f'Quantidade de números negativos: {negativos}')
    print(f'Soma dos números positivos: {soma_positivos}')

if __name__=="__main__":
   main()