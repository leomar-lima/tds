class Calculadora:
  numero1=0
  numero2=0
  operação=None

  def calcular(self,numero1, numero2,operação):

    self.numero1 = numero1
    self.numero2 = numero2
    self.operação = operação

    if self.operação == '+':
      return self.numero1 + self.numero2
    elif self.operação == '-':
      return self.numero1 - self.numero2
    elif self.operação == '*':
      return self.numero1 * self.numero2
    elif self.operação == '/':
      if self.numero2 != 0:
        return self.numero1 / self.numero2
      else:
        return "Erro: Divisão por zero não permitida"
    else:
      return "Operação inválida"

def main():
  minha_calculadora = Calculadora()
  while True:
    #minha_calculadora.numero1 = float(input("Digite o primeiro número: "))
    #minha_calculadora.numero2 = float(input("Digite o segundo número: "))
    #minha_calculadora.operação = input("Escolha a operação (+, -, *, /) ou 'q' para sair: ")
    numero1 = float(input("Digite o primeiro número: "))
    operação = input("Escolha a operação (+, -, *, /) ou 'q' para sair: ")
    numero2 = float(input("Digite o segundo número: "))


    resultado = minha_calculadora.calcular(numero1,numero2,operação)

    print(f'{minha_calculadora.numero1} {minha_calculadora.operação} {minha_calculadora.numero2} = {resultado}')

    resp=str.upper(input("Continua?(S/N)"))
    if resp == 'N':
      break
main()