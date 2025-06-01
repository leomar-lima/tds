'''Questão 11
Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário.
Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
==== =MENU========
1)Cadastar nome
2)Pesquisar nome
3)Listar todos os nome
4) Alterar nome
5) Excluir nome
0) Sair do programa
——————–
Digite sua escolha:_'''

def cadastrar_nome(lista):
    nome = input("Digite o nome a ser cadastrado: ")
    lista.append(nome)
    print(f"Nome '{nome}' cadastrado com sucesso!")
    return lista

def pesquisar_nome(lista):
    nome = input("Digite o nome a ser pesquisado: ")
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == nome:
            posicoes.append(i)
    if posicoes:
        print(f"Nome '{nome}' encontrado na(s) posição(ões): {posicoes}")
    else:
        print(f"Nome '{nome}' não encontrado na lista.")

def listar_nomes(lista):
    if not lista:
        print("A lista de nomes está vazia.")
    else:
        print("Lista de nomes:")
        for i, nome in enumerate(lista):
            print(f"{i}: {nome}")

def alterar_nome(lista):
      listar_nomes(lista)
      while True:
        try:
            posicao = int(input("Digite a posição do nome a ser alterado: "))
            if 0 <= posicao < len(lista):
                novo_nome = input("Digite o novo nome: ")
                lista[posicao] = novo_nome
                print(f"Nome na posição {posicao} alterado para '{novo_nome}'.")
                return lista
            else:
                print("Posição inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro. Operação cancelada.")
            return lista

def excluir_nome(lista):
    listar_nomes(lista)
    if not lista:
        return lista
    while True:
      try:
          posicao = int(input("Digite a posição do nome a ser excluído: "))
          if 0 <= posicao < len(lista):
              confimacao = int(input(f"Deseja realmente exluir o nome '{lista[posicao]}', confirme com o número da posição({posicao}) ou outro número para cancelar: "))
              if confimacao != posicao:
                  print("Operação cancelada.")
                  return lista
              nova_lista = list(range(len(lista)-1))
              j=0
              for i in range(len(lista)):
                if i != posicao:
                  nova_lista[j]=lista[i]
                  j+=1
              print(f"Nome '{lista[posicao]}' excluído da posição {posicao}.")
              return nova_lista
          else:
              print("Posição inválida.")
      except ValueError:
          print("Entrada inválida. Digite um número inteiro. Operação cancelada.")
          return lista


def main():
    lista_nomes = []

    while True:
        print("\n==== MENU ====")
        print("1) Cadastrar nome")
        print("2) Pesquisar nome")
        print("3) Listar todos os nomes")
        print("4) Alterar nome")
        print("5) Excluir nome")
        print("0) Sair do programa")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            lista_nomes = cadastrar_nome(lista_nomes)
        elif escolha == '2':
            pesquisar_nome(lista_nomes)
        elif escolha == '3':
            listar_nomes(lista_nomes)
        elif escolha == '4':
            lista_nomes = alterar_nome(lista_nomes)
        elif escolha == '5':
            lista_nomes = excluir_nome(lista_nomes)
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()