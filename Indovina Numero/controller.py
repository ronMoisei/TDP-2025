from math import log2

from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def reset(self, e):
        self._model.reset()
        self._view._txtOutT.value = self._model.T
        self._view._lv.controls.clear()
        self._view._btnPlay.disabled = False
        self._view._txtIn.disabled = False
        self._view._lv.controls.append(
            ft.Text("Indovina a quale numero sto pensando!"))

        self._view._pb.value = self._model.T / self._model.TMax
        self._view._txtOutNMax.value = self._model.NMax

        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txtIn.value
        self._view._txtIn.value = ""

        if tentativoStr == "":
            self._view._lv.controls.append(
                ft.Text("Attenzione! inserisci un valore numerico da testare.",
                        color="red"))
            self._view.update()
            return

        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lv.controls.append(
                ft.Text("Attenzione, valore inserito non è un intero.",
                        color="red")
            )
            self._view.update()
            return

        if tentativoInt < 0 or tentativoInt > self._model.NMax:
            self._view._lv.controls.append(
                ft.Text("Attenzione, valore inserito non è compreso tra 0 e "
                        f"{self._model.NMax}.",
                        color="red")
            )
            self._view.update()
            return

        self._view._txtOutT.value = self._model.T - 1
        self._view._pb.value = (self._model.T - 1) / self._model.TMax

        res = self._model.play(tentativoInt)

        if res == 0: #ho vinto
            self._view._lv.controls.append(
                ft.Text(f"Fantastico! hai vinto, il "
                        f"segreto era {tentativoInt}",
                        color="green"))
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == 2: # ho finito tutte le vite
            self._view._lv.controls.append(
                ft.Text(f"Mi dispiace, hai finito le vite. "
                        f"Il segreto era: {self._model.segreto}")
            )
            self._view._btnPlay.disabled = True
            self._view._txtIn.disabled = True
            self._view.update()
            return
        elif res == -1: # il mio segreto è più piccolo
            self._view._lv.controls.append(
                ft.Text(f"Il segreto è più piccolo di {tentativoInt}.")
            )
            self._view.update()
        else: #il segreto è più grande
            self._view._lv.controls.append(ft.Text(
                f"Il segreto è più grande di {tentativoInt}"
            ))
            self._view.update()

    def getNMax(self):
        return self._model.NMax

    def getTMax(self):
        return self._model.TMax

    def setDifficulty(self, e):
        self._model.NMax = int(self._view._sl.value)
        self._model.TMax = int(log2(self._model.NMax))
        self._view._txtOutNMax.value = self._model.NMax
        self._view.update()
        print(self._model.NMax, "Nmax")