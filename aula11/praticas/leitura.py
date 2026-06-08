import pandas as pd


df = pd.read_csv('aula11\\praticas\\estudantes.csv')
'''
#print(df)
print(df.isna().sum())
print(df.dropna())
print('*'*10)

df['nota'] = df['nota'].fillna(0)
df['cidade'] = df['cidade'].fillna('PE')
media_idade = df['idade'].mean()
df['idade'] = df['idade'].fillna(media_idade)

print(df)
'''

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "nota": ["8.5", "6.0", "erro", "5.5"]
}

df = pd.DataFrame(dados)
print(df.dtypes)

print(df)
print('*'*10)

df['nota'] = pd.to_numeric(df['nota'], errors='coerce')
print(df)
print(df.dtypes)
df.to_csv('relatorio.csv', index=False)
