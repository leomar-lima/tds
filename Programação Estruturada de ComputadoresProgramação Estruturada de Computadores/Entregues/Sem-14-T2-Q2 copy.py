def main():
    numeros = []
    for i in range(10):
        numero = int(input())
        numeros.append(numero)

    print(numeros)
    negativos = 0
    soma_positivos = 0
    for numero in numeros:
        if numero < 0:
            negativos += 1
        else:
            soma_positivos += numero

    print(f'{negativos}')
    print(f'{soma_positivos}')

if __name__=="__main__":
   main()