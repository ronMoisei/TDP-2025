

import flet as ft
from Lab04.UI.controller import Controller

class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # il controller verrà settato in main.py
        self.__controller = None

    def setController(self, controller: Controller):
        self.__controller = controller

    def add_content(self):
        # 1) Switch tema
        self.__theme_switch = ft.Switch(
            label="Light theme",
            value=False,
            on_change=self.theme_changed
        )
        theme_box = ft.Container(
            content=self.__theme_switch,
            padding=10,
            # il Container NON espande → resta a sinistra
        )

        # 2) Titolo
        self.__title = ft.Text(
            "TDP 2025 - Lab04: SpellChecker",
            size=24,
            weight="bold",
            color="blue",
            text_align=ft.TextAlign.CENTER,
        )
        titolo_box = ft.Container(
            content=self.__title,
            expand=True,           # espande per occupare lo spazio orizzontale rimanente
            padding=10,
        )
        self.txtIn = ft.TextField(label = "Inserire testo...",
                                  disabled=True,)
        # 3) Dropdown dizionari
        self.ddDic = ft.Dropdown(
            label="dictionaries",
            width=200,
            on_change=self.__controller.choice_dictionary,
            options=[]
        )
        self.__controller.fillDictionary()
        dic_box = ft.Container(
            content=self.ddDic,
            padding=10,
            # NON espande → resta a destra
        )
        self.btnCheck = ft.Button(text ="Verifica",
                                  on_click = self.__controller.check,
                                  )
        # 4) Metto tutto in una singola riga che si estende orizzontalmente
        header = ft.Row(
            controls=[theme_box, titolo_box, dic_box],
            alignment=ft.MainAxisAlignment.CENTER
        )
        userRow = ft.Row(
            controls=[self.txtIn, self.btnCheck],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.lvResult = ft.ListView()
        lv_box = ft.Container(
            content=self.lvResult,
            padding=50,
            expand=True,
            border=ft.border.all(2, color = "blue"),  # bordo di 2px, blu
            border_radius=5,                            # angoli arrotondati
    )
        btnVerifica = ft.Button(text="Verifica caricamento dizionario",
                                on_click=self.__controller.verifica)
        # 5) Aggiungo l’header alla pagina
        self.page.add(header,
                      userRow,
                      lv_box,
                      btnVerifica,)
        print(self.txtIn)
        self.page.update()

    def theme_changed(self, e: ft.ControlEvent):
        # inverte tema
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        # aggiorna label
        self.__theme_switch.label = (
            "Light theme"
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else "Dark theme"
        )
        self.page.update()

    def update(self):
        self.page.update()