import networkx as nx

from MetroParis.database.DAO import DAO
from MetroParis.model.fermata import Fermata


class Model:
    """
    Fa da intermediario tra il DAO (accesso al DB) e
    il controller/view: carica e fornisce i dati in memoria.
    """
    def __init__(self):
        self._fermate = DAO.get_Fermate()
        self._grafo = nx.DiGraph()
        self._idMAPFermate = self.mapFermate(self._fermate)

    def mapFermate(self, listFermate):
        mappa = {}
        for fermata in listFermate:
            mappa[fermata.id_fermata] = fermata
        return mappa

    def buildGraphPesato(self):
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgesPesati()

    def addEdgesPesati(self):
        connessioni = DAO.get_Connessioni()
        for edge in connessioni:
            u = self._idMAPFermate[edge.id_stazP]
            v = self._idMAPFermate[edge.id_stazA]

            if self._grafo.has_edge(u, v):
                self._grafo[u][v]['weight'] += 1
            else:
                self._grafo.add_edge(u, v)

    def buildGraph(self):
        #Aggiungiamo i nodi
        self._grafo.add_nodes_from(self._fermate)
        self.addEdges()

    def addEdges(self):
        connessioni = DAO.get_Connessioni()
        for edge in connessioni:
            u = self._idMAPFermate[edge.id_stazP]
            v = self._idMAPFermate[edge.id_stazA]
            self._grafo.add_edge(u, v)

    def getBFSNodesFromTree(self, source: Fermata):
        tree = nx.bfs_tree(self._grafo, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi

    def getBFSNodesFromEdges(self, source: Fermata):
        archi = nx.bfs_edges(self._grafo, source)
        res = []
        for u,v in archi:
            res.append(u)
        return res


    @property
    def fermate(self):
        return self._fermate


    def get_NumNodi(self):
        return len(self._grafo.nodes)

    def get_NumArchi(self):
        return len(self._grafo.edges)

    def get_fermata(self, id: int):
        if id in self._idMAPFermate:
            print(f"{id}: {type(self._idMAPFermate[id])}")
            return self._idMAPFermate[id]

        else:
            return "Fermata non presente"



if __name__ == "__main__":
   m = Model()
   m.buildGraph()

   fermata = m.get_fermata(12)
   BFSTree = m.getBFSNodesFromTree(fermata)

   for f in m._idMAPFermate:
       print(f)