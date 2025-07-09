

import flet as ft
import Lab05.model.model as md

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = md.Model()
        self._corso = None
        self._pd = None

    def fillddCorso(self, pd):
        self._view.ddCorso.options.clear()
        if pd is not None:
            print(f"self periodo: {self._pd}")
            for d in self._model.getCorsobyPD(self._pd):
                self._view.ddCorso.options.append(
                    ft.dropdown.Option(key=f"{d.codins} - {d.nome}: {d.pd} periodo - {d.crediti} CFU",
                    data=d,)
                )
        else:
            for d in self._model.getAllCorsi():
                self._view.ddCorso.options.append(
                    ft.dropdown.Option(
                        key=f"{d.codins} - {d.nome}: {d.pd} periodo - {d.crediti} CFU",
                        data=d,
                    )
                )
        print(self._view.ddCorso.options)
        self._view.update()

    def choice_corso(self, e):

        # e.control è il Dropdown, non l'Option
        selected_key = e.control.value
        # recupera l'Option corrispondente per avere il .data
        for opt in self._view.ddCorso.options:
            if opt.key == selected_key:
                self._corso = opt.data
                break
        #self._view.txtIn.disabled = False
        self._view.update()
        print(self._corso)
        print("Hai scelto l'oggetto Dictionary:", selected_key)

    def setPeriodo(self, e):
        self._view.ddCorso.value = "Selezionare un corso"
        self._view.update()
        print(f"Dropdown corso: {self._view.ddCorso}")
        selected_key = e.control.value
        if selected_key == "I":
            self._pd = 1
        elif selected_key == "II":
            self._pd = 2
        else:
            self._pd = None
        self.fillddCorso(self._pd)
        self._view.ddCorso.disabled = False
        self._view.update()


    def cercaIscritti(self, e):
        self._view.lvResult.controls.clear()
        # codins = self._view.ddCodins.value # ho una stringa
        if self._corso is None: # ho l'oggetto
            self._view.create_alert("Selezionare un corso di interesse.")
            return
        #procediamo a stampare gli studenti
        students = self._model.getStudentByCorso(self._corso.codins)

        if len(students) == 0:
            self._view.lvResult.controls.append(
                ft.Text("Nessuno studente iscritto a questo corso."))
            self._view.update_page()
            return

        self._view.lvResult.controls.append(
            ft.Text(f"Studenti iscritti al corso {self._corso}:"))

        for s in students:
            self._view.lvResult.controls.append(ft.Text(s))
        self._view.update()