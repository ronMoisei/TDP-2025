import flet as ft


import Lab04.model.model as md



class Controller:
    def __init__(self, view, model):
        self._model = md.Model()
        self._view = view
        self._dicValue = None


    def get_dictionaries(self, e):
        return self._model.languageList()

    def fillDictionary(self):

        self._view.ddDic.options.clear()
        for d in self._model.languageList():
            self._view.ddDic.options.append(
                ft.dropdown.Option(
                    key=d,
                    data=self._model.get_dictionary(d),
                )
            )

        self._view.update()  # forza il redraw

    def choice_dictionary(self, e):

        # e.control è il Dropdown, non l'Option
        selected_key = e.control.value
        # recupera l'Option corrispondente per avere il .data
        for opt in self._view.ddDic.options:
            if opt.key == selected_key:
                self._dicValue = opt.data
                break
        self._view.txtIn.disabled = False
        self._view.update()
        print(type(self._dicValue))
        print(self._dicValue._language)
        print("Hai scelto l'oggetto Dictionary:", selected_key)

    def verifica(self,e):
        self._view.lvResult.controls.clear()

        print("premuto")
        if self._dicValue is None:
            self._view.create_alert("Selezionare un dizionario")
            return
        print("Verifica caricamento")
        self._view.lvResult.controls.append(ft.Text(str(self._dicValue)))
        self._view.update()

        print("Appeso")



    def check(self, e):
        self._view.lvResult.controls.clear()
        sbagliate = []
        parole = self._view.txtIn.value
        if parole is not None:
            sbagliate = self._model.checkLanguage(parole, self._dicValue._language)
            self._view.lvResult.controls.append(ft.Text(sbagliate))
            self._view.lvResult.controls.append(ft.Text(parole))
            self._view.update()