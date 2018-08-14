import re
Regex = re.compile('\d{2}/\d{2}/\d{4}')
pesquisa = Regex.findall("estou na data 07/08/2018 e 20/08/2018")
for i in range(len(pesquisa)):
    print(pesquisa[i])