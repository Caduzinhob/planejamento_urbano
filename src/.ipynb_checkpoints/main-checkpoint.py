from ler_arquivo import ler_arquivo_ins_stdin
from calcular_estatisticas import (
    calcular_estatisticas,
    calcular_intermediacao,
    calcular_caminho_medio,
    calcular_diametro
)
from geracao_matriz import floyd_warshall

def main():
    # Ler o grafo da entrada padrão
    grafo = ler_arquivo_ins_stdin()

    # Calcular a matriz de caminhos mais curtos
    matriz_caminhos = floyd_warshall(grafo)

    for origem, destinos in matriz_caminhos.items():
        for destino, custo in destinos.items():
            print(f"Custo de {origem} para {destino}: {custo}")

    # Calcular estatísticas
    estatisticas = calcular_estatisticas(grafo)

    # Calcular métricas adicionais
    estatisticas["Intermediação"] = calcular_intermediacao(grafo, matriz_caminhos)
    estatisticas["Caminho médio"] = calcular_caminho_medio(matriz_caminhos)
    estatisticas["Diâmetro"] = calcular_diametro(matriz_caminhos)

    # Exibir estatísticas
    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()
