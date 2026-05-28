with open('aula06/praticas/notas.txt', 'w') as notas, open('blabla.txt', 'w') as coiso:
    for _ in range(4):
        numero = input('Insira um número: ')
        notas.write(f'{numero}\n')

print('-- acabou --')
