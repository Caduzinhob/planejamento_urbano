def calcular_estatisticas(grafo, matriz_caminhos):
    return {
        "Vértices": len(grafo.nos),
        "Arestas": len(grafo.arestas),
        "Arcos": len(grafo.arcos),
        "Vértices Requeridos": len(grafo.nos_requeridos),
        "Arestas Requeridas": len(grafo.arestas_requeridas),
        "Arcos Requeridos": len(grafo.arcos_requeridos),
        "Densidade": calcular_densidade(grafo),
        "Grau Mínimo": calcular_grauminimo(grafo),
        "Grau Máximo": calcular_graumaximo(grafo),
        "Caminho Médio": calcular_caminho_medio(matriz_caminhos),
        "Diâmetro": calcular_diametro(matriz_caminhos),
        "Intermediação Total": sum(calcular_intermediacao(grafo, matriz_caminhos).values())
    }
    return estatisticas

def calcular_densidade(grafo):
    num_vertices = len(grafo.nos)
    num_arestas_arcos = len(grafo.arestas) + len(grafo.arcos)
    if num_vertices > 1:
        return num_arestas_arcos / (num_vertices * (num_vertices - 1))
    return 0

def calcular_grauminimo(grafo):
    graus = {no: 0 for no in grafo.nos}

    # Corrigido para desempacotar os três valores
    for de, para, custo in grafo.arestas + grafo.arcos:
        graus[de] += 1
        graus[para] += 1

    return min(graus.values())

def calcular_graumaximo(grafo):
    graus = {no: 0 for no in grafo.nos}

    # Corrigido para desempacotar os três valores
    for de, para, custo in grafo.arestas + grafo.arcos:
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