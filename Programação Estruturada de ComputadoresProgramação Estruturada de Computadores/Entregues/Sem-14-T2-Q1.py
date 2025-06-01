def main():
    #ENTRADA DE DADOS
    numeros = []
    print('Digite 10 números inteiros:')
    for i in range(10):
        numero = int(input())
        numeros.append(numero)

    #PROCESSAMENTO DE DADOS
    maior_numero = max(numeros)
    posicao_maior = numeros.index(maior_numero)

    #SAIDA DE DADOS
    # Imprime os resultados
    print('A lista de números é:', numeros)
    print(f'O maior elemento é {maior_numero} e ele se encontra na posição {posicao_maior}.')

if __name__=="__main__":
   main()