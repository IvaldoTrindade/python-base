"""
template = "Olá %s, tudo bem? O seu saldo bancário é de %.2f!"

nome = "Ivaldo"
saldo = 149.9

print(template % (nome, saldo))
"""
email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar o %(produto)s?

Esse produto é ótimo para resolver o %(texto)s

Clique agora em %(link)s para garantir essa oferta exclusiva!

Mas corre que ainda restam penas %(quantidade)d unidade disponível!

O valor promocional dessa oferta imperdível é de %(preco).2f
"""

clientes = ["Ivaldo", "Bruna", "Diego", "Alexandre"]

for i in clientes:
    print(
        email_tmpl 
        % {"nome": clientes, 
        "produto":"Nissan GTR", 
        "texto":"Andar sempre de transporte, ou ter que pedir uber", 
        "link":"www.nissan.com", 
        "quantidade": 1, 
        "preco":35497.50
        }
    )