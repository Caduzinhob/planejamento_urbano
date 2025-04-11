from ler_arquivo import ler_arquivo_ins_stdin
from calcular_estatisticas import calcular_estatisticas
from geracao_matriz import floydwarshall

def main():
    grafo = ler_arquivo_ins_stdin()

    matriz_caminhos = floydwarshall(grafo)

    estatisticas = calcular_estatisticas(grafo, matriz_caminhos)

    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()