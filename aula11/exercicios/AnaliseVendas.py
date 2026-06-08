import pandas as pd


def main():
    df = pd.read_csv("vendas.csv")

    print("Primeiras linhas da tabela:")
    print(df.head())

    print("\nInformações gerais:")
    df.info()

    df["total"] = df["quantidade"] * df["valor_unitario"]

    total_por_vendedor = df.groupby("vendedor")["total"].sum()
    total_por_cidade = df.groupby("cidade")["total"].sum()
    total_por_categoria = df.groupby("categoria")["total"].sum()

    vendedor_maior_total = total_por_vendedor.idxmax()
    cidade_maior_total = total_por_cidade.idxmax()

    vendas_acima_1000 = df[df["total"] >= 1000]
    vendas_ordenadas = df.sort_values("total", ascending=False)

    print("\nTotal vendido por vendedor:")
    print(total_por_vendedor)

    print("\nTotal vendido por cidade:")
    print(total_por_cidade)

    print("\nTotal vendido por categoria:")
    print(total_por_categoria)

    print(
        f"\nVendedor com maior total vendido: "
        f"{vendedor_maior_total} (R$ {total_por_vendedor[vendedor_maior_total]:.2f})"
    )

    print(
        f"Cidade com maior total vendido: "
        f"{cidade_maior_total} (R$ {total_por_cidade[cidade_maior_total]:.2f})"
    )

    print("\nVendas com total maior ou igual a R$ 1000.00:")
    print(vendas_acima_1000)

    print("\nVendas ordenadas pelo total, do maior para o menor:")
    print(vendas_ordenadas)

    vendas_ordenadas.to_csv("relatorio_vendas.csv", index=False)

    print("\nArquivo relatorio_vendas.csv salvo com sucesso.")


if __name__ == "__main__":
    main()
