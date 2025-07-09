import flet as ft
from UI import view as v
from UI import controller as c
from model import model as md

def main(page: ft.Page):

    multiDic = md.Model()
    view = v.View(page)
    controller = c.Controller(view, multiDic)
    view.setController(controller)
    view.add_content()


ft.app(target=main)