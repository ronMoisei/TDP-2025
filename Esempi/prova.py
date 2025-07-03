import flet as ft

def main(page: ft.Page):
    # 1) Controllo Text che funge da contatore, inizializzato a "0"
    counter = ft.Text(value="0", size=72)

    # 2) Handler per il pulsante "+1"
    def increment(e: ft.ControlEvent):
        # leggo il valore corrente, lo converto in intero
        current = int(counter.value)
        # incremento solo se < 999
        if current < 999:
            counter.value = str(current + 1)
            # aggiorno solo il controllo counter
            counter.update()

    # 3) Handler per il pulsante "reset"
    def reset(e: ft.ControlEvent):
        counter.value = "0"
        counter.update()

    # 4) Pulsanti con i relativi handler
    plus_btn = ft.ElevatedButton(text="+1", on_click=increment)
    reset_btn = ft.ElevatedButton(text="reset", on_click=reset)

    # 5) Layout: contatore grande sopra, i due pulsanti sotto affiancati
    page.add(
        counter,
        ft.Row(controls=[plus_btn, reset_btn], spacing=20)
    )

ft.app(target=main)
