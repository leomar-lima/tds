#Cria o conjunto de mumeros
def conjuntos():
    conjunto=[]
    for i in range(10):
        numero = int(input())
        conjunto.append(numero)
    return conjunto

def main():
    #ENTRADA DE DADOS
    # Inicializa listas para armazenar os conjuntos de números
    lista1 = conjuntos()
    lista2 = conjuntos()
    # Cria a lista união sem duplicatas
    lista_uniao = []

    #PROCESSAMENTO DE DADOS
    # Adiciona elementos da primeira lista
    for elemento in lista1:
        if elemento not in lista_uniao:
            lista_uniao.append(elemento)

    # Adiciona elementos da segunda lista
    for elemento in lista2:
        if elemento not in lista_uniao:
            lista_uniao.append(elemento)

    #SAÍDA DE DADOS

    print('Lista união:', lista_uniao)

if __name__=="__main__":
   main()