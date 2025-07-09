import flet as ft

import Lab06.model.model as md
import Lab06.UI.view as v
import Lab06.UI.controller as c

def main(page: ft.Page):
    model = md.Model()
    view = v.View(page)
    controller = c.Controller(view, model)
    view.setController(controller)
    view.loadInterface()

ft.app(target = main)