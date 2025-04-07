class Grafo:
    def __init__(self):
        self.nos = set()  # Conjunto de nós
        self.arestas = []  # Lista de arestas (de, para, custo)
        self.arcos = []  # Lista de arcos (de, para, custo)
        self.nos_requeridos = set()  # Nós requeridos
        self.arestas_requeridas = []  # Arestas requeridas
        self.arcos_requeridos = []  # Arcos requeridos

    def adicionar_no(self, no):
        self.nos.add(no)

    def adicionar_aresta(self, de, para, custo):
        self.arestas.append((de, para, custo))
        self.adicionar_no(de)
        self.adicionar_no(para)

    def adicionar_arco(self, de, para, custo):
        self.arcos.append((de, para, custo))
        self.adicionar_no(de)
        self.adicionar_no(para)

    def adicionar_no_requerido(self, no):
        self.nos_requeridos.add(no)

    def adicionar_aresta_requerida(self, de, para, custo):
        self.arestas_requeridas.append((de, para, custo))

    def adicionar_arco_requerido(self, de, para, custo):
        self.arcos_requeridos.append((de, para, custo))