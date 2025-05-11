import reflex as rx
import web.components.styles.styles as styles

def header() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.avatar(src="favicon.ico", size="8", radius="medium"), # Debemos posicionar a la Izquierda.
                rx.text("Hola! Me llamo Luis ", size="9"),
                spacing="9"
            ),
            margin_y= styles.Size.BIG.value
        )
    )
