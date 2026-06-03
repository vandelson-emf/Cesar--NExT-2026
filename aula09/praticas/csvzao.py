#import csv
from csv import DictReader

with open('aula09\\praticas\\dados_financeiros.csv') as arquivo:
    leitor = DictReader(arquivo)
    for linha in leitor:
        if int(linha['Lucros/Perdas']) < 0:
            print(linha['Data'])
