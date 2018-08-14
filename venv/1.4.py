import re
frase = "A plca do carro 2135213é IDP-24740000, a qual é a do uno e MGA-1111 é a placa do corsa"
Regex = re.compile("[A-Za-z]{3}-?\d{4}")
pesquisa = Regex.findall(frase)
for x in range(len(pesquisa)):
    print(pesquisa[x])