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

Os resultados serão salvos em `prefixcalc.log`
"""
__version__ = "0.1.1"

import os
import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos!")
    print("Ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments
validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")

with open(filepath, "a") as file_:
    file_.write(f"{operation}, {n1}, {n2} = {result}\n")

print(f"O resultado é {result}")