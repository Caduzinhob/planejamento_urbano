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


# Graph Visualization for CARP Instances

## Overview
This module provides a Jupyter Notebook (`visualizacao_resultados.ipynb`) for visualizing graph metrics and statistics derived from CARP (Capacitated Arc Routing Problem) instances. The notebook generates a detailed table of metrics and a bar chart for numerical data, helping users analyze the structure and properties of the graph.

## Features
The visualization includes:
1. **Graph Metrics Table**:
   - Total number of vertices, edges, and arcs.
   - Number of required vertices, edges, and arcs.
   - Graph density, minimum and maximum vertex degrees.
   - Average path length and graph diameter.
   - Betweenness centrality (intermediation) for each vertex.

2. **Bar Chart**:
   - Displays numerical metrics for quick comparison.

## File Structure
- `visualizacao_resultados.ipynb`: The main notebook for graph visualization.
- `selected_instances/`: Folder containing `.dat` files with CARP instances.

## How to Use
1. **Open the Notebook**:
   - Launch Jupyter Notebook and open `visualizacao_resultados.ipynb`.

2. **Load a CARP Instance**:
   - Modify the `arquivo` variable in the notebook to point to the desired `.dat` file:
     ```python
     arquivo = r"d:\Meus arquivos\Documentos\GitHub\projeto_carp_grafos\selected_instances\BHW1.dat"
     ```

3. **Run the Notebook**:
   - Execute all cells to generate the metrics table and bar chart.

4. **Analyze the Results**:
   - The notebook will display:
     - A table with graph metrics.
     - A separate table for betweenness centrality (intermediation) values.
     - A bar chart for numerical metrics.

## Example Output
### Metrics Table
| Metric                     | Value     |
|----------------------------|-----------|
| Total de Vértices          | 56        |
| Total de Arestas           | 16        |
| Total de Arcos             | 31        |
| Vértices Requeridos        | 16        |
| Arestas Requeridas         | 16        |
| Arcos Requeridos           | 31        |
| Densidade                  | 0.015260  |
| Grau Mínimo                | 0         |
| Grau Máximo                | 5         |
| Caminho Médio              | 2.345678  |
| Diâmetro                   | 10        |

### Intermediation Table
| Vertex   | Intermediation |
|----------|----------------|
| 1        | 0.123456       |
| 2        | 0.234567       |
| 3        | 0.345678       |
| ...      | ...            |

### Bar Chart
A bar chart is generated to visualize numerical metrics such as density, average path length, and vertex degrees.

## Requirements
- Python 3.x
- Libraries:
  - `pandas`
  - `matplotlib`
  - `os`

Install the required libraries using:
```bash
pip install pandas matplotlib