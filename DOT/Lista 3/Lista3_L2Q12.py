'''Questão 12
Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas.'''

def prova(gabarito,respostas):
    num_alunos = len(respostas)
    acertos = []
    for resp_aluno in respostas:
        acertos_aluno = 0
        for i in range(len(resp_aluno)):
            if type(resp_aluno[i]) != str or type(gabarito[i]) != str or (resp_aluno[i] not in ["A", "B","C","D", "E"]) or (gabarito[i] not in ["A", "B","C","D", "E"]) or len(gabarito)!=len(resp_aluno):
                return Exception
            if resp_aluno[i] == gabarito[i]:
                acertos_aluno+=1
        acertos.append(acertos_aluno)
    return acertos

assert prova(["A","B","C"],(["A","B","C"],["A","C","D"])) == [3,1]
assert prova(["A","B","C"],(["A","F","C"],["A","C","D"])) == Exception
assert prova(["A","B","C"],(["A","E","C"],["A",1,"D"])) == Exception
assert prova(["A","B","C"],([-1,"E","C"],["A","B","D"])) == Exception
assert prova(["A","B","C"],(["A","E","C"],["A","B"])) == Exception

print("TESTES OK")

