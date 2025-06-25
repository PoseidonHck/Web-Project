import reflex as rx
import web.components.styles.styles as styles
import web.components.styles.colors as colors
from web.components.navbar import navbar

def urlScanner() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("URL Scanner", style=styles.title_body_style),
            rx.text("Ingresa la URL que deseas escanear:"),
            rx.input(placeholder="https://example.com", width="100%"),
            rx.button("Scan URL", color_scheme="blue", width="100%"),
            rx.text("Los resultados del escaneo aparecerán en breve"),
        )
    )