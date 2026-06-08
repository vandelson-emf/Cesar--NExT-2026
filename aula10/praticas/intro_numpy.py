import numpy as np


notas = np.array([1.44564, 5.5, 8.9, 10, .5])

#print(notas)

lista = [10, 20, 30]
array = np.array([10, 20, 30])

print(lista + [5])
print(array + 5)

precos = np.array([100, 200, 300])
precos_com_desconto = precos * 0.9

print(precos_com_desconto)

numeros = np.arange(0, 10, 2)

print(numeros)

valores = np.ones((5, 10, 5))

print(valores)

# 10 | | | | | | | | | | | | 15
valores = np.linspace(0, 1, 5)

print(valores)

notas = np.array([
    [1.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 9.9]
])

print(notas.ndim)
print(notas.shape)
print(notas.size)
print(notas.dtype)

print(notas[0, 0])
print(notas[-1, -1])
print(notas[:,0])

notas = np.array([7.0, 8.0, 6.0, 9.0])

print(notas + 1)
print(notas - 0.5)
print(notas * 2)
print(notas / 2)

notas_unidade_1 = np.array([7.0, 8.0, 6.0])
notas_unidade_2 = np.array([0.0, 8.0, 10.0])

#print((notas_unidade_1 + notas_unidade_2) / 2)

# print(notas_unidade_1.sum())
# print(notas_unidade_1.mean())
# print(notas_unidade_1.min())
# print(notas_unidade_1.max())

print(notas_unidade_1.mean())
print(notas_unidade_1.std())
print(notas_unidade_2.mean())
print(notas_unidade_2.std())

turma_a = np.array([7.0, 7.1, 7.2, 7.0, 7.1])
turma_b = np.array([3.0, 5.0, 7.0, 9.5, 10.0])

print(turma_a.mean(), turma_a.std())
print(turma_b.mean(), turma_b.std())

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [8.5, 5.6, 7.8],
    [7.5, 9.0, 9.0]
])

print(notas.mean())
print(notas.mean(axis=0))
print(notas.mean(axis=1))

notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0])

print((notas >= 7).sum())
print(notas[notas >= 7])

nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0]
])

medias = notas.mean(axis=1)
aprovados = (medias >= 7) | (medias < 6)
print(nomes[aprovados])
print(medias[aprovados])
