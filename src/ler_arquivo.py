from grafo import Grafo
import sys

def ler_arquivo_ins_stdin():
    grafo = Grafo()
    linhas = sys.stdin.readlines()

    for i, linha in enumerate(linhas):
        linha = linha.strip()
        if linha.startswith("ReN."):
            for j in range(i + 1, len(linhas)):
                if linhas[j].strip() == "":
                    break
                partes = linhas[j].split()
                grafo.adicionar_no_requerido(partes[0])  
                grafo.adicionar_no(partes[0]) 

        elif linha.startswith("ReE."):
            for j in range(i + 1, len(linhas)):
                if linhas[j].strip() == "":
                    break
                partes = linhas[j].split()
                de, para, custo = partes[1], partes[2], int(partes[3])
                grafo.adicionar_aresta_requerida(de, para, custo)  
                grafo.adicionar_aresta(de, para, custo)  

        elif linha.startswith("ReA."):
            for j in range(i + 1, len(linhas)):
                if linhas[j].strip() == "":
                    break
                partes = linhas[j].split()
                de, para, custo = partes[1], partes[2], int(partes[3])
                grafo.adicionar_arco_requerido(de, para, custo)  
                grafo.adicionar_arco(de, para, custo) 

    return grafo