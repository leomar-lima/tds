#FUNÇÃO "dados" FAZ RECEBE A ENTRADA DADOS INSERIDOS PELO TECLADO.
def dados():
  temperatura = float(input().strip())
  escala = input().strip().upper()[0]
  return (temperatura, escala)

#A FUNÇÃO "soma" faz a operação soma e retorna o somatorio.
def soma(num1, num2):
   somatorio=num1 + num2
   return float(f'{somatorio:.4f}')

#A FUNÇÃO "para_Fahrenhein" CONVERTE O VALOR RECEBIDO PARA A ESCALA: Fahrenhein           
def para_Fahrenhein(valor):
  valor=valor*(9/5)+32
  return valor

#A FUNÇÃO "para_Celcius" CONVERTE O VALOR RECEBIDO PARA A ESCALA: Celcius        
def para_Celcius(valor):
  valor=(valor-32)*(5/9)
  return valor

#FUNÇÃO "calculo" RECEBE OS DADOS E FAZ A COMPARAÇÃO PARA RETORNAR A TEMPERATURA E SUA ESCALA
def calculo(dados):
  escala1 = " "
  temperatura1 = 0.0
  for temperatura, escala in dados:
    if (escala1 in "CF" and escala in "CF"):
      if (escala1 == escala):
        return soma(temperatura1,temperatura), escala
      if (escala == "C"):
        temperatura1 = para_Celcius(temperatura1)
        return soma(temperatura1,temperatura), escala
      temperatura1 = para_Fahrenhein(temperatura1)
      return soma(temperatura1,temperatura), escala
    temperatura1 = temperatura
    escala1 = escala

def main():
   # Inicializando o vetor "temperaturas"
   temperaturas=[]
   #PROCESSAMENTO DE DADOS
   for i in range(2):
    temperaturas.append(dados())
   temperatura_soma = calculo(temperaturas)
   #SAÍDA DE DADOS
   print(temperatura_soma)

        
   
if __name__=="__main__":
   main()