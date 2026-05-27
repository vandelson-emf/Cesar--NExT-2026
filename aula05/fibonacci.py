# n = int(input())

# anterior, atual = 0, 1

# sequencia = [anterior, atual]

# if n <= 46:
#     for i in range (2, n):
#         anterior, atual = atual, anterior + atual
#         sequencia.append(atual)
#     print (sequencia)

n = int(input())

anterior, atual = 0, 1

sequencia = [anterior, atual]

if n <= 46:
    for i in range (2, n):
        anterior, atual = atual, anterior + atual
        sequencia.append(atual)
    
    for item in sequencia:
        print (item, end = ' ')
    