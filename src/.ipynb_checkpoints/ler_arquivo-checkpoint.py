import sys
from grafo import Grafo

def ler_arquivo_ins_stdin():
    grafo = Grafo()
    linhas = sys.stdin.readlines()  # Lê todas as linhas da entrada padrão

    # Processar as seções do arquivo
    for i, linha in enumerate(linhas):
        linha = linha.strip()
        if linha.startswith("ReN."):
            # Nós requeridos
            for j in range(i + 1, len(linhas)):
                if linhas[j].strip() == "":
                    break
                partes = linhas[j].split()
                grafo.adicionar_no_requerido(partes[0])  # Trabalhar com o identificador como string
                grafo.adicionar_no(partes[0])  # Adicionar o nó ao grafo principal

        elif linha.startswith("ReE."):
            # Arestas requeridas
            for j in range(i + 1, len(linhas)):
                if linhas[j].strip() == "":
                    break
                partes = linhas[j].split()
                grafo.adicionar_aresta_requerida(partes[1], partes[2], int(partes[3]))
                grafo.adicionar_aresta(partes[1], partes[2], int(partes[3]))  # Adicionar ao grafo principal

        elif linha.startswith("ReA."):
            # Arcos requeridos
            for j in range(i + 1, len(linhas)):
                if linhas[j].strip() == "":
                    break
                partes = linhas[j].split()
                grafo.adicionar_arco_requerido(partes[1], partes[2], int(partes[3]))
                grafo.adicionar_arco(partes[1], partes[2], int(partes[3]))  # Adicionar ao grafo principal

    return grafo