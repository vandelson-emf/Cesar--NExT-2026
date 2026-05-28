try:
    linhas_arquivo = []
    nome_arquivo = input('Insira o nome do arquivo: ')
    with open(nome_arquivo, encoding='utf-8') as arq:
        print(arq.read())
        linhas_arquivo.append('sadfsdfs')
except FileNotFoundError as erro:
    print(f'Deu erro: {type(erro).__name__} - {erro}')
    print('O arquivo está sendo criado!')
    novo_arq = open(nome_arquivo, 'w')
    novo_arq.close()
else:
    print('Tudo certo, nada errado!')
finally:
    del(nome_arquivo)
    del(linhas_arquivo)
    print('Acabou o programa! 🙅‍♂️')
