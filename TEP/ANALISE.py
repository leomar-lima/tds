import numpy as np

np.random.seed(42) # Para resultados reproduzíveis ele nao muda os valores ramdom mesmo inicializando o programa vairas vezes

# criando un dataset de vendas
ids = np.arange(1, 11) # IDs de 1 a 10
precos = np.random.randint(20, 200, size=10) # Preços entre R$20 e R$200
vendas_a = np.random.randint(50, 500, size=10) # Vendas na Região A
vendas_b = np.random.randint(30, 400, size=10) # Vendas na Região B
custos = np.random.randint(10, 150, size=10) # Custos entre R$10 e R$150

dataset = np.column_stack((ids, precos, vendas_a, vendas_b, custos))

    
def MediaVendas(dataset):
    
    MediaVendasA = np.mean([vendaA[2] for vendaA in dataset ])
    MediaVendaB = np.mean([vendasB[3] for vendasB in dataset])
    
    return MediaVendasA, MediaVendaB

def Mediana(dados):
    
    MedianaA = np.median([vendas[2] for vendas in dados])
    MedianaB = np.median([vendas[3] for vendas in dados])

    return MedianaA,MedianaB

def DesvioPadrao(dados):
    
    DesvioPadraoA = np.std([vendas[2] for vendas in dados])
    DesvioPadraoB = np.std([vendas[3] for vendas in dados])
    
    return DesvioPadraoA,DesvioPadraoB    

def ReceitaTotal(dados):
    
    ReceitaTotalA = np.sum([vendas_a[1]*vendas_a[2] for vendas_a in dados])
    ReceitaTotalB = np.sum([vendas_b[1]*vendas_b[3] for vendas_b in dados])
    
    return ReceitaTotalA,ReceitaTotalB

def ProdutoMaiorMargemLucro(dados):
    
    MargemLucro = np.argmax([venda[1] - venda[4] for venda in dados])
    # Ele retorna o indice do produto com maior margem de lucro
    # soma-se o resultado +1 para retornar o id do produto
    
    return MargemLucro
    

def AdicionarColuna(dataset):
    
    ReceitaTotalA = np.array([vendas_a[1]*vendas_a[2] for vendas_a in dataset])
    ReceitaTotalB = np.array([vendas_b[1]*vendas_b[3] for vendas_b in dataset])


    ReceitaTotal = np.array([ReceitaTotalA[i] + ReceitaTotalB[i] for i in range(len(ReceitaTotalA)) ])
    dataset = np.column_stack((dataset,ReceitaTotal))
    
    return dataset

def FiltroPorValor(dataset,valor):
    
    filtro = {}
    
    for linha in dataset:
        filtro[f'Produtos acima de {valor}'] = [produto[0] for produto in dataset if produto[5] > valor]
        
    return filtro


def OrdenarDataset(dataset,crescente=True):
     
    if crescente:
        ordenar_indice = np.argsort(dataset[:,5])
    else:
        ordenar_indice = np.argsort(dataset[:,5])[::-1]
        #invertende a ordem do array, especificado pela coluna 5
        
    dataset_ordenado = dataset[ordenar_indice]
    
    return dataset_ordenado


    
# resultados:
    
print("Dataset de Vendas:\n", dataset)

print()

print(f'Formato do dataset: {dataset.shape}')

print()

print(f'Tipo de dadosd do dataset : {dataset.dtype}')

print()

print(f'Valores minimos de cada coluna: {np.min(dataset,axis=0)}')

print(f'Valores máximos de cada coluna: {np.max(dataset,axis=0)}')

print()


print(f'Media de vendas de A: {MediaVendas(dataset)[0]}\nMedia de vendas de B: {MediaVendas(dataset)[1]}')

print()

print()

print(f'Mediana de vendas A: {Mediana(dataset)[0]}\nMediana de vendas B: {Mediana(dataset)[1]}')

print()

print()

print(f'Desvio padrao de A: {DesvioPadrao(dataset)[0]}\nDevio padrao de B: {DesvioPadrao(dataset)[1]}')

print()

print(f'Receita total A: {ReceitaTotal(dataset)[0]}\nReceita total B: {ReceitaTotal(dataset)[1]}')

print()

print(f'Produto com maior margem de lucro: {ProdutoMaiorMargemLucro(dataset)+1}')

print()

novo_dataset = AdicionarColuna(dataset)
print(novo_dataset)


print()

filtrar = FiltroPorValor(novo_dataset, 50000)
for chave, valor in filtrar.items():
    print(f'{chave}: {valor}')

print()


#colocar o dataset em ordem, pela  receita total (decrecente)
print(OrdenarDataset(dataset=novo_dataset,crescente=False))