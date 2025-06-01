class Calculadora:
    def _init_(self, numero_1=0, numero_2=0, operador = None, ligado= False):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.operador = operador
        self.ligado = ligado


    def ligar(self):
        self.ligado = True
        return 'Calculadora ligada'

    def desligar(self):
        self.ligado = False
        return 'Calculadora desligada'

    def reset(self):
        self.numero_1 = 0
        self.numero_2 = 0
        self.operador = None
        return 'calculadora resetada'


    def calcular(self):
        if not self.ligado:
            return 'Calculadora desligada'
        else:
            if self.operador == '+':
                resultado = self.numero_1 + self.numero_2
                return resultado
            elif self.operador == '-':
                resultado = self.numero_1 - self.numero_2
                return resultado
            elif self.operador == '*':
                resultado = self.numero_1 * self.numero_2
                return  resultado
            elif self.operador == '/':
                if self.numero_2 <= 0:
                    return 'Erro divisão por zero.'
                else:
                    resultado = self.numero_1 / self.numero_2
                    return resultado
            else:
                return 'Operador inválido'

def main():
    calculadora = Calculadora()
    while True:
        ligar = input('Pressione L para Ligar a calculadora e D para Desligar! \n').strip().upper()
        #loop principal o usuario liga ou sai da calculadora
        if ligar == 'L':
            print(calculadora.ligar()) #calculadora ligada
            e_numero = False #variável que armazena a verificação se é um número
            inicio = True #variável que armazena a verifição se é o inicio da calculadora
            while True:
                if (inicio):      
                    while True: #tratamento de dados
                        try:
                            number1 = float(input('Digite um número: \n').strip())
                            e_numero = True
                        except ValueError:
                            print('Digite valores válidos.')
                            e_numero = False
                        if(e_numero):
                            break                 
                while True: #tratamento de dados
                    op  = str(input('Digite a operação: \n').strip())
                    if(op  in ["+","-","*","/"]):
                        break
                    else:
                        print(f'Digite operador válido: +-*/')
                while True: #tratamento de dados
                    try:
                        number2 = float(input('Digite o próximo número: \n').strip())
                        e_numero = True
                    except ValueError:
                        print('Digite valores válidos.')
                        e_numero = False
                    if(e_numero):
                        break
                calculadora.numero_1 = number1  
                calculadora.numero_2 = number2 #definição dos valores da instancia
                calculadora.operador = op 
                resultado = calculadora.calcular() #chama o metodo calcular
                if resultado == 'Erro divisão por zero.':
                    print(resultado)
                    print(calculadora.reset())
                else:
                    print(f'RESULTADO: {number1} {op} {number2} = {resultado}')

                while True: #loop dentro do primeiro while
                    opcao = str(input('Continuar Operando? (S - SIM/ N - NÃO/ C - RESET) ')).strip().upper()
                    if opcao in ['SIM', 'S']:#caso o ususario queira continuar operando
                        inicio = False
                        number1=resultado
                        break                           
                    elif opcao in ['NAO','NÃO','N']:
                        print(calculadora.desligar())
                        return #ele encerra a função main
                    elif opcao == 'C':
                        inicio = True
                        resultado=0
                        print(calculadora.reset())
                        break# encerra o loop while contido no while principal e volta a pedir os primeiros numeros
                    else:
                        print('Opção inválida')

        elif ligar == 'D':
            print(calculadora.desligar()) #desliga a calculadora
            break
        else:
            print('Opção inválida')

main()