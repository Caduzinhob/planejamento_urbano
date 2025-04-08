def calcular_estatisticas(grafo, matriz_caminhos):
    estatisticas = {
        "Quantidade de vértices": len(grafo.nos),
        "Quantidade de arestas": len(grafo.arestas),
        "Quantidade de arcos": len(grafo.arcos),
        "Quantidade de vértices requeridos": len(grafo.nos_requeridos),
        "Quantidade de arestas requeridas": len(grafo.arestas_requeridas),
        "Quantidade de arcos requeridos": len(grafo.arcos_requeridos),
        "Densidade do grafo": calcular_densidade(grafo),
        "Grau mínimo dos vértices": calcular_grau_minimo(grafo),
        "Grau máximo dos vértices": calcular_grau_maximo(grafo),
        "Intermediação": calcular_intermediacao(grafo, matriz_caminhos),
        "Caminho médio": calcular_caminho_medio(matriz_caminhos),
        "Diâmetro": calcular_diametro(matriz_caminhos),
    }
    return estatisticas

def calcular_densidade(grafo):
    num_vertices = len(grafo.nos)
    num_arestas_arcos = len(grafo.arestas) + len(grafo.arcos)
    if num_vertices > 1:
        return num_arestas_arcos / (num_vertices * (num_vertices - 1))
    return 0

def calcular_grau_minimo(grafo):
    graus = {no: 0 for no in grafo.nos}
    for de, para, _ in grafo.arestas + grafo.arcos:
        graus[de] += 1
        graus[para] += 1
    return min(graus.values()) if graus else None

def calcular_grau_maximo(grafo):
    graus = {no: 0 for no in grafo.nos}
    for de, para, _ in grafo.arestas + grafo.arcos:
        graus[de] += 1
        graus[para] += 1
    return max(graus.values()) if graus else None

def calcular_intermediacao(grafo, matriz_caminhos):
    intermediacao = {no: 0 for no in grafo.nos}
    for i in grafo.nos:
        for j in grafo.nos:
            if i != j:
                for k in grafo.nos:
                    if k != i and k != j:
                        if matriz_caminhos[i][j] == matriz_caminhos[i][k] + matriz_caminhos[k][j]:
                            intermediacao[k] += 1
    return intermediacao

def calcular_caminho_medio(matriz_caminhos):
    total_caminhos = 0
    soma_caminhos = 0
    for i in matriz_caminhos:
        for j in matriz_caminhos[i]:
            if i != j and matriz_caminhos[i][j] < float('inf'):
                soma_caminhos += matriz_caminhos[i][j]
                total_caminhos += 1
    return soma_caminhos / total_caminhos if total_caminhos > 0 else None

def calcular_diametro(matriz_caminhos):
    diametro = 0
    for i in matriz_caminhos:
        for j in matriz_caminhos[i]:
            if i != j and matriz_caminhos[i][j] < float('inf'):
                diametro = max(diametro, matriz_caminhos[i][j])
    return diametro