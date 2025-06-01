'''LISTA 4 - QUESTÃO 3
Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25
'''

def soma_seq_2_maiores(lista):
    maior = None
    for i in range(len(lista)):
        if type(lista[i]) != int or len(lista)<=1:
            return Exception
        if maior == None:
            maior = lista[i]+lista[i+1]
        if i < (len(lista)-1):
            if maior < (lista[i]+lista[i+1]):
                maior = lista[i]+lista[i+1]
    return maior

assert soma_seq_2_maiores([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 25
assert soma_seq_2_maiores([5.0, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == Exception
assert soma_seq_2_maiores(["a", -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == Exception
assert soma_seq_2_maiores([5]) == Exception
print("TESTES OK!")