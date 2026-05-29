'''
Beecrowd - https://judge.beecrowd.com/pt/problems/view/1068

Balanço de Parênteses I

'''

# parenteses_aberto, parenteses_fechado = 0, 0
# analise = False

# expressao = str(input('Informe a expressão para análise: '))

# for index, caracter in enumerate(expressao):

#     match caracter:
#         case "(":
#             parenteses_aberto += 1
#         case ')':
#             parenteses_fechado += 1
#             if parenteses_fechado > parenteses_aberto:
#                 analise = False
#                 break

# analise = True if parenteses_aberto == parenteses_fechado else False

import re

def validar_parenteses(expressao):
    # 1. Extrai apenas os caracteres '(' e ')'
    parenteses = re.findall(r"[()]", expressao)
    
    # Se não houver parênteses, a expressão é válida por padrão
    if not parenteses:
        return True
        
    pilha = []
    
    # 2. Valida a sequência e a quantidade
    for char in parenteses:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            # Se fechar sem ter nenhum aberto, a sequência é inválida
            if not pilha:
                return False
            pilha.pop()
            
    # Se a pilha terminar vazia, a quantidade e a sequência estão corretas
    return len(pilha) == 0

# --- Testes Práticos ---
testes = [
    "((a + b) * c)",      # Válido
    "(a + b)) * (c",      # Inválido (quantidade errada)
    ")a + b(",            # Inválido (sequência errada)
    "a + b",              # Válido (sem parênteses)
    ")3+b*(2-c)("
]

for t in testes:
    print(f"Expressão: {t:<20} Resultado: {validar_parenteses(t)}")
