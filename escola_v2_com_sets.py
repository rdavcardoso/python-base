#!/usr/bin/env python3
"""Exibe relatório de crianças agrupadas por sala
que frequentam cada uma das atividades.
Script criado na aula do curso Python Base da
Linux Tips, Professor Bruno Rocha
"""

__version__ = "0.1.0"
__author__ = "Rogerio"

#Dados
sala1 = ["Erik", "Maia","Gustavo","Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

#Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print(f"{nome_atividade} sala1", atividade_sala1)
    print(f"{nome_atividade} sala2", atividade_sala2)
    print("-" * 45)
    
