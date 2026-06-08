import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda", "Eduardo", "Fernanda"],
    "idade": [18, 21, 19, 20, 22, 18],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão", "Recife", "Olinda"],
    "nota": [8.5, 6.0, 9.0, 5.5, 6.9, 4.5]
}

df = pd.DataFrame(dados)

#print(df.head(3))
#print(df.tail(3))
#df.info()
#print(df.describe())
#print(df.columns)

#print(df[['nota', 'nome']])

#print(df.iloc[0])
#print(df.iloc[-1])
#print(df.iloc[0, 0])
#print(df.loc['cidade'])
'''
print(df[df['nota'] >= 7])
print('*'*10)
print(df[df['cidade'] == 'Recife'])
print('*'*10)
print(df[(df['cidade'] == 'Olinda') | (df['nota'] >= 7)])
'''

#df.loc[df['cidade'] == 'Recife', 'nota'] += 0.5

df['situacao'] = 'Recuperação'

df.loc[df['nota'] >= 7, 'situacao'] = 'Aprovado'
df.loc[df['nota'] < 5, 'situacao'] = 'Reprovado'

print(df)
