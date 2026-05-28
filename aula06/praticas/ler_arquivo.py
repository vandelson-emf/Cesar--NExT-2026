arquivo = open('aula06/praticas/exemplo.txt', encoding='utf-8')
#arquivo = open('aula06/exercicios/dados_financeiros.csv', encoding='utf-8')

#conteudo = arquivo.read()
#print(conteudo)

'''for _ in range(10):
    print(arquivo.readline())
'''

linhas = arquivo.readlines()
print(linhas)
arquivo.seek(2)
for linha in arquivo.readlines():
    print(linha.strip())
