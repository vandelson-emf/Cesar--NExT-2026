t = (0, 1, 1, 2, 3, 5)
l = [0, 1, 1, 2, 3, 5]

numeros = set()

numeros.add(1)
numeros.add(2)
numeros.add(3)
numeros.add(1)
numeros.add(1)
numeros.add(1.001)
numeros.add(4)
numeros.add('1')

#numeros[1] = 1

print(numeros)

# - criar um set
votos = ['aaa', 'bbb', 'aaa', 'bbb', 'ccc', 'aaa', 'aaa', 'bbb']
candidatos_unicos = set(votos)
print(candidatos_unicos)

for candidato in candidatos_unicos:
    print(candidato, votos.count(candidato))

# - print(ingredientes[0]) # erro
# - adicionar elementos

# - remover elementos
candidatos_unicos.remove('bbb')

print(candidatos_unicos)
