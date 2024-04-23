#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: texto do usuário

$ notes.py read --tag=tech
...

"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print("Must specify subcommand {argument[0]}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    #leitura de notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()
            

if arguments[0] == "new":
    title = arguments[1] #TODO: tratar exception
    text = [
        f"{title}",
        input("Tag: ").strip(),
        input("Text:\n").strip()
    ]
    # \t - tsv (tab separeted values)
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
    
