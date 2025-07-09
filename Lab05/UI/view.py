import flet as ft

from Lab05.UI.controller import Controller


class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # il controller verrà settato in main.py
        self.__controller = None

    def setController(self, controller: Controller):
        self.__controller = controller

    def loadInterface(self):
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
            "TDP 2025 - Lab05: Segreteria Studenti",
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


        # 4) Metto tutto in una singola riga che si estende orizzontalmente
        header = ft.Row(
            controls=[theme_box, titolo_box],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.ddCorso = ft.Dropdown(
            label="Selezionare un corso",
            width=600,
            on_change=self.__controller.choice_corso,
            options=[],
            disabled = True
        )
        self.ddPeriodo = ft.Dropdown(
            label="Periodo",
            width=200,
            on_change = self.__controller.setPeriodo,
            options=[
                ft.dropdown.Option(key = "I", data = 1),
                ft.dropdown.Option(key = "II", data = 2),
                ft.dropdown.Option(key="Tutti i periodi", data = None)
            ]
        )


        self.btnCercaIscritti = ft.Button(
            text="Cerca Iscritti",
            on_click=self.__controller.cercaIscritti,
        )
        row1 = ft.Row(
            controls=[self.ddPeriodo, self.ddCorso, self.btnCercaIscritti],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.lvResult = ft.ListView()
        lv_box = ft.Container(
            content=self.lvResult,
            padding=50,
            expand=True,
            border=ft.border.all(2, color="blue"),  # bordo di 2px, blu
            border_radius=5,  # angoli arrotondati
        )
        # 5) Aggiungo l’header alla pagina
        self.page.add(header,
                      row1,
                      lv_box,

                      )
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