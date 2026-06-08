import pandas as pd


def formatar_nomes(df):
    if df.empty:
        return "nenhum estudante"

    return ", ".join(df["nome"])


def main():
    df = pd.read_csv("estudantes.csv")

    print("Primeiras linhas da tabela:")
    print(df.head())

    print("\nInformações gerais:")
    df.info()

    colunas_avaliacoes = ["avaliacao_1", "avaliacao_2", "avaliacao_3"]

    df["media"] = df[colunas_avaliacoes].mean(axis=1)

    df["situacao"] = "Recuperação"
    df.loc[df["media"] >= 7, "situacao"] = "Aprovado"
    df.loc[df["media"] < 5, "situacao"] = "Reprovado"

    aprovados = df[df["situacao"] == "Aprovado"]
    recuperacao = df[df["situacao"] == "Recuperação"]
    reprovados = df[df["situacao"] == "Reprovado"]

    media_por_turma = df.groupby("turma")["media"].mean()
    media_por_cidade = df.groupby("cidade")["media"].mean()

    indice_maior_media = df["media"].idxmax()
    indice_menor_media = df["media"].idxmin()

    estudante_maior_media = df.loc[indice_maior_media]
    estudante_menor_media = df.loc[indice_menor_media]

    print("\nEstudantes aprovados:")
    print(formatar_nomes(aprovados))

    print("\nEstudantes em recuperação:")
    print(formatar_nomes(recuperacao))

    print("\nEstudantes reprovados:")
    print(formatar_nomes(reprovados))

    print("\nMédia por turma:")
    print(media_por_turma.round(2))

    print("\nMédia por cidade:")
    print(media_por_cidade.round(2))

    print(
        f"\nEstudante com maior média: "
        f"{estudante_maior_media['nome']} ({estudante_maior_media['media']:.2f})"
    )

    print(
        f"Estudante com menor média: "
        f"{estudante_menor_media['nome']} ({estudante_menor_media['media']:.2f})"
    )

    df.to_csv("resultado_estudantes.csv", index=False)

    print("\nArquivo resultado_estudantes.csv salvo com sucesso.")


if __name__ == "__main__":
    main()
