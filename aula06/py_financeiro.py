total_meses = 0
total_liquido = 0.0
soma_lucros = 0.0
qtd_meses_lucros = 0
soma_perdas = 0.0
qtd_meses_perda = 0
maior_aumento_lucro = {
    "data":"",
    "valor": 0.0
}
maior_reducao_lucro= {
    "data":"",
    "valor": 0.0
}

info = {
    "total_meses"           : 0,
    "total_liquido"         : 0.0,
    "soma_lucros"           : 0.0,
    "qtd_meses_lucro"       : 0,
    "soma_perdas"           : 0.0,
    "qtd_meses_perda"       : 0,
    "maior_aumento_lucro"   : maior_aumento_lucro,
    "maior_reducao_lucro"   : maior_reducao_lucro
}

with open ('aula06/dados_financeiros.csv') as dados:
