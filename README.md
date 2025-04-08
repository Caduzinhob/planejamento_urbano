## Cabeçalho

Este é um trabalho da disciplina de Algoritmos em Grafos - GCC218

- Ministrado pelo: Professor Mayron César de Oliveira Moreira.
- Realizado pelo aluno:
- Carlos Eduardo Borges de Sousa - 202020296

# Planejamento Urbano
Trabalho de Grafos

Este projeto implementa um sistema para análise de grafos em problemas de planejamento urbano. Ele utiliza algoritmos para calcular estatísticas e métricas de grafos, como intermediação, caminho médio e diâmetro, além de gerar a matriz de caminhos mais curtos usando o algoritmo de Floyd-Warshall.

## Estrutura do Projeto

### Arquivos Principais
- **`grafo.py`**: Define a classe `Grafo`, que representa o grafo e armazena nós, arestas e arcos.
- **`ler_arquivo.py`**: Contém a função `ler_arquivo_ins_stdin`, que lê os dados de um arquivo `.ins` e constrói o grafo.
- **`geracao_matriz.py`**: Implementa o algoritmo de Floyd-Warshall para calcular a matriz de caminhos mais curtos.
- **`calcular_estatisticas.py`**: Contém funções para calcular estatísticas e métricas do grafo, como densidade, grau mínimo, grau máximo, intermediação, caminho médio e diâmetro.
- **`main.py`**: Arquivo principal que integra todas as funções e exibe as estatísticas do grafo.

---

## Funcionalidades

### 1. Classe `Grafo` (`grafo.py`)
A classe `Grafo` é responsável por armazenar os dados do grafo:
- **`adicionar_no(no)`**: Adiciona um nó ao grafo.
- **`adicionar_aresta(de, para, custo)`**: Adiciona uma aresta bidirecional ao grafo.
- **`adicionar_arco(de, para, custo)`**: Adiciona um arco direcionado ao grafo.
- **`adicionar_no_requerido(no)`**: Adiciona um nó requerido ao grafo.
- **`adicionar_aresta_requerida(de, para, custo)`**: Adiciona uma aresta requerida ao grafo.
- **`adicionar_arco_requerido(de, para, custo)`**: Adiciona um arco requerido ao grafo.

---

### 2. Leitura do Arquivo `.ins` (`ler_arquivo.py`)
A função `ler_arquivo_ins_stdin` lê os dados de um arquivo `.ins` e constrói o grafo:
- Lê nós, arestas e arcos do arquivo.
- Adiciona os elementos ao grafo principal e às listas de elementos requeridos.

---

### 3. Algoritmo de Floyd-Warshall (`geracao_matriz.py`)
A função `floyd_warshall` calcula a matriz de caminhos mais curtos:
- Inicializa uma matriz de distâncias com valores infinitos.
- Preenche a matriz com os custos das arestas e arcos.
- Aplica o algoritmo de Floyd-Warshall para calcular os menores caminhos entre todos os pares de nós.

---

### 4. Estatísticas e Métricas do Grafo (`calcular_estatisticas.py`)
A função `calcular_estatisticas` calcula as seguintes métricas:
- **Quantidade de vértices, arestas e arcos**: Conta os elementos do grafo.
- **Densidade do grafo**: Mede a conectividade do grafo.
- **Grau mínimo e máximo dos vértices**: Calcula os graus dos nós.
- **Intermediação**: Mede a importância de cada nó nos caminhos mais curtos.
- **Caminho médio**: Calcula a média dos comprimentos dos caminhos mais curtos.
- **Diâmetro**: Determina o maior caminho mais curto no grafo.

---

## Como Executar o Programa

### 1. Executar o Programa Principal
Para executar o programa principal e calcular as estatísticas do grafo, utilizar o seguinte comando no terminal, modificando a instancia que quiser testar:

- Rode o comando `python ./src/main.py < ./ins/03.ins` no cmd.

## Iniciar o Jupyter Notebook

- Rode o comando `jupyter notebook` no cmd, ele então abrirá a aba no navegador.


## Visualização de Estatísticas do Grafo

O notebook `visualizacao_resultados.ipynb` foi desenvolvido para facilitar a análise de estatísticas de grafos gerados a partir de arquivos `.ins`. Ele realiza as seguintes etapas:

1. **Carregamento de Arquivo `.ins`**:
   - O notebook utiliza a função `ler_arquivo_ins_arquivo` para carregar uma instância de grafo a partir de um arquivo `.ins`.

2. **Cálculo de Estatísticas**:
   - As estatísticas do grafo são calculadas utilizando as funções `floyd_warshall` (para gerar a matriz de distâncias) e `calcular_estatisticas`.

3. **Exibição em Tabela**:
   - As estatísticas calculadas são organizadas em um `DataFrame` do `pandas` e exibidas em formato de tabela estilizada.

4. **Visualização Gráfica**:
   - As métricas numéricas do grafo são exibidas em um gráfico de barras utilizando a biblioteca `matplotlib`.

### Como Utilizar

1. Atualize o caminho do arquivo `.ins` no notebook para ver as estatiscas de cada intancia,
depois é só utilizar o botão de execução:

   ```python
   arquivo = [
       r"D:\\Meus arquivos\\Documentos\\GitHub\\planejamento_urbano\\ins\\09.ins"
   ]