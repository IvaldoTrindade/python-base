#!/bin/env python3
"""Cadastro de produto - Esse documento está sendo utilizado para praticar os aprendizados sobre dicionários em python
 e"""
__version__ = "0.1.0"

from pprint import pprint

produto = {"nome":"Caneta",
    "cores":["Azul","Vermelho","Preto","Branco","Verde"],
    "preco":2.50,
    "em_estoque":True,
    "dimensao":{"altura": 12.1, "largura": 0.8},
    "cod":123,
    "codebar":None,

}

cliente = {"nome":"Ivaldo"}
compra = {"cliente":cliente, "produto":produto, "quantidade": 3}


total_compra = compra['quantidade'] * compra['produto']['preco']

print(f"O cliente {compra['cliente']['nome']} "
    f"comprou {compra['quantidade']} unidades de {compra['produto']['nome']} na cor {compra['produto']['cores'][2]} "
    f"e pagou o total de {total_compra} reais pela compra"
)


