def floydwarshall(grafo):
    no = sorted(grafo.nos)  # Corrigido para usar 'grafo.nos'
    n = len(no)
    idx = {no: i for i, no in enumerate(no)}

    # Inicialização da matriz
    dist = [[float('inf')] * n for i in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Preenchimento inicial
    for de, para, custo in grafo.arestas:
        i, j = idx[de], idx[para]
        dist[i][j] = min(dist[i][j], custo)
        dist[j][i] = min(dist[j][i], custo)

    for de, para, custo in grafo.arcos:
        i, j = idx[de], idx[para]
        dist[i][j] = min(dist[i][j], custo)

    # Algoritmo principal
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Corrigido para evitar sobrescrever a variável 'no'
    return {no_atual: {no[j]: dist[i][j] for j in range(n)} for i, no_atual in enumerate(no)}