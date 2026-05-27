'''
Axela é uma assistente virtual em desenvolvimento. Ela irá te auxiliar nas mais diversas
tarefas diárias, inclusive na digitação de textos. Você precisa ajudar a desenvolver uma das
funções para a Axela: um conversor de números. Esta função terá que converter um número por
extenso (em português) para algarismos numéricos. Esta função também precisará converter os
algarismos nos respectivos valores, por extenso.

Entrada
A entrada consiste em vários casos de teste. Cada caso contém um número N (0 ≤ N ≤ 9),
ou por extenso, ou por algarismos.

Saída
Para cada caso de teste, imprima o valor devidamente convertido.
'''

def conversor(numero):
    extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

    if isinstance(numero, int) and 0 <= numero <= 9:
        print (extenso[int(numero)])
    elif isinstance(numero, str) and numero in extenso:
        print (extenso.index(numero))
    else:
        print('Número inválido')
    
teste = ['cinco', 'dois', 6, 'nove', 10, 3]


for numero in teste:
    conversor(numero)