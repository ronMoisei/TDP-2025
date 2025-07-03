import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._page = page
        self._page.title = "TDP 2025 - Color Code Breaker"
        # allineamento orizzontale e verticale
        self._page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self._page.vertical_alignment   = ft.MainAxisAlignment.CENTER

        self._controller = None

    def setController(self, c):
        self._controller = c

    def loadInterface(self):
        # — Titolo centrale in alto —
        self._titolo = ft.Text(
            "Benvenuti al Color Code Breaker",
            size=34,
            color="blue"
        )
        titolo_box = ft.Container(
            content=self._titolo,
            alignment=ft.alignment.center,
            padding=20
        )

        # — Slider per la difficoltà —
        # mostra il valore corrente come label
        self._sl = ft.Slider(
            label="Seleziona difficoltà: {value}",
            min=2, max=6, divisions=4, value=2,
            width=400,
            on_change=self._controller.setDifficulty
        )
        # — Pulsante PLAY grande —
        self._btn_play = ft.ElevatedButton(
            text="PLAY",
            width=200,
            height=60,
            on_click=self._controller.play
        )
        self._btnCheck = ft.ElevatedButton(
            text="CHECK",
            width=200,
            height=60,
            disabled= True,
            on_click=self._controller.check
        )
        # metto slider e play uno accanto all’altro
        controllo_row = ft.Row(
            controls=[self._sl, self._btn_play],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        )

        # — TextField “Inserisci tentativo” —
        self._txt_in = ft.TextField(
            label="Inserisci tentativo",
            width=200,
            disabled=True  # verrà abilitato premendo PLAY
        )

        # — ListView per il log delle mosse —
        self._lv = ft.ListView(
            expand=True,
            spacing=5,
            auto_scroll=True,
            padding=10,
            height=300
        )

        # — Pulsante RESET in basso a destra —
        self._btn_reset = ft.ElevatedButton(
            text="RESET",
            width=120,
            on_click=self._controller.reset
        )
        reset_box = ft.Container(
            content=self._btn_reset,
            alignment=ft.alignment.bottom_right,
            padding=ft.padding.only(right=20, bottom=10)
        )

        checkBox = ft.Row([self._txt_in, self._btnCheck], alignment=ft.MainAxisAlignment.CENTER)

        # — Aggiungo tutto nella pagina, in ordine verticale —
        self._page.add(
            titolo_box,
            controllo_row,
            checkBox,
            self._lv,
            reset_box
        )

        # unico update finale
        self._page.update()

    @property
    def txtIn(self):
        return self._txt_in

    @property
    def logView(self):
        return self._lv

    def update(self):
        self._page.update()
