# NExT 26.1 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 11 - Pandas

### Na aula de hoje

* O que é o Pandas;
* Diferenças entre NumPy e Pandas;
* `Series` e `DataFrame`;
* Criando tabelas com Pandas;
* Lendo arquivos CSV com `read_csv`;
* Visualizando dados com `head`, `tail`, `info` e `describe`;
* Tratando valores ausentes;
* Agrupando dados com `groupby`;
* Ordenando dados;
* Salvando resultados com `to_csv`;
* Boas práticas no uso de Pandas.

---

## 🐼 Pandas

**[Pandas](https://pandas.pydata.org)** é uma biblioteca Python usada para manipulação e análise de dados.

Ela é especialmente útil quando precisamos trabalhar com dados em formato de tabela, como:

* Planilhas;
* Arquivos CSV;
* Relatórios financeiros;
* Bases de clientes;
* Resultados de formulários...

Na prática, Pandas permite carregar, organizar, limpar, transformar, filtrar, resumir e salvar dados usando poucas linhas de código.

Se na aula de NumPy começamos a trabalhar com arrays numéricos, agora vamos avançar para estruturas mais próximas de uma planilha.

---

### Por que usamos Pandas?

Na aula anterior, vimos que NumPy é muito eficiente para trabalhar com arrays numéricos.

Por exemplo:

```python
import numpy as np

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [8.0, 8.5, 8.5]
])

print(notas.mean(axis=1))
```

Esse tipo de estrutura funciona muito bem quando os dados são numéricos e organizados em linhas e colunas.

Mas dados reais geralmente são mais complexos.

Imagine um arquivo `.csv` com os seguintes dados:

```csv
nome,idade,cidade,nota,status
Ana,18,Recife,8.5,Aprovado
Bruno,21,Olinda,6.0,Recuperação
Carlos,19,Recife,9.0,Aprovado
Duda,,Jaboatão,5.5,Recuperação
Eduardo,22,Recife,,Pendente
```

Nesse caso, temos:

* Textos;
* Números inteiros;
* Números decimais;
* Valores ausentes;
* Categorias.

Para esse tipo de situação, Pandas é mais adequado do que NumPy puro.

---

## Pandas e o pipeline de dados

Nas aulas anteriores, vimos o fluxo de ETL e EDA:

* **Extract**: extrair dados de arquivos, sistemas, APIs ou entradas do usuário;
* **Transform**: limpar, corrigir, converter e organizar os dados;
* **Load**: salvar os dados transformados em algum destino;
* **EDA**: explorar os dados com estatísticas, tendências, padrões e visualizações.

Pandas aparece principalmente nas etapas de **transformação** e **exploração**.

Com ele, conseguimos responder perguntas como:

* Quantos registros existem na base?
* Quais colunas têm valores ausentes?
* Qual a média de uma coluna?
* Quais linhas atendem a uma condição?
* Qual cidade tem mais estudantes?
* Qual vendedor vendeu mais?
* Como salvar um novo arquivo com os dados tratados?

---

## Pandas x NumPy

Pandas e NumPy são bibliotecas diferentes, mas trabalham muito bem juntas.

| Ferramenta | Melhor uso |
| ---------- | ---------- |
| NumPy | Cálculos numéricos, arrays, matrizes, operações vetorizadas |
| Pandas | Tabelas, dados com rótulos, arquivos CSV, limpeza e análise de dados |

O NumPy trabalha principalmente com arrays.

O Pandas trabalha principalmente com duas estruturas:

* `Series`;
* `DataFrame`.

Internamente, Pandas pode usar NumPy em várias operações, mas oferece uma interface mais amigável para trabalhar com dados tabulares.

---

## Instalando e importando Pandas

Caso seja necessário instalar, use o terminal:

```bash
python -m pip install pandas
```

> ℹ️ Use este comando dentro do ambiente virtual do projeto, como visto na aula sobre `venv` e `pip`. Material disponível [aqui](/venv_pip.md).

Depois, importamos no nosso código Python:

```python
import pandas as pd
```

Esse apelido `pd` é uma convenção muito comum na comunidade Python.

Exemplo:

```python
import pandas as pd

print(pd.__version__)
```

---

# 1. `Series`

Uma `Series` é uma estrutura de dados unidimensional.

Ela é parecida com uma lista ou com um array NumPy de uma dimensão, mas possui um diferencial importante: **índices**.

```python
import pandas as pd

notas = pd.Series([8.0, 7.5, 9.0, 6.5])

print(notas)
```

Saída:

```txt
0    8.0
1    7.5
2    9.0
3    6.5
dtype: float64
```

Observe que aparecem duas informações:

* À esquerda: o índice;
* À direita: o valor.

---

## Criando uma `Series` com índices personalizados

```python
import pandas as pd

notas = pd.Series(
    [8.0, 7.5, 9.0, 6.5],
    index=['Ana', 'Bruno', 'Carlos', 'Duda']
)

print(notas)
```

Saída:

```txt
Ana       8.0
Bruno     7.5
Carlos    9.0
Duda      6.5
dtype: float64
```

Agora os índices são os nomes dos estudantes.

Podemos acessar uma nota pelo índice:

```python
print(notas["Carlos"])
# 9.0
```

---

## Operações com `Series`

Assim como no NumPy, muitas operações são aplicadas de forma vetorizada.

```python
notas_corrigidas = notas + 0.5

print(notas_corrigidas)
```

Também podemos calcular estatísticas:

```python
print(notas.mean())
print(notas.min())
print(notas.max())
print(notas.std())
```

---

# 2. `DataFrame`

Um `DataFrame` é a principal estrutura do Pandas.

Ele representa uma tabela com linhas e colunas.

Podemos pensar em um `DataFrame` como uma planilha dentro do Python.

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "idade": [18, 21, 19, 20],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão"],
    "nota": [8.5, 6.0, 9.0, 5.5]
}

df = pd.DataFrame(dados)

print(df)
```

Saída:

```txt
     nome  idade    cidade  nota
0     Ana     18    Recife   8.5
1   Bruno     21    Olinda   6.0
2  Carlos     19    Recife   9.0
3    Duda     20  Jaboatão   5.5
```

---

## Entendendo o `DataFrame`

No exemplo anterior:

* Cada coluna tem um nome;
* Cada linha representa um registro;
* O índice aparece à esquerda;
* Cada coluna pode ter um tipo de dado diferente.

Essa é uma das grandes vantagens do Pandas em relação ao NumPy.

Em uma mesma tabela, podemos ter:

* Texto;
* Números;
* Datas;
* Categorias;
* Valores ausentes.

---

# 3. Visualizando dados

Quando trabalhamos com uma tabela grande, não devemos imprimir tudo de uma vez.

Pandas oferece métodos úteis para conhecer os dados aos poucos.

Vamos usar este exemplo:

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda", "Eduardo", "Fernanda"],
    "idade": [18, 21, 19, 20, 22, 18],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão", "Recife", "Olinda"],
    "nota": [8.5, 6.0, 9.0, 5.5, 6.9, 4.5]
}

df = pd.DataFrame(dados)
```

---

## `head()`

Mostra as primeiras linhas da tabela.

```python
print(df.head())
```

Também podemos escolher a quantidade:

```python
print(df.head(3))
```

---

## `tail()`

Mostra as últimas linhas da tabela.

```python
print(df.tail())
```

---

## `info()`

Mostra informações gerais da tabela.

```python
df.info()
```

Esse método ajuda a identificar:

* Quantidade de linhas;
* Quantidade de colunas;
* Nome das colunas;
* Tipos de dados;
* Quantidade de valores não nulos.

---

## `describe()`

Mostra estatísticas descritivas das colunas numéricas.

```python
print(df.describe())
```

Exemplo de informações apresentadas:

* Quantidade;
* Média;
* Desvio padrão;
* Menor valor;
* Quartis;
* Maior valor.

---

## `shape`, `columns` e `dtypes`

```python
print(df.shape)
print(df.columns)
print(df.dtypes)
```

* `shape`: mostra o formato da tabela;
* `columns`: mostra os nomes das colunas;
* `dtypes`: mostra os tipos de dados de cada coluna.

---

# 4. Selecionando colunas

## Uma coluna

```python
print(df["nome"])
```

O resultado é uma `Series`.

---

## Várias colunas

Para selecionar várias colunas, usamos uma lista de nomes dentro dos colchetes.

```python
print(df[["nome", "nota"]])
```

Nesse caso, como estamos selecionando várias colunas, o resultado é um `DataFrame`.

---

# 5. Selecionando linhas com `loc` e `iloc`

Pandas possui duas formas muito comuns de selecionar linhas e colunas:

* `loc`: seleção por rótulo;
* `iloc`: seleção por posição.

---

## `iloc`

Usamos `iloc` quando queremos selecionar pela posição.

```python
print(df.iloc[0])
```

Esse código pega a primeira linha.

Também podemos selecionar linhas e colunas:

```python
print(df.iloc[0, 3])
```

Esse código pega o valor da linha 0 e coluna 3.

---

## `loc`

Usamos `loc` quando queremos selecionar pelo rótulo do índice ou pelo nome da coluna.

```python
print(df.loc[0, "nome"])
```

Esse código pega o valor da linha com índice 0 na coluna `"nome"`.

Também podemos selecionar várias colunas:

```python
print(df.loc[0, ["nome", "nota"]])
```

---

# 6. Filtrando dados

Uma das operações mais importantes em análise de dados é filtrar linhas.

Imagine que queremos selecionar apenas estudantes com nota maior ou igual a 7.

```python
aprovados = df[df["nota"] >= 7]

print(aprovados)
```

O que acontece aqui?

```python
df["nota"] >= 7
```

gera uma máscara booleana:

```txt
0     True
1    False
2     True
3    False
4     True
5    False
Name: nota, dtype: bool
```

Depois usamos essa máscara para filtrar o `DataFrame`.

---

## Filtros com texto

```python
recife = df[df["cidade"] == "Recife"]

print(recife)
```

---

## Filtros com múltiplas condições

```python
recife_aprovados = df[(df["cidade"] == "Recife") & (df["nota"] >= 7)]

print(recife_aprovados)
```

> ⚠️ Assim como no NumPy, em Pandas usamos `&` para combinar condições com “e”, e cada condição deve ficar entre parênteses.

Também podemos usar `|` para representar “ou”:

```python
recife_ou_olinda = df[(df["cidade"] == "Recife") | (df["cidade"] == "Olinda")]

print(recife_ou_olinda)
```

---

# 7. Criando e alterando colunas

Podemos criar novas colunas a partir de valores existentes.

```python
df["nota_corrigida"] = df["nota"] + 0.5

print(df)
```

Também podemos criar uma coluna de situação:

```python
df["situacao"] = "Recuperação"

df.loc[df["nota"] >= 7, "situacao"] = "Aprovado"
df.loc[df["nota"] < 5, "situacao"] = "Reprovado"

print(df)
```

Esse código começa considerando todos em recuperação.

Depois altera:

* Quem tem nota maior ou igual a 7 para `"Aprovado"`;
* Quem tem nota menor que 5 para `"Reprovado"`.

---

# 8. Lendo arquivos CSV

Na aula de NumPy, vimos que `np.loadtxt()` funciona melhor com arquivos bem organizados e numéricos.

Com Pandas, ler arquivos CSV com cabeçalho e dados mistos é muito mais simples.

Imagine um arquivo chamado `estudantes.csv`:

```csv
nome,idade,cidade,nota
Ana,18,Recife,8.5
Bruno,21,Olinda,6.0
Carlos,19,Recife,9.0
Duda,20,Jaboatão,5.5
Eduardo,22,Recife,7.0
Fernanda,18,Olinda,4.5
```

Podemos carregar o arquivo assim:

```python
import pandas as pd

df = pd.read_csv("estudantes.csv")

print(df.head())
```

O Pandas identifica automaticamente:

* O cabeçalho;
* As colunas;
* Os tipos possíveis de cada coluna;
* O separador padrão, que é a vírgula.

---

## CSV com separador `;`

No Brasil, é comum encontrar arquivos CSV separados por ponto e vírgula.

Exemplo:

```csv
nome;idade;cidade;nota
Ana;18;Recife;8.5
Bruno;21;Olinda;6.0
```

Nesse caso:

```python
df = pd.read_csv("estudantes.csv", sep=";")
```

---

## CSV com vírgula decimal

Também é comum encontrar arquivos com vírgula como separador decimal.

Exemplo:

```csv
nome;idade;cidade;nota
Ana;18;Recife;8,5
Bruno;21;Olinda;6,0
```

Nesse caso:

```python
df = pd.read_csv("estudantes.csv", sep=";", decimal=",")
```

---

# 9. Valores ausentes

Dados reais frequentemente têm valores faltando. ~~Ou algum outro tipo de desgraça~~.

Em Pandas, valores ausentes podem aparecer como `NaN` (_Not a Number_, ou “não é um número”).

Exemplo:

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda", "Eduardo"],
    "idade": [18, 21, None, 20, 22],
    "nota": [8.5, None, 9.0, 5.5, 7.0]
}

df = pd.DataFrame(dados)

print(df)
```

---

## Identificando valores ausentes

```python
print(df.isna())
```

Para contar valores ausentes por coluna:

```python
print(df.isna().sum())
```

---

## Removendo linhas com valores ausentes

```python
df_sem_ausentes = df.dropna()

print(df_sem_ausentes)
```

Isso remove linhas que possuem pelo menos um valor ausente.

Também podemos remover considerando apenas uma coluna específica:

```python
df_sem_nota = df.dropna(subset=["nota"])

print(df_sem_nota)
```

---

## Preenchendo valores ausentes

Podemos preencher valores ausentes com um valor fixo:

```python
df["nota"] = df["nota"].fillna(0)

print(df)
```

Também podemos preencher com uma estatística:

```python
media_idade = df["idade"].mean()

df["idade"] = df["idade"].fillna(media_idade)

print(df)
```

> ⚠️ Preencher valores ausentes exige cuidado. Nem sempre substituir por `0` ou pela média é a melhor decisão. Isso depende do contexto do problema.

---

# 10. Convertendo tipos de dados

Às vezes, uma coluna numérica é carregada como texto.

Isso pode acontecer por causa de valores inválidos, vírgula decimal, espaços ou textos misturados.

Exemplo:

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda"],
    "nota": ["8.5", "6.0", "erro", "5.5"]
}

df = pd.DataFrame(dados)

print(df.dtypes)
```

Para converter a coluna `nota` para número:

```python
df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

print(df)
print(df.dtypes)
```

O parâmetro `errors="coerce"` transforma valores inválidos em `NaN`.

Depois podemos tratar os valores ausentes:

```python
df = df.dropna(subset=["nota"])
```

---

# 11. Ordenando dados

Podemos ordenar uma tabela por uma coluna.

```python
df_ordenado = df.sort_values("nota")

print(df_ordenado)
```

Para ordenar do maior para o menor:

```python
df_ordenado = df.sort_values("nota", ascending=False)

print(df_ordenado)
```

---

# 12. Agrupando dados com `groupby`

O `groupby` permite agrupar dados por uma ou mais colunas e calcular resumos.

Imagine esta tabela de vendas:

```python
import pandas as pd

dados = {
    "vendedor": ["Ana", "Ana", "Bruno", "Bruno", "Carlos", "Carlos"],
    "cidade": ["Recife", "Olinda", "Recife", "Olinda", "Recife", "Olinda"],
    "valor": [1200, 1500, 900, 1000, 2000, 2100]
}

df = pd.DataFrame(dados)
```

---

## Total por vendedor

```python
total_por_vendedor = df.groupby("vendedor")["valor"].sum()

print(total_por_vendedor)
```

Saída:

```txt
vendedor
Ana       2700
Bruno     1900
Carlos    4100
Name: valor, dtype: int64
```

---

## Média por vendedor

```python
media_por_vendedor = df.groupby("vendedor")["valor"].mean()

print(media_por_vendedor)
```

---

## Total por cidade

```python
total_por_cidade = df.groupby("cidade")["valor"].sum()

print(total_por_cidade)
```

---

## Mais de uma agregação

```python
resumo = df.groupby("vendedor")["valor"].agg(["sum", "mean", "min", "max"])

print(resumo)
```

---

# 13. Salvando dados em CSV

Depois de limpar ou transformar uma tabela, podemos salvar o resultado em um novo arquivo.

```python
df.to_csv("resultado.csv", index=False)
```

O parâmetro `index=False` evita salvar o índice como uma coluna extra.

Para salvar usando ponto e vírgula:

```python
df.to_csv("resultado.csv", sep=";", index=False)
```

---

# 🚀 Projeto Guiado: Análise de Estudantes

Vamos juntar os conceitos em um exemplo mais completo.

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda", "Eduardo", "Fernanda"],
    "cidade": ["Recife", "Olinda", "Recife", "Jaboatão", "Recife", "Olinda"],
    "avaliacao_1": [8.0, 6.0, 9.0, 4.0, 7.0, 5.0],
    "avaliacao_2": [7.5, 5.5, 8.5, 6.0, 7.0, 4.5],
    "avaliacao_3": [9.0, 7.0, 9.5, 5.0, 7.0, 6.0]
}

df = pd.DataFrame(dados)

df["media"] = df[["avaliacao_1", "avaliacao_2", "avaliacao_3"]].mean(axis=1)

df["situacao"] = "Recuperação"
df.loc[df["media"] >= 7, "situacao"] = "Aprovado"
df.loc[df["media"] < 5, "situacao"] = "Reprovado"

print(df)
```

---

## Filtrando estudantes aprovados

```python
aprovados = df[df["situacao"] == "Aprovado"]

print(aprovados[["nome", "media", "situacao"]])
```

---

## Média por cidade

```python
media_por_cidade = df.groupby("cidade")["media"].mean()

print(media_por_cidade)
```

---

## Salvando resultado

```python
df.to_csv("resultado_estudantes.csv", index=False)
```

---

# 14. Boas práticas com Pandas

1. **Use `import pandas as pd`**

   Essa é a convenção mais comum.

2. **Veja os dados antes de transformar**

   Use `head()`, `info()`, `describe()`, `shape` e `dtypes`.

3. **Confira valores ausentes**

   Use `isna().sum()` antes de remover ou preencher dados.

4. **Evite alterar dados sem entender o impacto**

   Remover linhas ou preencher valores ausentes pode mudar o resultado da análise.

5. **Use nomes claros para colunas**

   Prefira nomes como `nota`, `media`, `cidade`, `valor_venda`.

6. **Evite espaços e acentos nos nomes das colunas em projetos maiores**

   Isso facilita o acesso e reduz erros.

7. **Use `index=False` ao salvar CSV quando o índice não for importante**

   Isso evita criar uma coluna extra no arquivo.

8. **Não resolva tudo com `for`**

   Pandas foi criado para trabalhar com operações em colunas, filtros e agrupamentos.

9. **Crie arquivos de saída diferentes dos arquivos originais**

   Evite sobrescrever os dados brutos.

10. **Documente decisões de limpeza**

   Se você removeu linhas, preencheu valores ausentes ou converteu tipos, registre o motivo.

---

# 15. Resumo dos principais recursos

| Recurso | Para que serve | Exemplo |
| ------- | -------------- | ------- |
| `pd.Series()` | Criar uma série | `pd.Series([1, 2, 3])` |
| `pd.DataFrame()` | Criar uma tabela | `pd.DataFrame(dados)` |
| `pd.read_csv()` | Ler arquivo CSV | `pd.read_csv("dados.csv")` |
| `.head()` | Ver primeiras linhas | `df.head()` |
| `.tail()` | Ver últimas linhas | `df.tail()` |
| `.info()` | Ver estrutura geral | `df.info()` |
| `.describe()` | Ver estatísticas | `df.describe()` |
| `.shape` | Ver linhas e colunas | `df.shape` |
| `.columns` | Ver nomes das colunas | `df.columns` |
| `.dtypes` | Ver tipos das colunas | `df.dtypes` |
| `df["coluna"]` | Selecionar uma coluna | `df["nome"]` |
| `df[["a", "b"]]` | Selecionar várias colunas | `df[["nome", "nota"]]` |
| `.loc[]` | Selecionar por rótulo | `df.loc[0, "nome"]` |
| `.iloc[]` | Selecionar por posição | `df.iloc[0, 2]` |
| Filtro booleano | Filtrar linhas | `df[df["nota"] >= 7]` |
| `.isna()` | Identificar ausentes | `df.isna()` |
| `.dropna()` | Remover ausentes | `df.dropna()` |
| `.fillna()` | Preencher ausentes | `df["nota"].fillna(0)` |
| `pd.to_numeric()` | Converter para número | `pd.to_numeric(df["nota"], errors="coerce")` |
| `.sort_values()` | Ordenar dados | `df.sort_values("nota")` |
| `.groupby()` | Agrupar dados | `df.groupby("cidade")["nota"].mean()` |
| `.to_csv()` | Salvar CSV | `df.to_csv("saida.csv", index=False)` |

---

## 🧱 Exercícios fundamentais

### [Exercício 01] Criando um DataFrame

Crie um `DataFrame` com os seguintes dados:

```txt
nome      idade   cidade     nota
Ana       18      Recife     8.5
Bruno     21      Olinda     6.0
Carlos    19      Recife     9.0
Duda      20      Jaboatão   5.5
```

Depois exiba:

* A tabela completa;
* As duas primeiras linhas;
* O formato da tabela com `shape`;
* Os tipos das colunas com `dtypes`.

---

### [Exercício 02] Selecionando colunas

Usando o `DataFrame` do exercício anterior, exiba:

* Apenas a coluna `nome`;
* As colunas `nome` e `nota`;
* A primeira linha usando `iloc`;
* O nome da terceira pessoa usando `loc` ou `iloc`.

---

### [Exercício 03] Filtrando estudantes

Usando o mesmo `DataFrame`, filtre e exiba:

* Estudantes com nota maior ou igual a 7;
* Estudantes de Recife;
* Estudantes de Recife com nota maior ou igual a 7;
* Estudantes com nota entre 5 e 6.9.

---

### [Exercício 04] Criando colunas

Adicione uma nova coluna chamada `nota_corrigida`, somando `0.5` ponto à nota original.

Depois crie uma coluna chamada `situacao`, seguindo as regras:

* `Aprovado`: nota maior ou igual a 7;
* `Recuperação`: nota maior ou igual a 5 e menor que 7;
* `Reprovado`: nota menor que 5.

---

### [Exercício 05] Valores ausentes

Crie um `DataFrame` com os dados abaixo:

```python
dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Duda", "Eduardo"],
    "idade": [18, 21, None, 20, 22],
    "nota": [8.5, None, 9.0, 5.5, 7.0]
}
```

Depois:

* Exiba a quantidade de valores ausentes por coluna;
* Crie uma versão removendo linhas com valores ausentes;
* Crie outra versão preenchendo a nota ausente com `0`;
* Preencha a idade ausente com a média das idades.

---

### [Exercício 06] Agrupando dados

Crie um `DataFrame` com os dados abaixo:

```python
dados = {
    "vendedor": ["Ana", "Ana", "Bruno", "Bruno", "Carlos", "Carlos"],
    "cidade": ["Recife", "Olinda", "Recife", "Olinda", "Recife", "Olinda"],
    "valor": [1200, 1500, 900, 1000, 2000, 2100]
}
```

Calcule:

* Total vendido por vendedor;
* Média de venda por vendedor;
* Total vendido por cidade;
* Maior venda registrada;
* Vendedores com total acima de 3000.

---

## 🚀 Mini Projeto 9: PyNotas Pandas

### Contexto

Na aula de NumPy, você analisou notas usando arrays.

Agora, a coordenação do curso enviou uma planilha em formato CSV com informações dos estudantes.

Desta vez, além das notas, existem informações textuais como nome, cidade e turma.

### Dados iniciais

Crie um arquivo chamado `estudantes.csv` com o seguinte conteúdo:

```csv
nome,cidade,turma,avaliacao_1,avaliacao_2,avaliacao_3
Ana,Recife,A,8.0,7.5,9.0
Bruno,Olinda,A,6.0,5.5,7.0
Carlos,Recife,B,9.0,8.5,9.5
Duda,Jaboatão,B,4.0,6.0,5.0
Eduardo,Recife,A,7.0,7.0,7.0
Fernanda,Olinda,B,5.0,4.5,6.0
```

### O desafio

Crie um programa que:

1. Leia o arquivo `estudantes.csv`;
2. Exiba as primeiras linhas da tabela;
3. Exiba informações gerais com `info()`;
4. Calcule a média de cada estudante;
5. Crie a coluna `situacao`;
6. Exiba os estudantes aprovados;
7. Exiba os estudantes em recuperação;
8. Exiba os estudantes reprovados;
9. Calcule a média por turma;
10. Calcule a média por cidade;
11. Identifique o estudante com maior média;
12. Identifique o estudante com menor média;
13. Salve um novo arquivo chamado `resultado_estudantes.csv`.

### Regras

* Use Pandas;
* Use `read_csv`;
* Use filtros booleanos;
* Use `groupby`;
* Use `to_csv`;
* Evite resolver os cálculos principais com `for`;
* Mostre as informações com mensagens compreensíveis.

### Exemplo de saída esperada

```txt
Média por turma:
turma
A    6.97
B    6.50

Média por cidade:
cidade
Jaboatão    5.00
Olinda      5.67
Recife      8.06

Estudante com maior média: Carlos (9.00)
Estudante com menor média: Duda (5.00)
```

### ✨ Extra

Depois de implementar este desafio, gere um arquivo com dados sintéticos de 500 estudantes e adapte o programa para ler esse arquivo.

O início do arquivo deve ter os mesmos dados deste exercício. Os demais dados devem ser gerados de forma aleatória, respeitando a lógica do sistema, incluindo nomes, cidades, turmas e notas.

---

## 🚀 Mini Projeto 10: Análise de Vendas com Pandas

### Contexto

Uma loja registrou suas vendas em um arquivo CSV.

Cada linha representa uma venda realizada.

Diferente do exercício de NumPy, agora os dados estão em formato mais parecido com uma base real: cada venda tem vendedor, cidade, produto, categoria, quantidade e valor unitário.

### Dados iniciais

Crie um arquivo chamado `vendas.csv` com o seguinte conteúdo:

```csv
data,vendedor,cidade,produto,categoria,quantidade,valor_unitario
2026-01-05,Ana,Recife,Notebook,Eletrônicos,2,3500
2026-01-05,Bruno,Olinda,Mouse,Periféricos,5,80
2026-01-06,Ana,Recife,Teclado,Periféricos,3,150
2026-01-06,Carlos,Jaboatão,Monitor,Eletrônicos,2,1200
2026-01-07,Duda,Recife,Cadeira,Escritório,4,600
2026-01-07,Carlos,Olinda,Notebook,Eletrônicos,1,3500
2026-01-08,Bruno,Recife,Mouse,Periféricos,10,80
2026-01-08,Ana,Jaboatão,Cadeira,Escritório,2,600
```

### O desafio

Crie um programa que:

1. Leia o arquivo `vendas.csv`;
2. Exiba as primeiras linhas;
3. Exiba informações gerais da tabela;
4. Crie uma coluna `total`, multiplicando `quantidade` por `valor_unitario`;
5. Calcule o total vendido por vendedor;
6. Calcule o total vendido por cidade;
7. Calcule o total vendido por categoria;
8. Identifique o vendedor com maior total vendido;
9. Identifique a cidade com maior total vendido;
10. Exiba vendas com total maior ou igual a 1000;
11. Ordene as vendas pelo total, do maior para o menor;
12. Salve um arquivo chamado `relatorio_vendas.csv`.

### Regras

* Use Pandas;
* Use `read_csv`;
* Use criação de colunas;
* Use `groupby`;
* Use filtros booleanos;
* Use `sort_values`;
* Use `to_csv`.

### ✨ Extra

Depois de implementar este desafio, gere um arquivo com dados sintéticos de 1000 vendas e adapte o programa para ler esse arquivo.

O início do arquivo deve ter os mesmos dados deste exercício. Os demais dados devem ser gerados de forma aleatória, respeitando a lógica do sistema, incluindo datas, vendedores, cidades, produtos, categorias, quantidades e valores.

No final, salve:

* `relatorio_vendas.csv`, com todas as vendas e a coluna `total`;
* `resumo_vendedores.csv`, com o total vendido por vendedor;
* `resumo_cidades.csv`, com o total vendido por cidade;
* `resumo_categorias.csv`, com o total vendido por categoria.

---

## Referências úteis

* Documentação oficial do Pandas: <https://pandas.pydata.org/docs/>
* Guia introdutório "10 minutes to pandas": <https://pandas.pydata.org/docs/user_guide/10min.html>
* Introdução às estruturas de dados do Pandas: <https://pandas.pydata.org/docs/user_guide/dsintro.html>
* Leitura e escrita de dados tabulares: <https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html>
* `read_csv`: <https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html>
* `DataFrame.to_csv`: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html>
* Trabalhando com dados ausentes: <https://pandas.pydata.org/docs/user_guide/missing_data.html>

Acabou 👍👍
