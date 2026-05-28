arquivo = open('aula06/praticas/eita.txt', 'w', encoding='utf-8')

arquivo.write('Primeira linha do arquivo\n')
arquivo.write('Outra linha no arquivo\n')
arquivo.write('Estou escrevendo no arquivo\n')

arquivo.seek(0)

arquivo.write('First\n')

arquivo.close()

outro_arq = open('aula06/praticas/muitas_linhas.txt', 'w')

lista = ['ovos\n', 'bacon\n', 'Spam\n']

outro_arq.writelines(lista)

outro_arq.close()