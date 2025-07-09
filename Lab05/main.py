import flet as ft

import Lab05.model.model as md
import Lab05.UI.view as v
import Lab05.UI.controller as c

def main(page: ft.Page):
    model = md.Model()
    view = v.View(page)
    controller = c.Controller(view, model)
    view.setController(controller)
    view.loadInterface()

ft.app(target = main)