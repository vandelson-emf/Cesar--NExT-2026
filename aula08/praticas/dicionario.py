palavras_en = ['dog', 'lion', 'tiger']

dicionario = {
    'cachorro': 'dog',
    'leão': 'lion',
    'tigre': 'tiger'
}

print(dicionario['tigre'])
print(dicionario['leão'])

enderecos = {
    '53240440': ['Avenida da Saudade', '32B', 'Prox ao não sei o que'],
    '53000090': ['Rua dos Bobos', '00', 'Prox a casa de Enzo']
}

print(dicionario)
print(enderecos['53240440'])

# - Criando um dicionário
dados = dict()

# - Acessando elementos de um dicionário
# - Adição de itens por atribuição
dados['bear'] = 'urso'
'''for _ in range(3):
    chave, valor = input('Insira chave e valor: ').split()
    dados[chave] = valor'''

#print(dados)

# - Adição de itens por update
infos = [('monkey', 'macaco'), ('pig', 'porco'), ('rabbit', 'coelho')]
dados.update(infos)
print(dados)

# - Removendo itens
removido = dados.pop('rabbit')
removido2 = dados.popitem()
print(dados)
print(removido)
print(removido2)

# - esvaziando um dicionário
#dados.clear()
#print(dados)

# - adicionar valores + update()
# - get()
#print(dados['bearasdasdasd'])
print(dados.get('bear', 'Animal não encontrado'))

# - keys()
print(dados.keys())

# - values()
print(dados.values())

# - items()
print(dados.items())

# - for
for chave, valor in dados.items():
    print(f'{chave} - {valor}')
