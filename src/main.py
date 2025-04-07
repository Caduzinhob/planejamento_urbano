from ler_arquivo import ler_arquivo_ins_stdin
from calcular_estatisticas import calcular_estatisticas
from geracao_matriz import floyd_warshall

def main():
    # Ler o grafo da entrada padrão
    grafo = ler_arquivo_ins_stdin()

    # Calcular a matriz de caminhos mais curtos
    matriz_caminhos = floyd_warshall(grafo)

    # Calcular estatísticas (incluindo métricas adicionais)
    estatisticas = calcular_estatisticas(grafo, matriz_caminhos)

    # Exibir estatísticas
    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()