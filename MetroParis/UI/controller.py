import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        self._view.lst_result.control.clear()
        self._view.lst_result.control.append(ft.Text("Grafo correttamente creato"))
        self._view.lst_result.control.append(ft.Text(f"contiene {self._model.get_NumNodi()} Nodi"))
        self._view.lst_result.control.append(ft.Text(f"contiene {self._model.get_NumArchi()} archi"))
        self._view.btnCalcola.disabled = False
        self._view.update_page()


    def handleCercaRaggiungibili(self, e):
        if self._fermataPartenza is None:
            self._view.lst_result.control.clear()
            self._view.lst_result.control.append(
                ft.Text("Fermata partenza non esistente", color="red")
            )
            self._view.update_page()
        nodes = self._model.getBFSNodesFromEdges(self._fermataPartenza)
        self._view.lst_result.control.clear()
        self._view.lst_result.control.append(
            ft.Text(f"Stazioni raggiungibili a partire da {self._fermataPartenza}:")
        )
        for n in nodes:
            self._view.lst_result.control.append(ft.Text(n))
        self._view.update_page()



    def loadFermate(self, dd: ft.Dropdown()):
        fermate = self._model.fermate

        if dd.label == "Stazione di Partenza":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(
                    text = f.nome,
                    data = f,
                    on_click = self.read_DD_Partenza))
        elif dd.label == "Stazione di Arrivo":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(
                    text = f.nome,
                    data = f,
                    on_click = self.read_DD_Arrivo))


    def read_DD_Partenza(self, e):
        print("Reading DD Partenza")
        print(e.control.data)
        if e.control.data is None:
            self._fermataPartenza = None
        else:
            self._fermataPartenza = e.control.data

    def read_DD_Arrivo(self, e):
        print("Reading DD Arrivo")
        if e.control.data is None:
            self._fermataArrivo = None
        else:
            self._fermataArrivo = e.control.data