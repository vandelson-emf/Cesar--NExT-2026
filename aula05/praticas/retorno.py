'''coiso = 'aaaaaaaaaaaaa'

del(coiso)

print(quantidade_caracteres)
entrada_usuario = input('Informe alguma coisa: ')

quantidade_caracteres = len(coiso)

if quantidade_caracteres > 10:
    print('Tem mais que 10 caracteres')
else:
    print('Tem 10 ou menos caracteres')'''

def velocidade(distancia, tempo):
    return distancia/tempo

velo = velocidade(1000, 4)

if velo > 100:
    print('Você será multado!')
else:
    print('Tá de boas 🖖')

def monta_nome(primeiro_nome, segundo_nome):
    primeiro_nome = primeiro_nome.capitalize()
    segundo_nome = segundo_nome.capitalize()

    return f'{primeiro_nome} {segundo_nome}'

nomes = []

for _ in range(4):
    print('Cadastro do Nomes')
    primeiro_nome = input('Informe o 1º nome: ')
    segundo_nome = input('Informe o 2º nome: ')
    nome_completo = monta_nome(primeiro_nome, segundo_nome)
    nomes.append(nome_completo)

print(nomes)
