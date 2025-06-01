import numpy as np

def gerar_dados():
    # Gerar dados aleatórios
    np.random.seed(42) # Para resultados reproduzíveis
    ids = np.arange(1, 11) # IDs de 1 a 10
    precos = np.random.randint(20, 200, size=10) # Preços entre R$20 e R$200
    vendas_a = np.random.randint(50, 500, size=10) # Vendas na Região A
    vendas_b = np.random.randint(30, 400, size=10) # Vendas na Região B
    custos = np.random.randint(10, 150, size=10) # Custos entre R$10 e R$150
    # Criar o dataset como um array
    return np.column_stack((ids, precos, vendas_a, vendas_b, custos))

def media_mediana_desvio(dataset,col):
    return f"Média: {np.mean(dataset[:, col])}\nMediana: {np.median(dataset[:, col])}\nDesvio padrão: {np.std(dataset[:, col])}"



def main():
    dataset = gerar_dados()

    # Exibir o dataset
    print(f"Dataset de Vendas:\n{dataset}")

    #1. Exploração de Dados
    #Imprima o formato do array (número de linhas e colunas).
    print(f"\nFormato do array: {dataset.shape}")
    #Verifique o tipo dos dados no array.
    print(f"Tipo dos dados: {dataset.dtype}")
    #Encontre o valor mínimo e máximo de cada coluna.
    print(f"Valor mínimo de cada coluna: {dataset.min(axis=0)}")
    print(f"Valor máximo de cada coluna: {dataset.max(axis=0)}")

    #2. Cálculos Estatísticos
    #Calcule a média, mediana e desvio padrão das vendas em cada região.
    print(f"\nVendas na Região A:\n{media_mediana_desvio(dataset, 2)}")
    print(f"\nVendas na Região B:\n{media_mediana_desvio(dataset, 3)}")
    #Determine a receita total de vendas para cada região (preço × quantidade vendida).
    receita_A = dataset[:, 1] * dataset[:, 2]
    receita_B = dataset[:, 1] * dataset[:, 3]
    print(f"\nReceita total na Região A: {np.sum(receita_A)}")
    print(f"Receita total na Região B: {np.sum(receita_B)}")
    #Identifique o produto com maior margem de lucro (Preço - Custo).
    produto_maior_lucro = np.argmax(dataset[:, 1] - dataset[:, 4])
    print(f"Produto com maior margem de lucro: {dataset[produto_maior_lucro, :]}, com índice {produto_maior_lucro} no Dataset.")

    #3. Manipulação de Dados
    #Adicione uma coluna de "Receita Total" ao dataset (soma das receitas das Regiões A e B).
    receita_total = receita_A + receita_B
    dataset = np.column_stack((dataset, receita_total))
    print(f"\nDataset com coluna de Receita Total:\n{dataset}")
    #Filtre apenas os produtos com receita total acima de R$10.000.
    produtos_maior_10K = dataset[dataset[:, 5] > 10000]
    print(f"\nProdutos com Receita Total acima de R$10.000:\n{produtos_maior_10K}")

    #4. Visualização de Insights
    #Ordene o dataset pela receita total (em ordem decrescente).
    dataset_receita_ord_dec = dataset[np.argsort(dataset[:, 5])[::-1]]
    print(f"\nDataset ordenado por Receita Total (em ordem decrescente):\n{dataset_receita_ord_dec}")
    #Encontre a região com maior volume de vendas.
    total_vendas_A = np.sum(dataset[:, 2])
    total_vendas_B = np.sum(dataset[:, 3])
    print()
    if total_vendas_A > total_vendas_B:
        print("A Região A possui o maior volume de vendas.")
    elif total_vendas_B > total_vendas_A:
        print("A Região B possui o maior volume de vendas.")
    else:
        print("As Regiões A e B possuem o mesmo volume de vendas.")




if __name__ == '__main__':
    main()