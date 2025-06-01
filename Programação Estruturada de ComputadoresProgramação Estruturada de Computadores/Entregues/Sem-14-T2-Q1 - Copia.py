def main():
    numeros = []
    for i in range(10):
        numero = int(input())
        numeros.append(numero)

    print(numeros)
    maior_numero = max(numeros)
    posicao_maior = numeros.index(maior_numero)

    print(f'{maior_numero}')
    print(f'{posicao_maior}')

if __name__=="__main__":
   main()