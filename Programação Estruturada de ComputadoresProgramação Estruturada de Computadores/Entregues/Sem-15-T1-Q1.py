#FUNÇÃO "dados" FAZ RECEBE A ENTRADA DADOS INSERIDOS PELO TECLADO.
def dados():
  temperatura = float(input().strip())
  escala = input().strip().upper()[0]
  return temperatura, escala

#FUNÇÃO "comparacao" RECEBE OS DADOS E FAZ A COMPARAÇÃO PARA RETORNAR A TEMPERATURA E SUA ESCALA
def comparacao(dados):
  escala1 = ""
  temperatura1 = 0.0
  for temperatura, escala in dados:
    if (escala1 != ""):
      if (escala1 == escala):
        if(temperatura1 > temperatura):
          return temperatura1, escala1
      if (escala1 == "C"):
        C= round(temperatura1*(9/5)+32,4)
        if (C > temperatura):
          return temperatura1, escala1
      F = round((temperatura1-32)*(5/9),4)
      if (F > temperatura):
        return temperatura1,escala1
      return temperatura, escala
    temperatura1 = temperatura
    escala1 = escala

def main():
   # Inicializando o vetor "temperaturas"
   temperaturas=[]
   #PROCESSAMENTO DE DADOS
   for i in range(2):
    temperaturas.append(dados())
   temperatura_maior = comparacao(temperaturas)
   #SAÍDA DE DADOS
   print(temperatura_maior)

        
   
if __name__=="__main__":
   main()