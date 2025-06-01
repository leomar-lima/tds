class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.__volume_min=0
        self.__volume_max=vol_max
        self.__freq_min=88
        self.__freq_max=108
        self.__estacoes = estacoes
        self.__volume=None
        self.__ligado=False
        self.__estacao_atual=None
        self.__frequencia_atual=None
        self.__antena_habilitada=False
    
    def __primeira_estacao(self):
        if self.__antena_habilitada:
            primeira_estacao = list(self.__estacoes.keys())[0]
            self.__frequencia_atual = primeira_estacao
            self.__estacao_atual = self.__estacoes[primeira_estacao]

    
    def ligar(self):
        self.__ligado=True
        self.__antena_habilitada=True
        self.__volume= self.__volume_min
        self.__primeira_estacao()
        

    def desligar(self):
        self.__ligado = False
        self.__antena_habilitada = False
        self.__volume = None
        self.__frequencia_atual = None
        self.__estacao_atual=None
   
    
    def aumentar_volume(self, valor=1):
        if not self.__ligado:
            print("Rádio desligado.")
            return
        if self.__volume is None:
            self.__volume = self.__volume_min
        if valor:
            self.__volume = min(self.__volume + valor, self.__volume_max)
        else:
            self.__volume = min(self.__volume + 1, self.__volume_max)
        volume_alerta = 0.8*self.__volume_max
        if self.__volume>volume_alerta and self.__volume-valor<volume_alerta:
            print("A audição em volume elevado por períodos longos pode prejudicar sua audição.")
        print(f"Volume: {self.__volume}")


    def diminuir_volume(self, valor=1):
        if not self.__ligado:
            print("Rádio desligado.")
            return
        if self.__volume is None:
            self.__volume = self.__volume_min
        if valor:
            self.__volume = max(self.__volume - valor, self.__volume_min)
        else:
            self.__volume = max(self.__volume - 1, self.__volume_min)
        print(f"Volume: {self.__volume}")

    def mudar_frequencia(self, frequencia=None):
        if not self.__ligado:
            print("Rádio desligado.")
            return

        if frequencia:
            if frequencia in self.__estacoes:
                self.__frequencia_atual = frequencia
                self.__estacao_atual = self.__estacoes[frequencia]
            else:
                print(f"Frequencia: {frequencia}, Estação inexistente. Seguindo para a próxima estação.")
                estacoes = list(self.__estacoes.keys())
                for i in estacoes:
                    if frequencia>estacoes[0]:
                        self.__frequencia_atual = i
                        self.__estacao_atual = self.__estacoes[i]
                        if i>frequencia:
                            break
                    else:
                        self.__primeira_estacao()

        print(f"Frequência: {self.__frequencia_atual}, Estação: {self.__estacao_atual}")



def main():
    estacoes = {89.5:'Cocais',91.5:'Mix',94.1:'Boa',99.1:'Club'}
    radio1 = RadioFM(100,estacoes)
    radio2 = RadioFM(100,estacoes)
    radio3 = RadioFM(100,estacoes)
    
    radio1.ligar()
    radio1.aumentar_volume()
    radio1.aumentar_volume(5)
    radio1.mudar_frequencia()
    radio1.mudar_frequencia(99.1)
    radio1.desligar()
    
    radio2.ligar()
    radio2.diminuir_volume()
    radio2.diminuir_volume(3)
    radio2.mudar_frequencia()
    radio2.mudar_frequencia(90.5)
    
    radio3.ligar()
    radio3.aumentar_volume(10)
    radio3.mudar_frequencia(94.1)
    radio3.desligar()

    radio2.aumentar_volume(100)
    radio2.aumentar_volume(10)
    radio2.diminuir_volume(20)
    radio2.diminuir_volume(5)
    radio2.aumentar_volume(6)
    radio2.mudar_frequencia(88)
    radio2.mudar_frequencia(100)
    radio2.desligar()




if __name__ == "__main__":
    main()