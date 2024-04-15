"""Calculadora prefix

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

import os
import sys

args = sys.argv[1:]

if not args:
    oper = input("operação: ")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    #TODO fazer de uma forma que não precise repetir os dicts
    operacoes = {
        "sum": [(n1 + n2), "+"],
        "sub": [(n1 - n2), "-"],
        "mul": [(n1 * n2), "*"],
        "div": [(n1 / n2), "/"],
        }
    if oper in operacoes:
            result = operacoes[oper][0]
            oper_simb = operacoes[oper][1]
            print(f"{n1} {oper_simb} {n2} = {result}")
            path = os.curdir
            filepath = os.path.join(path, "prefixcalc4.log")
    
            with open(filepath, "a") as file_:
                file_.write(f"{n1} {oper_simb} {n2} = {result}\n")
    else:
         print("operação não suportada\n"
             "tente uma das operções suportadas\n"
             "sum: soma\n"
             "sub: subtração\n"
             "mul: multiplicação\n"
             "div: divisão\n")     

elif len(args) == 3:
    oper = args[0]
    n1 = int(args[1])
    n2 = int(args[2])
    operacoes = {
        "sum": [(n1 + n2), "+"],
        "sub": [(n1 - n2), "-"],
        "mul": [(n1 * n2), "*"],
        "div": [(n1 / n2), "/"],
        }
    
    if oper in operacoes:
        result = operacoes[oper][0]
        oper_simb = operacoes[oper][1]
        print(f"{n1} {oper_simb} {n2} = {result}")
        path = os.curdir
        filepath = os.path.join(path, "prefixcalc4.log")

        with open(filepath, "a") as file_:
            file_.write(f"{n1} {oper_simb} {n2} = {result}\n")
            
    else:
        print("operação não suportada\n"
            "tente uma das operções suportadas\n"
            "sum: soma\n"
            "sub: subtração\n"
            "mul: multiplicação\n"
            "div: divisão\n")
      
    




