# n = int(input())

# anterior, atual = 0, 1

# sequencia = [anterior, atual]

# if n <= 46:
#     for i in range (2, n):
#         anterior, atual = atual, anterior + atual
#         sequencia.append(atual)
#     print (sequencia)

def fibonacci(n):
    anterior, atual = 0, 1

    sequencia = [anterior, atual]

    if n <= 46:
        for i in range (2, n):
            anterior, atual = atual, anterior + atual
            sequencia.append(atual)
        
        return sequencia

print(*fibonacci(10))
    