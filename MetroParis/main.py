import flet as ft

from model.model import model as md
from UI.view import View as v
from UI.controller import Controller as c

def main(page: ft.Page):
    model = md.Model()
    view = v(page)
    controller = c(view, model)
    view.setController(controller)
    view.loadInterface()

ft.app(target = main)