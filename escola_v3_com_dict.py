#!/usr/bin/env python3
"""Exibe relatório de crianças agrupadas por sala
que frequentam cada uma das atividades.
Script feito para aprimorar o Script
escola_v2_com_sets.py utilizando dicionários
Curso Python Base da LinuxTips
Professor Bruno Rocha
"""

__version__ = "0.1.1"
__author__ = "Rogerio"

#Dados
salas = {
    "sala1": ["Erik", "Maia","Gustavo","Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}


#Listar alunos em cada atividade por sala
for nome_atividade, alunos_atividade in atividades.items():
    for nome_sala, alunos_sala in salas.items():
        print(f"{nome_atividade} {nome_sala}: {set(alunos_atividade) & set(alunos_sala)}")
    print("-" * 45)    
        
    


   
    
