#Cria o conjunto de mumeros
def conjuntos():
    conjunto=[]
    for i in range(5):
        numero = int(input())
        conjunto.append(numero)
    return conjunto

def main():
    #ENTRADA DE DADOS
    # Inicializa listas para armazenar os conjuntos de números
    print('Digite 5 números reais para o conjunto X:')
    conjunto_x = conjuntos()
    print('Digite 5 números reais para o conjunto Y:')
    conjunto_y = conjuntos()

    #PROCESSAMENTO DE DADOS
    # Calcula o produto escalar e constrói a fórmula
    produto_escalar = 0
    formula = ""

    for i in range(5):
        produto_escalar += conjunto_x[i] * conjunto_y[i]
        if i == 0:
            formula += f"({conjunto_x[i]} x {conjunto_y[i]})"
        else:
            formula += f" + ({conjunto_x[i]} x {conjunto_y[i]})"
    
    #SAÍDA DE DADOS

    # Imprime os resultados
    print('Conjunto X:', conjunto_x)
    print('Conjunto Y:', conjunto_y)
    print('Produto Escalar:', produto_escalar)

if __name__=="__main__":
   main()