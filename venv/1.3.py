import re
regex = re.compile('\d{3}-\d{5}-\d{4}')
pesquisa = regex.findall("os telefones são: 051-98029-9754, 051-11111-1111")
for x in range(len(pesquisa)):
    print(pesquisa[x])