'''Questão 13 Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.'''

from random import *

def ocorrencias_faces(resultados):
    ocorrencias = {}
    for resultado in resultados:
        if resultado in ocorrencias:
            ocorrencias[resultado] += 1
        else:
            ocorrencias[resultado] = 1
    return ocorrencias

def main():
  n = randint(1, 100)
  print(f"Lançando o dado {n} vezes...")
  lancamentos = []
  for i in range(n):
    lancamento = randint(1, 6)
    lancamentos.append(lancamento)
  ocorrencias = ocorrencias_faces(lancamentos)

  print("\nNúmero de ocorrências de cada face:")
  for face, ocorrencia in ocorrencias.items():
      print(f"Face {face}: {ocorrencia} ocorrência(s)")

if __name__ == "__main__":
  main()
