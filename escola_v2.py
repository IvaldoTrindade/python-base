#!/usr/bin/env python3
"""Exibe um relatório de criaças por atividade

Imprimir a quantidade de crianças agrupadas por sala, e quem frequentam determinadas atividades.
"""

__version__ = "0.1.0"

#Dados
sala1 = ["Douglas","Bruno","Renata","Lin","Davis","Flavia","Gabriele","Xavier","Eduardo","Rodrigo"]
sala2 = ["Alexandre","Gabriel","Diego","Francisco","Roberto","Cristiano","Harry","Jefferson","Leonardo","Felipe"]

#Informações sobre as aulas
aula_ingles = ["Davis","Alexandre","Gabriele","Xavier","Gabriel","Harry"]
aula_musica = ["Gabriel","Rodrigo","Gabriele","Cristiano","Harry"]
aula_danca = ["Bruno","Eduardo","Rodrigo","Renata","Francisco","Cristiano","Gabriel"]
aula_comunicacao = ["Flavia", "Lin", "Francisco","Roberto"]

atividades = [("Inglês", aula_ingles),("Comunicação", aula_comunicacao),("Dança", aula_danca),("Música", aula_musica)]

#Listar as ativiades de cada sala:
for nome_ativiade, atividade in atividades:
    print(f"Alunos da atividade: {nome_ativiade}\n")
    print("-" * 50)

    #Interseção com os alunos das sala 1 e 2 que estão nas atividades.
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    """
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    """        

    print(f"Aula de {nome_ativiade} sala 1: ", atividade_sala1)
    print(f"Aula de {nome_ativiade} sala 2: ", atividade_sala2)
    print()
    print("#"*50)
