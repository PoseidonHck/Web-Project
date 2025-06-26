import reflex as rx
import web.components.styles.styles as styles
import web.components.styles.colors as colors
from web.components.navbar import navbar
from web.Backend.url_scanner_state import UrlScannerState

def urlScanner() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "URL Scanner", 
                    style=styles.title_body_style
                    ),
                rx.text(
                    "Ingresa la URL que deseas escanear:", 
                    aling="center"
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="https://example.com", 
                            on_change=UrlScannerState.set_url,
                            width="100%"
                        ),
                        rx.button(
                            "Scan URL", 
                            width="25%",
                            on_click=UrlScannerState.scan_url,
                        ),
                        width="100%",
                    ),
                rx.text("Los resultados del escaneo aparecerán en breve:"),
                rx.text(
                    UrlScannerState.result,
                    padding_top=styles.Size.SMALL.value,
                    ),
                padding=styles.Size.SUPREME.value,
                ),
                aling="center",
                width="100%",
            ))