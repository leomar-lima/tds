'''Lista 1 - Questão 8
Escreva uma função que lê um caractere digitado pelo usuário e retorna este
caractere somente se ele for igual a 'S' ou 'N'. Se ocaractere não for nem 'S'
nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'.
Use esta função em um programa que fica lendo do usuário um número qualquer e
imprime este número ao cubo na tela. O programa deve ficar lendo os números até
o usuário responder 'N' à pergunta se ele deseja continuar ou não.'''

def cubo(x, resposta):
    if (resposta != "S" and resposta != "N" ) or type(x) == str:
        return Exception
    if resposta == "S":
        return round(x**3,2)
    return None

assert cubo(4, "S") == 64
assert cubo(0,"S") == 0
assert cubo(-2,"S") == -8
assert cubo(3.14,"S") == 30.96
assert cubo(1,"N") == None
assert cubo(1, " ") == Exception
assert cubo(" ","S") == Exception

print("TESTES OK")


