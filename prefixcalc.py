"""Calculadora infix

Versão feita sem auxílio.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py 
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"
__author__ = "Rogerio Cardoso"
__license__ = "Unlicensed"

import sys

args = sys.argv[1:]

if not args:
    oper = input("operação: ")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    #TODO fazer de uma forma que não precise repetir os dicts
    operacoes = {
        "sum": (n1 + n2),
        "sub": (n1 - n2),
        "mul": (n1 * n2),
        "div": (n1 / n2),
    }
    if oper in operacoes:
        print(operacoes[oper])
    else:
         print("operação não suportada\n"
             "tente uma das operções suportadas\n"
             "sum: soma\n"
             "sub: subtração\n"
             "mul: multiplicação\n"
             "div: divisão\n")     

elif len(sys.argv) == 4:
    oper = sys.argv[1]
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    operacoes = {
        "sum": (n1 + n2),
        "sub": (n1 - n2),
        "mul": (n1 * n2),
        "div": (n1 / n2),
        }
    if oper in operacoes:
        print(operacoes[oper])
    else:
        print("operação não suportada\n"
            "tente uma das operções suportadas\n"
            "sum: soma\n"
            "sub: subtração\n"
            "mul: multiplicação\n"
            "div: divisão\n")
      
    




