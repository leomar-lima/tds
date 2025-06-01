'''LISTA 4 - QUESTÂO 1
Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]
'''

def lista_inteiros_sem_repeticao(lista):
    for i in lista:
        if type(i) != int:
            return Exception
    return sorted(set(lista))

assert lista_inteiros_sem_repeticao([1,1,2,2,3,3,4,4,5,5]) == [1,2,3,4,5]
assert lista_inteiros_sem_repeticao([-1,-1,-2,-2,-3,-3,-4,-4,-5,-5]) == [-5, -4,-3,-2,-1]
assert lista_inteiros_sem_repeticao([1.2,1.2,1,1]) == Exception
assert lista_inteiros_sem_repeticao(["a","a",2,2]) == Exception

print("TESTES OK!")