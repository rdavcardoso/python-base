#!/usr/bin/env python3

import sys
import os

# EAFP - Easy to Ask Forgiviness than Permission
try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: usar retry
else:
    print("Sucesso")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
