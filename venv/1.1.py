import re
Regex = re.compile('\d{5}-\d{3}')
frase = "Meu cep é 95630-000"
pesquisa = Regex.search(frase)
print(pesquisa.group())
