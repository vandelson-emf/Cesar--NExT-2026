import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda", "Eduardo"],
    "idade": [18, 21, None, 20, 22],
    "nota": [8.5, None, 9.0, 5.5, 7.0]
}

df = pd.DataFrame(dados)

print("Tabela original:")
print(df)

print("\nQuantidade de valores ausentes por coluna:")
print(df.isna().sum())

df_sem_ausentes = df.dropna()

print("\nTabela removendo linhas com valores ausentes:")
print(df_sem_ausentes)

df_nota_zero = df.copy()
df_nota_zero["nota"] = df_nota_zero["nota"].fillna(0)

print("\nTabela preenchendo nota ausente com 0:")
print(df_nota_zero)

df_idade_media = df.copy()
media_idade = df_idade_media["idade"].mean()
df_idade_media["idade"] = df_idade_media["idade"].fillna(media_idade)

print("\nTabela preenchendo idade ausente com a média:")
print(df_idade_media)
