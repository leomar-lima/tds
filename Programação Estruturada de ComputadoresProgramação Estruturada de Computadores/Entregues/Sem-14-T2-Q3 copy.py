def main():
    numeros = []
    for i in range(20):
        numero = int(input())
        numeros.append(numero)

    numeros_unicos = []
    for numero in numeros:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)

    print(numeros_unicos)

if __name__=="__main__":
   main()