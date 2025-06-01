from datetime import datetime

class CarteiraHabilitacao:
    def __init__(self, numero_registro, nome, data_nascimento, categoria, data_emissao, data_validade):
        self.validar_data_nascimento(data_nascimento)
        self.validar_categoria(categoria)
        self.validar_datas_emissao_validade(data_emissao, data_validade)
        
        self.__numero_registro = numero_registro
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__categoria = categoria
        self.__data_emissao = data_emissao
        self.__data_validade = data_validade
        self.__situacao = "Ativa"
        self.__pontos = 0

    @property
    def numero_registro(self):
        return self.__numero_registro

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def categoria(self):
        return self.__categoria

    @property
    def data_emissao(self):
        return self.__data_emissao

    @property
    def data_validade(self):
        return self.__data_validade

    @property
    def situacao(self):
        return self.__situacao

    @property
    def pontos(self):
        return self.__pontos

    def suspender(self):
        if self.__situacao == "Ativa":
            self.__situacao = "Suspensa"
            print("Carteira suspensa.")
        else:
            print("Carteira já está suspensa ou cancelada.")

    def cancelar(self):
        if self.__situacao == "Ativa" or self.__situacao == "Suspensa":
            self.__situacao = "Cancelada"
            print("Carteira cancelada.")
        else:
            print("Carteira já está cancelada.")

    def adicionar_pontos(self, pontos):
        if self.__situacao == "Ativa":
            self.__pontos += pontos
            print(f"{pontos} pontos adicionados.")
        else:
            print("Carteira não está ativa.")

    def __str__(self):
        return f"Carteira de Habilitação nº {self.numero_registro}\nNome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nCategoria: {self.categoria}\nData de Emissão: {self.data_emissao}\nData de Validade: {self.data_validade}\nSituação: {self.situacao}\nPontos: {self.pontos}"

    def __validar_data_nascimento(data_nascimento):
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        idade = (datetime.now() - data_nascimento).days / 365.25
        if idade < 18:
            raise ValueError("Idade mínima para obter carteira de habilitação é 18 anos.")

    @staticmethod
    def validar_categoria(categoria):
        categorias_validas = ["A","B","C","D","E",AB", "AC", "AD","AE"]
        if categoria not in categorias_validas:
            raise ValueError("Categoria inválida.")

    @staticmethod
    def validar_datas_emissao_validade(data_emissao, data_validade):
        data_emissao = datetime.strptime(data_emissao, "%d/%m/%Y")
        data_validade = datetime.strptime(data_validade, "%d/%m/%Y")
        if data_validade <= data_emissao:
            raise ValueError("Data de validade deve ser posterior à data de emissão.")

# Testando os métodos
carteira1 = CarteiraHabilitacao("1234567890", "João Silva", "25/02/1990", "B", "10/03/2020", "10/03/2025")
print(carteira1)

carteira1.suspender()
print(carteira1)

carteira1.cancelar()
print(carteira1)

carteira2 = CarteiraHabilitacao("9876543210", "Maria Santos", "15/08/1995", "AB", "20/04/2022", "20/04/2027")
carteira2.adicionar_pontos(5)
print(carteira2)