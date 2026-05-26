'''
Beecrowd 1075 - Resto 2

Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão
resto igual a 2.

Entrada
A entrada contém um valor inteiro N (N < 10000).

Saída
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.
'''

# 

# Solução alternativa usando list comprehension
# n = int(input())
# resultados = [i for i in range(1, 10001) if i % n == 2]
# for r in resultados:
#     print(r)

# Solução usando lambda e filter
n = int(input())
resultados = filter(lambda x: x % n == 2, range(1, 10001))
for r in resultados:
    print(r)


'''

'''

