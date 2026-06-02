# dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

# print (type(dias_semana), dias_semana)

'''
***** EXERCÍCIO 01 *****
'''

# def ex_01 (lista):
#     return set(lista)

# nova_lista = ex_01([1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4])

# print ('\n===== Exercício 01 =====')
# print (f'Tipo: {type(nova_lista)} - {nova_lista}\n')

'''
***** EXERCÍCIO 02 *****
'''
arquivo = './aula08/EX_02_CEP_ENDERECO.txt'
base = open (arquivo, 'a+', encoding='utf-8')

def cadastrar_endereco (arquivo, endereco):
    arquivo.write(endereco)

def consultar_endereco (arquivo, cep_pesquisar):
    linhas = arquivo.readlines()

    for linha in linhas.strip(','):
        if linha[0]==cep_pesquisar:
            return f'Endereço localizado {linha[1]} para o CEP {cep_pesquisar}.' 
        
    return f'Endereço não localizado para o CEP {cep_pesquisar}.' 

        

'''
Testando
'''

# cadastrar_endereco(base, '52050220, Av Rosa e Silva - Gracas\n')
# cadastrar_endereco(base, '52050221, Rua da Hora - Gracas\n')
# cadastrar_endereco(base, '52050222, Rua do Futuro - Gracas\n')

# Antes de iniciar a pesquisa, tem que posicionar o cursor no início do arquivo
base.seek(0)
linhas = base.readlines()
print (linhas)
print ('-'*20)
print (len(linhas))
print ('*'*20)

for conteudo in linhas:
    print (f'{type(conteudo.split(','))} = {conteudo.split(',')}')
    print (conteudo.split(',')[0])

    # if conteudo.split(',')[0]==52050220:
    #     print ('Ok')
    # else:
    #     print ('No')
# for cep, endereco in linhas.split(','):
#     print (cep)
    # if linha[0]==52050220:
    #     print (f'Endereço localizado {linha[1]} para o CEP 52050220.' )
    # else:
    #     print (f'Endereço não localizado para o CEP 52050220.' )

#print (consultar_endereco (base, 52050220))
# print (consultar_endereco (base, 52050221))
# print (consultar_endereco (base, 52050224))

      
        

