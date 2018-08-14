import re
arquivo = open("fonemail.txt")
Regex = re.compile("@[A-Za-z]+\w+[.]\w{1-3}")
for linha in arquivo.readlines()
    