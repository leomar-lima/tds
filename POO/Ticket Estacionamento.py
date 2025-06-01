
from datetime import datetime, timedelta
import random
import math
import string

class Ticket:
    def __init__(self, tikets):
        self.__codigo = self.__gerar_numero(tikets)
        self.__entrada = datetime.now()
        self.__saida = "Sem registo"
        self.__status = "Ativo"
        self.__valor = "R$0.00"
    
    @property
    def codigo(self):
        return self.__codigo
    @property
    def entrada(self):
        return self.__entrada
    @property
    def saida(self):
        return self.__saida
    @property
    def status(self):
        return self.__status
    @property
    def valor(self):
        return self.__valor
    def __gerar_numero(self, tikets):
        while(True):
            codigo = random.sample(string.ascii_letters,3)
            codigo += random.sample(string.digits,5)
            codigo = "".join(random.sample(codigo,8))
            if codigo not in tikets:
                tikets.append(codigo)
                return codigo
            
    def __validar_horario(self,horario):
        try:
            horario = datetime.strptime(horario,"%d/%m/%Y %H:%M")
            if horario < self.__entrada:
                raise ValueError("Horário de saída não pode ser menor que o Horário de entrada.")
            return horario
        except ValueError:
            raise ValueError("Horario inválido!")
    
    def registrar_saida(self,horario):
        if self.__status == "Ativo":
            self.__saida = self.__validar_horario(horario)
            self.__valor= self.__calcular(self.__saida)
            self.__status = "Finalizado"
        return f'Código: {self.__codigo} - Saída registrada.'
    

    def consultar(self,horario):
        if self.__status == "Ativo":
            return f'CONSULTA\nCódigo: {self.__codigo}\nStatus: {self.__status}\nHorário de Entrada: {self.__entrada}\nHorário de Saída: {self.__saida}\nHorário de Consulta: {horario}\nValor: {self.__calcular(self.__validar_horario(horario))}'
        return f'CONSULTA\nCódigo: {self.__codigo} - Saída já realizada, não é possivél fazer consulta.'
    
    def __calcular(self, horario):
        tempo = horario - self.__entrada
        minutos = tempo.days*24*60+(tempo.seconds / 60) - 120
        valor = 8
        if minutos > 0:
            valor = valor + math.ceil(minutos/15)*0.5
        return f'R${valor:.2f}'
    
    def __str__(self):
        return f'Código: {self.__codigo}\nStatus: {self.__status}\nHorário de Entrada: {self.__entrada}\nHorário de Saída: {self.__saida}\nValor: {self.__valor}'

     
def main():
    tikets = []
    ticket1=Ticket(tikets)
    ticket2=Ticket(tikets)
    ticket3=Ticket(tikets)
    print(ticket1,end="\n\n")
    print(ticket1.consultar(datetime.strftime(ticket1.entrada+timedelta(hours=2),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket2.consultar(datetime.strftime(ticket1.entrada+timedelta(hours=2, minutes=30),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket1.registrar_saida(datetime.strftime(ticket1.entrada+timedelta(hours=2, minutes=30),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket1.consultar(datetime.strftime(ticket1.entrada+timedelta(hours=2, minutes=30),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket2.consultar(datetime.strftime(ticket1.entrada+timedelta(hours=23, minutes=59),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket3.consultar(datetime.strftime(ticket1.entrada+timedelta(days=1, minutes=58),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket2.registrar_saida(datetime.strftime(ticket1.entrada+timedelta(hours=24, minutes=10),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket3.registrar_saida(datetime.strftime(ticket1.entrada+timedelta(days=1, minutes=59),"%d/%m/%Y %H:%M")),end="\n\n")
    print(ticket1,end="\n\n")
    print(ticket2,end="\n\n")
    print(ticket3,end="\n\n")






if __name__ == "__main__":
    main()