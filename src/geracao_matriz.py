def floyd_warshall(grafo):
    # Inicializar a matriz de distâncias
    dist = {no: {no2: float('inf') for no2 in grafo.nos} for no in grafo.nos}
    for no in grafo.nos:
        dist[no][no] = 0  # Distância de um nó para ele mesmo é 0

    # Preencher a matriz com os custos das arestas e arcos
    for de, para, custo in grafo.arestas:
        dist[de][para] = custo
        dist[para][de] = custo  # Arestas são bidirecionais

    for de, para, custo in grafo.arcos:
        dist[de][para] = custo  # Arcos são direcionais

    # Algoritmo de Floyd-Warshall
    for k in grafo.nos:
        for i in grafo.nos:
            for j in grafo.nos:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist