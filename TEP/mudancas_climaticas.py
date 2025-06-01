import numpy as np

def exibir_primeiras(dataset,n):
    print(dataset[:n])

def medias_por_cidade(dataset,i):
    return {str(cidade): sum(float(parametro[i]) for parametro in dataset if parametro[1] == cidade)/sum(1 for parametro in dataset if parametro[1] == cidade) for cidade in list(set(cidades[1] for cidades in dataset))}

def maior_medias_temperatura(data):
    print(data)
    return  f"Indice: {[i for i, cidade in enumerate(data) if cidade == max(data,key=data.get)]}"

def cidade_maior_CO2(dataset):
    lista_CO2 = []
    for i in dataset:
        lista_CO2.append(i[3])
    return [data for data in dataset if data[3] == max(lista_CO2)]

def para_Fahrenheit(dataset):
    for temperatura in dataset:
        temperatura[2] = (float(temperatura[2]) * (9/5))+32
    return dataset

def main():
    dataset = np.genfromtxt("mudancas_climaticas.csv", delimiter=",", skip_header=1, dtype=str)
    
    print("Exiba as primeiras 5 linhas do dataset.")
    exibir_primeiras(dataset,5)
    print()
    print("Calcule e exiba a média da temperatura, nível de CO2 e precipitação de todas as cidades.")
    print("Médias de Temperaturas por Cidades:")
    print(medias_por_cidade(dataset,2))
    print("Médias de CO2 por Cidades:")
    print(medias_por_cidade(dataset,3))
    print("Médias de Precipitação por Cidades:")
    print(medias_por_cidade(dataset,4))
    print()
    print("Determine o índice da cidade com a maior temperatura média anual.")
    print(maior_medias_temperatura(medias_por_cidade(dataset,2)))
    print()
    print("Encontre a cidade com o maior nível de CO2 e exiba suas informações completas.")
    print(cidade_maior_CO2(dataset))
    print()
    print("Crie um novo array com os valores de temperatura convertidos para Fahrenheit.")
    print(para_Fahrenheit(dataset))


if __name__ == "__main__":
    main()