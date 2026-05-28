# arquivo = open ('aula06/arquivo_texto.txt', encoding='utf-8')

# conteudo = arquivo.read()

# print (conteudo)

cadastro = {}

with open ('aula06/arquivo_texto.txt', encoding='utf-8') as arquivo:

    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.strip()
        codigo, nome, fone = linha.split(',')
        cadastro[codigo] = (nome, fone)

print (cadastro)