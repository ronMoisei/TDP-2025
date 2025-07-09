import flet as ft

from Lab05.UI.controller import Controller


class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab06 - Analizza Vendite"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.__controller = None

    def setController(self, controller: Controller):
        self.__controller = controller

    def loadInterface(self):
        # Titolo centrale
        title = ft.Text(
            "Analizza Vendite",
            size=32,
            color="blue",
            text_align=ft.TextAlign.CENTER,
        )
        # 1) Switch tema
        self.__theme_switch = ft.Switch(
            label="Light theme",
            value=False,
            on_change=self.theme_changed)
        # Dropdown anno
        self.ddAnno = ft.Dropdown(
            label="anno",
            width=120,
            options=[ft.dropdown.Option(str(y), data=y) for y in range(2015, 2025)],
            on_change=lambda e: self.__controller.on_year_changed(e.control.value)
        )

        # Dropdown brand
        self.ddBrand = ft.Dropdown(
            label="brand",
            width=200,
            options=[
                ft.dropdown.Option("AutoArt"),
                ft.dropdown.Option("TrailChef"),
                ft.dropdown.Option("Acme"),
            ],
            on_change=lambda e: self.__controller.on_brand_changed(e.control.value)
        )

        # Dropdown retailer
        self.ddRetailer = ft.Dropdown(
            label="retailer",
            width=200,
            options=[
                ft.dropdown.Option("Online"),
                ft.dropdown.Option("Retail"),
                ft.dropdown.Option("Italy"),
            ],
            on_change=lambda e: self.__controller.on_retailer_changed(e.control.value)
        )

        # Pulsanti
        btn_top = ft.ElevatedButton(
            text="Top vendite",
            on_click=lambda e: self.__controller.show_top_sales()
        )
        btn_analizza = ft.ElevatedButton(
            text="Analizza vendite",
            on_click=lambda e: self.__controller.analyze_sales()
        )

        # Layout dropdowns
        row_filters = ft.Row(
            controls=[self.ddAnno, self.ddBrand, self.ddRetailer],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        # Layout bottoni
        row_buttons = ft.Row(
            controls=[btn_top, btn_analizza],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            padding=ft.padding.only(top=20),
        )

        # Contenitore principale
        self.page.add(
            ft.Column(
                controls=[
                    title,
                    self.__theme_switch,
                    row_filters,
                    row_buttons
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            )
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
