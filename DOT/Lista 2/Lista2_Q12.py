'''Questão 12
Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas.'''

from random import *
import string


def main():
    gabarito = [choice(string.ascii_uppercase[:5]) for _ in range(30)]
    num_alunos = randint(1, 100)
    acertos = []
    for aluno in range(1, num_alunos + 1):
        respostas = [choice(string.ascii_uppercase[:5]) for _ in range(30)]
        acertos_aluno = sum(1 for i in range(30) if respostas[i] == gabarito[i])
        acertos.append((aluno, acertos_aluno))

    print("\nNúmero de acertos de cada aluno:")
    for aluno, acertos in acertos:
        print(f"Aluno {aluno}: {acertos} acertos")

if __name__ == "__main__":
    main()
