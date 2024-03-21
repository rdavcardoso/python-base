#
"""Tabuada de 1 a 9"""

__version__ = "0.1.1"
__author__ = "Rogerio"

numeros = list(range(1,10))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 18)
    
    
