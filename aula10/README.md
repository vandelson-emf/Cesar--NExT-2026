# NExT 26.1 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 10 - NumPy

### Na aula de hoje

* O que é o NumPy;
* NumPy em análise de dados;
* Diferenças entre listas Python e arrays NumPy;
* Atributos principais: `ndim`, `shape`, `size` e `dtype`;
* Operações vetorizadas;
* Agregações com `sum`, `mean`, `min`, `max` e `std`;
* Boas práticas no uso de NumPy.

---

## 🎲 NumPy

**NumPy** significa **Numerical Python**.

Ele é uma biblioteca do Python criada para trabalhar com dados numéricos de forma eficiente, especialmente quando precisamos lidar com muitos valores ao mesmo tempo.

O NumPy permite criar e manipular estruturas parecidas com listas, mas muito mais adequadas para cálculos matemáticos, estatísticos e científicos.

Na prática, NumPy costuma aparecer principalmente nas etapas de transformação e exploração dos dados. Depois que os dados são extraídos de uma fonte, podemos usar arrays para calcular médias, somas, filtros, distribuições e outros resumos numéricos.

A estrutura principal do NumPy se chama **array**, ou mais especificamente `ndarray`, que significa **N-dimensional array**.

Um array pode ter:

* Uma dimensão: parecido com uma lista simples;
* Duas dimensões: parecido com uma tabela ou matriz;
* Três ou mais dimensões: usado em imagens, vídeos, tensores e dados mais complexos.

Exemplo:

```txt
Array 1D:
[10, 20, 30, 40]

Array 2D:
[
    [10, 20, 30],
    [40, 50, 60]
]

Array 3D:
[
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
```

### Por que usamos o NumPy?

O NumPy é um projeto [open source](https://github.com/numpy/numpy) e é uma das bases do ecossistema de dados em Python. Muitas bibliotecas importantes usam NumPy direta ou indiretamente, como:

* Pandas;
* Matplotlib;
* Scikit-learn;
* SciPy;
* OpenCV;
* TensorFlow;
* PyTorch.

Ou seja: aprender NumPy ajuda a entender melhor várias ferramentas modernas de dados, visualização, inteligência artificial e computação científica.

## O limite das listas

Até agora, usamos listas para armazenar coleções de valores:

```python
notas = [7.5, 8.0, 6.5, 9.0]
```

Listas são muito úteis, flexíveis e fáceis de usar. Elas podem guardar diferentes tipos de dados:

```python
mistura = ['Ana', 28, True, 9.5]
```

Essa flexibilidade é ótima para muitos problemas, mas pode ser ruim quando queremos fazer cálculos numéricos em grande escala.

Imagine que temos uma lista de notas e queremos adicionar 1 ponto em cada nota:

```python
notas = [7.5, 8.0, 6.5, 9.0]
notas_corrigidas = []

for nota in notas:
    notas_corrigidas.append(nota + 1)

print(notas_corrigidas)
```

Saída:

```python
[8.5, 9.0, 7.5, 10.0]
```

Funciona. Mas perceba que precisamos escrever um `for` para aplicar a operação em cada item.

Com NumPy, essa ideia fica mais direta.

---

## Instalando e importando NumPy

Em muitos ambientes de análise de dados, como Google Colab, Anaconda e alguns notebooks online, o NumPy já vem instalado.

Caso seja necessário instalar, usamos o terminal:

```bash
python -m pip install numpy
```

> ℹ️ Ou, usando um **ambiente virtual**, como explicado [aqui](/venv_pip.md).

Depois, importamos no nosso código Python:

```python
import numpy as np
```

Esse apelido `np` é uma convenção muito comum na comunidade Python. Ele deixa o código mais curto e ainda é fácil de reconhecer.

Exemplo:

```python
import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0])
print(notas)
```

Saída:

```python
[7.5 8.  6.5 9. ]
```

> 💡 Observe que a saída não aparece exatamente igual a uma lista Python. Arrays NumPy têm sua própria representação.

---

## Primeira diferença importante: lista x array

Vamos comparar uma lista Python com um array NumPy.

```python
lista = [10, 20, 30]
array = np.array([10, 20, 30])
```

Agora vamos tentar somar 5.

```python
print(lista + [5])
# saída: [10, 20, 30, 5]
```

Em listas, o operador `+` concatena listas.

Agora com NumPy:

```python
print(array + 5)
# saída: [15 25 35]
```

No NumPy, a operação foi aplicada em cada elemento do array.

Essa é uma diferença fundamental: **arrays NumPy foram pensados para operações matemáticas com muitos valores ao mesmo tempo**.

---

## Vetorização

**Vetorização** é a capacidade de aplicar uma operação a vários valores de uma vez, sem escrever manualmente um `for`.

Com lista:

```python
precos = [100, 200, 300]
precos_com_desconto = []

for preco in precos:
    precos_com_desconto.append(preco * 0.9)

print(precos_com_desconto)
```

Com NumPy:

```python
import numpy as np

precos = np.array([100, 200, 300])
precos_com_desconto = precos * 0.9

print(precos_com_desconto)
```

Saída:

```python
[ 90. 180. 270.]
```

O NumPy não elimina a repetição internamente. O que ele faz é executar essa repetição de maneira muito mais otimizada, usando implementações eficientes por baixo da linguagem Python.

Para quem está aprendendo, a ideia principal é:

> Em vez de pensar “vou percorrer cada elemento”, começamos a pensar “vou aplicar uma operação ao conjunto inteiro”.

---

## Criando arrays

### Criando um array a partir de uma lista

```python
import numpy as np

idades = np.array([18, 21, 25, 30])
print(idades)
```

### Criando um array com números sequenciais

```python
numeros = np.arange(0, 10)
print(numeros)
#[0 1 2 3 4 5 6 7 8 9]
```

Também podemos definir um intervalo com passo:

```python
pares = np.arange(0, 11, 2)
print(pares)
#[ 0  2  4  6  8 10]
```

### Criando arrays preenchidos com zero ou um

```python
zeros = np.zeros(5)
print(zeros)
#[0. 0. 0. 0. 0.]

uns = np.ones(4)
print(uns)
#[1. 1. 1. 1.]
```

### Criando uma matriz de zeros

```python
matriz = np.zeros((3, 4))
print(matriz)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
```

Aqui criamos uma matriz com 3 linhas e 4 colunas.

### Criando valores igualmente espaçados

```python
valores = np.linspace(0, 1, 5)
print(valores)
#[0.   0.25 0.5  0.75 1.  ]
```

`linspace` é útil quando queremos dividir um intervalo em uma quantidade específica de partes.

---

## Principais atributos de um array

Um array NumPy carrega informações importantes sobre sua estrutura.

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0]
])
```

### `ndim` - número de dimensões

```python
print(notas.ndim)
#2
```

Esse array tem duas dimensões: linhas e colunas.

### `shape` - formato do array

```python
print(notas.shape)
#(2, 3)
```

Isso significa que o array tem 2 linhas e 3 colunas.

### `size` - quantidade total de elementos

```python
print(notas.size)
#6
```

### `dtype` - tipo dos dados

```python
print(notas.dtype)
#float64
```

O `dtype` indica o tipo de dado armazenado no array.

Diferente de uma lista, um array NumPy normalmente trabalha melhor quando todos os valores são do mesmo tipo.

---

## Indexação e fatiamento

Arrays NumPy podem ser acessados de forma parecida com listas.

### Array 1D

```python
notas = np.array([7.5, 8.0, 6.5, 9.0])

print(notas[0])
print(notas[1])
print(notas[-1])
```

### Fatiamento em array 1D

```python
print(notas[1:3])
#[8.  6.5]
```

### Array 2D

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0]
])
```

Podemos acessar uma posição informando linha e coluna:

```python
print(notas[0, 0])
print(notas[2, 1])
#8.0
#8.5
```

### Pegando uma linha inteira

```python
print(notas[0])
#[8.  7.5 9. ]
```

### Pegando uma coluna inteira

```python
print(notas[:, 1])
#[7.5 8.  8.5]
```

O `:` significa “todas as linhas”.

Então:

```python
notas[:, 1]
```

Significa:

> Pegue todas as linhas da coluna 1.

---

## Operações matemáticas com arrays

```python
notas = np.array([7.0, 8.0, 6.0, 9.0])
```

### Soma

```python
print(notas + 1)
#[ 8.  9.  7. 10.]
```

### Subtração

```python
print(notas - 0.5)
```

### Multiplicação

```python
print(notas * 2)
```

### Divisão

```python
print(notas / 2)
```

### Operações entre arrays

```python
notas_unidade_1 = np.array([7.0, 8.0, 6.0])
notas_unidade_2 = np.array([8.0, 7.5, 9.0])

media = (notas_unidade_1 + notas_unidade_2) / 2
print(media)
#[7.5  7.75 7.5 ]
```

Nesse caso, o NumPy soma posição com posição:

```txt
[7.0, 8.0, 6.0]
+
[8.0, 7.5, 9.0]
=
[15.0, 15.5, 15.0]
```

Depois divide tudo por 2.

---

## Funções de agregação

Funções de agregação resumem muitos valores em um resultado.

```python
notas = np.array([7.5, 8.0, 6.5, 9.0, 10.0])
```

### Soma

```python
print(notas.sum())
```

### Média

```python
print(notas.mean())
```

### Menor valor

```python
print(notas.min())
```

### Maior valor

```python
print(notas.max())
```

### Desvio padrão

```python
print(notas.std())
```

O desvio padrão indica o quanto os valores estão espalhados em relação à média.

* Desvio padrão baixo: valores mais próximos da média;
* Desvio padrão alto: valores mais espalhados.

Exemplo:

```python
turma_a = np.array([7.0, 7.1, 7.2, 7.0, 7.1])
turma_b = np.array([3.0, 5.0, 7.0, 9.5, 10.0])

print(turma_a.mean(), turma_a.std())
print(turma_b.mean(), turma_b.std())
```

Mesmo que duas turmas tenham médias parecidas, elas podem ter distribuições bem diferentes.

---

## Entendendo `axis`

O parâmetro `axis` é um dos pontos que mais confunde no começo.

Vamos usar uma tabela de notas:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [8.5, 5.6, 7.8],
    [7.5, 9.0, 9.0]
])
```

Imagine que:

* Cada linha representa um estudante;
* Cada coluna representa uma avaliação.

```txt
             Avaliação 1   Avaliação 2   Avaliação 3
Estudante 1      8.0           7.5           9.0
Estudante 2      6.5           8.0           7.0
Estudante 3      9.5           8.5          10.0
Estudante 4      8.5           5.6           7.8
Estudante 5      7.5           9.0           9.0
```

### Média geral

```python
print(notas.mean())
```

Aqui o NumPy calcula a média de todos os valores.

### Média por coluna

```python
print(notas.mean(axis=0))
```

Saída:

```python
[8.   7.72 8.56]
```

`axis=0` percorre as linhas e calcula o resultado por coluna.

Pergunta-guia:

> Qual foi a média da turma em cada avaliação?

### Média por linha

```python
print(notas.mean(axis=1))
```

Saída:

```python
[8.16666667 7.16666667 9.33333333 7.3        8.5       ]
```

`axis=1` percorre as colunas e calcula o resultado por linha.

Logo...

> `axis=0` → calcula ao longo das linhas e retorna um resultado por coluna\
> `axis=1` → calcula ao longo das colunas e retorna um resultado por linha

---

## Máscaras booleanas

Máscaras booleanas são uma forma muito útil de filtrar dados.

```python
notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0])
```

Vamos descobrir quais notas são maiores ou iguais a 7:

```python
aprovadas = notas >= 7
print(aprovadas)
#[False  True  True False  True]
```

Agora podemos usar essa máscara para filtrar o array:

```python
print(notas[aprovadas])
#[7.  8.5 9. ]
```

Podemos fazer direto:

```python
print(notas[notas >= 7])
```

Também podemos contar quantos valores atendem à condição:

```python
print((notas >= 7).sum())
```

Como `True` vale 1 e `False` vale 0 em operações numéricas, a soma indica quantos itens passaram no teste.

---

## Broadcasting

**Broadcasting** é o mecanismo que permite ao NumPy realizar operações entre arrays de formatos diferentes, desde que eles sejam compatíveis.

O exemplo mais simples é somar um número a um array:

```python
valores = np.array([10, 20, 30])
print(valores + 5)
#[15 25 35]
```

O número `5` foi aplicado a todos os elementos.

Agora veja um exemplo com matriz:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0]
])

pesos = np.array([2, 3, 5])

notas_ponderadas = notas * pesos
print(notas_ponderadas)
#[[16.  22.5 45. ]
# [13.  24.  35. ]
# [19.  25.5 50. ]]
```

O array `pesos` tem 3 valores. A matriz `notas` tem 3 colunas. O NumPy consegue aplicar os pesos em cada linha.

Depois podemos calcular uma média ponderada:

```python
media_ponderada = notas_ponderadas.sum(axis=1) / pesos.sum()
print(media_ponderada)
#[8.35 7.2  9.45]
```

---

## Exemplo: Análise de Notas

Agora vamos juntar os conceitos.

### Dados iniciais

```python
import numpy as np

nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0]
])
```

Cada linha representa um estudante.
Cada coluna representa uma avaliação.

### Média de cada estudante

```python
medias = notas.mean(axis=1)
print(medias)
```

### Situação de aprovação

```python
aprovados = medias >= 7
print(aprovados)
```

### Mostrar apenas estudantes aprovados

```python
print(nomes[aprovados])
print(medias[aprovados])
```

### Mostrar estudantes em recuperação

```python
recuperacao = (medias >= 5) & (medias < 7)

print(nomes[recuperacao])
print(medias[recuperacao])
```

> ⚠️ Em NumPy, para combinar condições, usamos `&` em vez de `and`, e cada condição deve ficar entre parênteses.

### Mostrar estudantes reprovados

```python
reprovados = medias < 5

print(nomes[reprovados])
print(medias[reprovados])
```

---

## Carregando dados simples com NumPy

Em aulas anteriores, vocês trabalharam com arquivos CSV usando o módulo `csv`.

O NumPy também possui recursos para carregar dados numéricos de arquivos.

Para esta primeira aula, vamos usar um exemplo simples.

Imagine um arquivo `notas.csv` com o seguinte conteúdo:

```csv
8.0,7.5,9.0
6.0,5.5,7.0
9.0,8.5,9.5
4.0,6.0,5.0
```

Podemos carregar esse arquivo assim:

```python
import numpy as np

notas = np.loadtxt('notas.csv', delimiter=',')
print(notas)
```

Depois podemos calcular:

```python
print(notas.mean())
print(notas.mean(axis=0))
print(notas.mean(axis=1))
```

> ⚠️ `np.loadtxt` funciona melhor quando os dados são bem organizados e numéricos. Para arquivos CSV com cabeçalho, texto, valores ausentes ou dados mistos, normalmente usamos outras estratégias, como `csv`, `pandas` ou limpeza prévia dos dados.

---

## Boas práticas com NumPy

1. **Use `import numpy as np`**

   Essa é a convenção mais comum.

2. **Prefira operações vetorizadas quando fizer sentido**

   Em vez de criar muitos `for`, procure pensar em operações sobre o array inteiro.

3. **Observe o formato dos dados com `shape`**

   Muitos erros acontecem porque o array não está no formato esperado.

4. **Verifique o tipo dos dados com `dtype`**

   Dados importados de arquivos podem vir como texto, inteiro ou decimal.

5. **Use nomes claros**

   Prefira `notas`, `medias`, `precos`, `vendas` em vez de `x`, `a`, `b`, quando estiver aprendendo.

6. **Não use NumPy para tudo**

   Se você só tem poucos valores simples ou dados muito heterogêneos, listas e dicionários podem ser suficientes.

7. **Cuidado com cópias e alterações**

   Algumas operações podem gerar cópias; outras podem gerar visualizações dos mesmos dados. Em aulas introdutórias, o mais importante é testar e observar o comportamento.

---

## Resumo dos principais recursos

| Recurso          | Para que serve                     | Exemplo                                  |
| ---------------- | ---------------------------------- | ---------------------------------------- |
| `np.array()`     | Criar array a partir de lista      | `np.array([1, 2, 3])`                    |
| `np.arange()`    | Criar sequência numérica           | `np.arange(0, 10, 2)`                    |
| `np.linspace()`  | Criar valores igualmente espaçados | `np.linspace(0, 1, 5)`                   |
| `np.zeros()`     | Criar array preenchido com zero    | `np.zeros((3, 4))`                       |
| `np.ones()`      | Criar array preenchido com um      | `np.ones(5)`                             |
| `.ndim`          | Ver número de dimensões            | `array.ndim`                             |
| `.shape`         | Ver formato do array               | `array.shape`                            |
| `.size`          | Ver total de elementos             | `array.size`                             |
| `.dtype`         | Ver tipo dos dados                 | `array.dtype`                            |
| `.sum()`         | Somar valores                      | `notas.sum()`                            |
| `.mean()`        | Calcular média                     | `notas.mean()`                           |
| `.min()`         | Menor valor                        | `notas.min()`                            |
| `.max()`         | Maior valor                        | `notas.max()`                            |
| `.std()`         | Desvio padrão                      | `notas.std()`                            |
| Máscara booleana | Filtrar dados por condição         | `notas[notas >= 7]`                      |
| `axis=0`         | Agregar por coluna                 | `notas.mean(axis=0)`                     |
| `axis=1`         | Agregar por linha                  | `notas.mean(axis=1)`                     |
| `np.loadtxt()`   | Ler arquivo numérico simples       | `np.loadtxt('notas.csv', delimiter=',')` |

---

## 🧱 Exercícios fundamentais

### [Exercício 01] Criando arrays

Crie um array NumPy com os seguintes valores:

```python
[10, 20, 30, 40, 50]
```

Depois exiba:

* O array completo;
* O primeiro valor;
* O último valor;
* A quantidade total de elementos;
* O tipo dos dados.

---

### [Exercício 02] Corrigindo notas

Dado o array:

```python
notas = np.array([6.0, 7.5, 8.0, 5.5, 9.0])
```

Crie um novo array adicionando `0.5` ponto a cada nota.

Depois exiba:

* As notas originais;
* As notas corrigidas;
* A média antes da correção;
* A média depois da correção.

---

### [Exercício 03] Preços com desconto

Dado o array:

```python
precos = np.array([100, 250, 80, 300, 150])
```

Calcule um novo array com 10% de desconto.

Depois exiba:

* Os preços originais;
* Os preços com desconto;
* O maior preço original;
* O menor preço com desconto.

---

### [Exercício 04] Aprovados e recuperação

Dado o array:

```python
notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0, 6.5])
```

Crie filtros para exibir:

* Notas maiores ou iguais a 7;
* Notas entre 5 e 6.9;
* Notas menores que 5;
* Quantidade de estudantes aprovados.

---

### [Exercício 05] Matriz de notas

Dado o array:

```python
notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [5.0, 6.0, 6.5]
])
```

Calcule:

* A média geral;
* A média de cada estudante;
* A média de cada avaliação;
* A maior nota da matriz;
* A menor nota da matriz.

---

### [Exercício 06] Pesos das avaliações

Considere que as três avaliações possuem os seguintes pesos:

```python
pesos = np.array([2, 3, 5])
```

Usando a matriz de notas do exercício anterior, calcule a média ponderada de cada estudante.

Dica:

```python
notas_ponderadas = notas * pesos
```

Depois pense:

* Por que essa multiplicação funciona?
* O que aconteceria se `pesos` tivesse apenas 2 valores?

---

## 🚀 Mini Projeto 7: PyNotas NumPy

### Contexto

A coordenação de um curso recebeu uma tabela simples de notas de uma turma. Cada linha representa um estudante e cada coluna representa uma avaliação.

A equipe precisa de um pequeno programa que ajude a gerar um resumo da situação da turma.

### Dados iniciais

Use os dados abaixo diretamente no código:

```python
import numpy as np

nomes = np.array([
    'Ana',
    'Bruno',
    'Carlos',
    'Duda',
    'Eduardo',
    'Fernanda'
])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0],
    [7.0, 7.0, 7.0],
    [5.0, 4.5, 6.0]
])
```

### O desafio

Crie um programa que calcule e exiba:

1. A média de cada estudante (com nome);
2. A média da turma em cada avaliação;
3. A média geral da turma;
4. O nome dos estudantes aprovados (média maior ou igual a 7);
5. O nome dos estudantes em recuperação (média maior ou igual a 5 e menor que 7);
6. O nome dos estudantes reprovados (média menor que 5);
7. A maior média da turma (com nome);
8. A menor média da turma (com nome).

### Regras

* Use NumPy;
* Use máscaras booleanas;
* Use `axis` para calcular médias por linha e por coluna;
* Evite resolver tudo com `for`;
* Organize o código com variáveis claras;
* Mostre as informações com mensagens compreensíveis.

### Exemplo de saída esperada

```txt
Médias dos estudantes:
Ana: 8.17
Bruno: 6.17
Carlos: 9.00
Duda: 5.00
Eduardo: 7.00
Fernanda: 5.17

Média por avaliação:
Avaliação 1: 6.50
Avaliação 2: 6.42
Avaliação 3: 7.25

Média geral da turma: 6.72

Aprovados: Ana, Carlos, Eduardo
Recuperação: Bruno, Duda, Fernanda
Reprovados: nenhum estudante
```

### ✨ Extra

Depois de implementar este desafio, crie um módulo que gere um arquivo com dados sintéticos de 500 estudantes e adapte o programa atual para ler os dados desse arquivo.\
O início do arquivo deve ter os mesmos dados deste exercício. Os demais dados devem ser gerados de forma aleatória, respeitando a lógica do sistema, incluindo nomes e notas.

---

## 🚀 Mini Projeto 8: Análise de Vendas

### Contexto

Uma loja registrou o total de vendas de 4 vendedores ao longo de 5 dias.

```python
vendedores = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])

dias = np.array(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'])

vendas = np.array([
    [1200, 1500, 1100, 1800, 2000],
    [900,  1000, 950,  1200, 1300],
    [2000, 2100, 1900, 2200, 2500],
    [700,  850,  800,  950,  1000]
])
```

### O desafio

Calcule:

1. Total vendido por vendedor;
2. Total vendido por dia;
3. Média de vendas por vendedor;
4. Vendedor com maior total de vendas;
5. Dia com maior venda total;
6. Vendedores que venderam mais de 7000 no total.

### Dicas

* Use `sum(axis=1)` para total por vendedor;
* Use `sum(axis=0)` para total por dia;
* Use máscaras booleanas para filtrar vendedores;
* Use `np.argmax()` para encontrar a posição do maior valor.

### ✨ Extra

Depois de implementar este desafio, crie um módulo que gere um arquivo com dados sintéticos de 50 vendedores e adapte o programa atual para ler os dados desse arquivo.\
O início do arquivo deve ter os mesmos dados deste exercício. Os demais dados devem ser gerados de forma aleatória, respeitando a lógica do sistema, incluindo nomes e vendas.\
No final o programa deve salvar o relatório em um arquivo de resultados.
