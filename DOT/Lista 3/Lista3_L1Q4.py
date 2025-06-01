'''Lista 1 - Questão 4
Escreva um programa para ler as notas das duas avaliações de um aluno no
semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem
“PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação). '''

def calcular_media(n1, n2):
  if type(n1) == str or n1<0 or n1>10 or type(n2) == str or n2<0 or n2>10:
       return Exception
  media = (n1 + n2) / 2
  return media, "PARABÉNS! Você foi aprovado!" if media >= 6 else None


assert calcular_media(2,2) == (2, None)
assert calcular_media(8,10) == (9, "PARABÉNS! Você foi aprovado!")
assert calcular_media(0,0) == (0, None)
assert calcular_media(12,2) == Exception
assert calcular_media(2,12) == Exception
assert calcular_media(-1,2) == Exception
assert calcular_media(1,-2) == Exception
assert calcular_media(" ",2) == Exception
assert calcular_media(1," ") == Exception

print("TESTES OK")