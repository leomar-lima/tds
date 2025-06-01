import datetime
import random

class CartaoEmbarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data_hora_embarque):
        self._validar_codigo_reserva(codigo_reserva)
        self._validar_data_hora_embarque(data_hora_embarque)
        
        self.__nome_passageiro = nome_passageiro
        self.__numero_voo = numero_voo
        self.__codigo_reserva = codigo_reserva
        self.__data_hora_embarque = data_hora_embarque
        self.__status_checkin = False
        self.__assento = None
        self.__assentos_disponiveis = list(range(1, 31))  # Considerando 30 assentos

    @property
    def nome_passageiro(self):
        return self.__nome_passageiro

    @property
    def numero_voo(self):
        return self.__numero_voo

    @property
    def codigo_reserva(self):
        return self.__codigo_reserva

    @property
    def data_hora_embarque(self):
        return self.__data_hora_embarque

    @property
    def status_checkin(self):
        return self.__status_checkin

    @property
    def assento(self):
        return self.__assento

    def realizar_checkin(self):
        if not self.__status_checkin:
            self.__status_checkin = True
            self.__assento = random.choice(self.__assentos_disponiveis)
            self.__assentos_disponiveis.remove(self.__assento)
            print(f"Check-in realizado com sucesso! Assento atribuído: {self.__assento}")
        else:
            print("Check-in já realizado.")

    def alterar_assento(self, novo_assento):
        if self.__status_checkin:
            if novo_assento in self.__assentos_disponiveis:
                self.__assentos_disponiveis.append(self.__assento)
                self.__assentos_disponiveis.remove(novo_assento)
                self.__assento = novo_assento
                print(f"Assento alterado com sucesso para {self.__assento}!")
            else:
                print("Assento indisponível.")
        else:
            print("Realize o check-in antes de alterar o assento.")

    @staticmethod
    def _validar_codigo_reserva(codigo_reserva):
        if len(codigo_reserva) != 6 or not codigo_reserva.isalnum():
            raise ValueError("Código de reserva inválido. Deve ter 6 caracteres alfanuméricos.")

    @staticmethod
    def _validar_data_hora_embarque(data_hora_embarque):
        if data_hora_embarque < datetime.datetime.now():
            raise ValueError("Data e hora de embarque não podem ser retroativas.")

def main():
    cartao1 = CartaoEmbarque("João Silva", "AZ123", "ABC123", datetime.datetime(2024, 12, 29, 10, 0))
    cartao2 = CartaoEmbarque("Maria Santos", "AZ456", "DEF456", datetime.datetime(2024, 12, 30, 12, 0))
    cartao3 = CartaoEmbarque("Pedro Oliveira", "AZ789", "GHI789", datetime.datetime(2024, 12, 31, 14, 0))

    print(cartao1.nome_passageiro, cartao1.numero_voo, cartao1.codigo_reserva, cartao1.data_hora_embarque)

    cartao1.realizar_checkin()
    cartao1.alterar_assento(15)
    cartao2.realizar_checkin()
    cartao3.realizar_checkin()
    cartao3.alterar_assento(20)

    print(f'{cartao1.nome_passageiro} Assento:{cartao1.assento}\n{cartao2.nome_passageiro} Assento:{cartao2.assento}\n{cartao3.nome_passageiro} Assento:{cartao3.assento}')

if __name__ == "__main__":
    main()