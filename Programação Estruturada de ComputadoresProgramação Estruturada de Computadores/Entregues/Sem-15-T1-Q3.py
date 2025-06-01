
#A FUNÇÃO "carrega_cidades" ABRE O ARQUIVO EXTERNO E RETORNA EM UMA MATRIZ
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append((uf, int(ibge), nome, int(dia), int(mes), int(pop)))
    arquivo.close()
    return resultado

#A FUNÇÃO "nome_mes" CONVERTE O NUMERO DO MÊS EM NOME DO MES
def nome_mes(mes):
    if (mes==1) : return 'JANEIRO'
    if (mes==2) : return 'FEVEREIRO'
    if (mes==3) : return 'MARÇO'
    if (mes==4) : return 'ABRIL'
    if (mes==5) : return 'MAIO'
    if (mes==6) : return 'JUNHO'
    if (mes==7) : return 'JULHO'
    if (mes==8) : return 'AGOSTO'
    if (mes==9) : return 'SETEMBRO'
    if (mes==10) : return 'OUTUBRO'
    if (mes==11) : return 'NOVEMBRO'
    if (mes==12) : return 'DEZEMBRO'

def main():
    #ENTRADA DE DADOS
    dia_aniversario= int(input().strip())
    mes_aniversario = int(input().strip())

    #PROCESSAMENTO DE DADOS
    cidades = carrega_cidades()
    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia_aniversario} DE {nome_mes(mes_aniversario)}:")
    for uf, ibge, nome, dia, mes, pop in cidades:
        if (dia == dia_aniversario) and (mes == mes_aniversario):
            #SAÍDA DE DADOS
            print(f'{nome}({uf})')

if __name__=="__main__":
   main()