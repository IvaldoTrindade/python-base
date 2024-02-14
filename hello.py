#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem 
correspondente

usage: 

Tenha a variável LANG devidamente configurada, ex:
    export LANG=pt_BR
Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.1"
__author__ = "Ivaldo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]


msg = {
    "en_US": "Hello Wolrd!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde!"
}

print(current_language)
print(msg[current_language])
