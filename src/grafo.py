class Grafo:
    def __init__(self):
        self.nos = set()
        self.arestas = []
        self.arcos = []
        self.nos_requeridos = set()
        self.arestas_requeridas = []
        self.arcos_requeridos = []

    def adicionar_no(self, no):
        self.nos.add(str(no)) 

    def adicionar_aresta(self, de, para, custo):
        self.arestas.append((str(de), str(para), custo))
        self.nos.add(str(de))
        self.nos.add(str(para))

    def adicionar_arco(self, de, para, custo):
        self.arcos.append((str(de), str(para), custo))
        self.nos.add(str(de))
        self.nos.add(str(para))

    def adicionar_no_requerido(self, no):
        self.nos_requeridos.add(str(no))

    def adicionar_aresta_requerida(self, de, para, custo):
        self.arestas_requeridas.append((str(de), str(para), custo))

    def adicionar_arco_requerido(self, de, para, custo):
        self.arcos_requeridos.append((str(de), str(para), custo))