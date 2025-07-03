from math import log2

from model import Model
import flet as ft
from view import View

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()
        self.tentativoStr = ""
    def reset(self, e):
        self._model.reset()

    def setDifficulty(self, e):
        self._model.NMax = int(self._view._sl.value)
        self._model.TMax = int(log2(self._model.NMax))
        self._view.txtIn.disabled = True
        self._model.reset()
        self._view.update()
        print(self._model.NMax, "NMax")

    def play(self, e):
        self._view.txtIn.disabled = False
        self._view._sl.disabled = True
        self._view._btn_play.disabled = True
        self._view._btnCheck.disabled = False

        self._model.NMax = int(self._view._sl.value)
        self._view.update()

    def check(self, e):
        # 1) Leggo e “pulisco” l’input
        tent = self._view.txtIn.value.strip()
        # 2) Svuoto subito il campo
        self._view.txtIn.value = ""
        self._view.update()

        # 3) Fail-fast: stringa vuota?
        if not tent:
            self._view._lv.controls.append(
                ft.Text("Attenzione! inserisci un valore non vuoto.", color="red")
            )
            self._view.update()
            return

        # 4) Rifiuto input puramente numerico
        if tent.isdigit():
            self._view._lv.controls.append(
                ft.Text("Attenzione! il codice non può essere un numero.", color="red")
            )
            self._view.update()
            return
        result = self._model.play(tent)
        if result != [0,1]:
            self._view._lv.controls.append(ft.Text(f"Il tentativo {tent} ha {result[0]} lettere corrette"))
            self._view.update()
            return
        pass

