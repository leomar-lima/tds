def conjuntos():
    conjunto=[]
    for i in range(5):
        numero = int(input())
        conjunto.append(numero)
    return conjunto


def main():
    # Inicializa listas para armazenar os conjuntos de números
    conjunto_x = conjuntos()
    conjunto_y = conjuntos()
    
    # Calcula o produto escalar e constrói a fórmula
    produto_escalar = 0
    formula = ""

    for i in range(5):
        produto_escalar += conjunto_x[i] * conjunto_y[i]
        if i == 0:
            formula += f"({conjunto_x[i]} x {conjunto_y[i]})"
        else:
            formula += f" + ({conjunto_x[i]} x {conjunto_y[i]})"

    # Imprime os resultados
    print(conjunto_x)
    print(conjunto_y)
    print(f'{formula} = {produto_escalar}')

if __name__=="__main__":
   main()