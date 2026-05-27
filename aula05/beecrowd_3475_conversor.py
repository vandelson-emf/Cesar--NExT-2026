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
    numeros_extenso = {
        'zero': 0,
        'um': 1,
        'dois': 2,
        'três': 3,
        'quatro': 4,
        'cinco': 5,
        'seis': 6,
        'sete': 7,
        'oito': 8,
        'nove': 9
    }
    
    if isinstance(numero, int):
        return numeros_extenso.get(int(numero), 'Número inválido')
        #return list(numeros_extenso.keys())[list(numeros_extenso.values()).index(numero)]
    else:
        return numeros_extenso[numero]
    
teste = ['cinco', 'dois', 6, 'nove', 0, 3]

for numero in teste:
    print(conversor(numero))