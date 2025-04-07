def floyd_warshall(grafo):
    dist = {no: {no2: float('inf') for no2 in grafo.nos} for no in grafo.nos}
    for no in grafo.nos:
        dist[no][no] = 0  

    for de, para, custo in grafo.arestas:
        dist[de][para] = custo
        dist[para][de] = custo  

    for de, para, custo in grafo.arcos:
        dist[de][para] = custo  

    for k in grafo.nos:
        for i in grafo.nos:
            for j in grafo.nos:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist