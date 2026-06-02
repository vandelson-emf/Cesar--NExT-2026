dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

#dias_semana.pop(0) Imutável!

print(type(dias_semana), dias_semana)

print(dias_semana[0])
print(dias_semana[-1])

print(dias_semana.index('terça'))
#dias_semana[1] = 'domingo'

numeros = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 2, 2, 2, 2, 3]

numeros_imutaveis = tuple(numeros)

print(numeros_imutaveis)

numeros_ordenados = sorted(numeros_imutaveis)

print(numeros_imutaveis)
print(numeros_ordenados)

print(len(numeros_imutaveis))

'''
def append_tipo_sort(lista):
    lista.append('eita')

def append_tipo_sorted(lista):
    nova_lista = lista.copy()
    nova_lista.append()
    return nova_lista
'''
