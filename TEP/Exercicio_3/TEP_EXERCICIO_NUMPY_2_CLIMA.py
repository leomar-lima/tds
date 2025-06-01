import numpy as np

def media(dados:list):
    return [np.mean(i[i!=999.9]) for i in dados if len(i[i!=999.9])>0]
def meses(n):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[n] if 0 <= n < len(meses) else None
class Station():
    def __init__(self, endereco=str):
        self.__nome= endereco.split("station_")[1].replace(".csv","").upper()
        self.__dataset = np.loadtxt(endereco, delimiter=",", skiprows=1)
        self.__dataset_temperatura = self.__dataset[:,1:13]

    @property
    def nome(self):
        return self.__nome
    
    def Mes_Quente_Frio(self):
        return f'Cidade: {self.nome}, Mês mais Quente: {meses(np.argmax(media(self.__dataset_temperatura.T)))}, Mês mais Frio: {meses(np.argmin(media(self.__dataset_temperatura.T)))}'

    def qtd_meses_menor_temp(self, temp:int):
        return f'Cidade: {self.nome}: {sum(1 for i in self.__dataset_temperatura if len(i[(i<temp)&(i!=999.90)])>0)} meses'

    def qtd_meses_maior_temp(self, temp:int):
        return f'Cidade: {self.nome}: {sum(1 for i in self.__dataset_temperatura if len(i[(i>temp)&(i!=999.90)])>0)} meses'

    def calcular_media_temp_periodo(self,ano_inicio:int, ano_final:int):
        return  f'Cidade: {self.nome}: {float(media(self.__dataset[np.where((self.__dataset>=ano_inicio)&(self.__dataset<=ano_final)),-1])[0])}'

    def std_med_temp(self):
        media_temp = self.__dataset[:,-1]
        return np.std(media_temp[media_temp!=999.9])
    

def main():
    pasta = "Exercicio_3/"
    cidades = ["belem", "curitiba", "fortaleza", "goiania", "macapa", "manaus",
               "recife", "rio", "salvador", "sao_luiz", "sao_paulo", "vitoria"]
    estacoes = {cidade: Station(f"{pasta}/station_{cidade}.csv") for cidade in cidades}

    print("Encontre o mês mais quente e o mês mais frio em todo o período para cada cidade.")

    for cidade in estacoes.values():
        print(cidade.Mes_Quente_Frio())
    
    print("\nDetermine o número de meses em que a temperatura foi abaixo de 20°C para cada cidade.")
    for cidade in estacoes.values():
        print(cidade.qtd_meses_menor_temp(20))

    print("\nDetermine o numero de meses em que a temperatura foi acima de 38° para cada cidade")
    for cidade in estacoes.values():
        print(cidade.qtd_meses_maior_temp(38))

    print("\nCalcule a média de temperatura de todas as cidades entre os anos de 2000 a 2019.")
    for cidade in estacoes.values():
        print(cidade.calcular_media_temp_periodo(2000,2019))
    
    print("\nIdentifique a cidade com a maior variação de temperatura ao longo do período analisado.")
    desvio_padrao = []
    for cidade in estacoes.values():
        desvio_padrao.append(cidade.std_med_temp())
    print(f'Cidade: {cidades[np.argmax(desvio_padrao)].upper()}')



if __name__ == "__main__":
    main()