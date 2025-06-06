import reflex as rx
import web.components.styles.styles as styles
from web.components.button_link import button_link_linkedin, button_link_github
from web.components.tittle import tittle

def herramienta(icon: str, witdh: str, text: str) -> rx.Component:
    return rx.hstack(
        rx.icon(
            tag=icon, 
            width=witdh,
            color=styles.Color.CONTENT.value,
        ),
        rx.text(text)
    )

def tools() -> rx.Component:
    return rx.box(
            tittle("Dominio de herramietas:"),
            rx.vstack(
                herramienta(
                    icon="terminal",
                    witdh=styles.Size.BIG.value,
                    text="Terminal y consola de comandos"
                    ),
                herramienta(
                    icon="code",
                    witdh=styles.Size.BIG.value,
                    text="Python y programación en general"
                ),
                herramienta(
                    icon="git-branch",
                    witdh=styles.Size.BIG.value,
                    text="Git y GitHub"
                ),
                herramienta(
                    icon="container",
                    witdh=styles.Size.BIG.value,
                    text="Docker y contenedores"
                ),
                herramienta(
                    icon="network",
                    witdh=styles.Size.BIG.value,
                    text="Redes y protocolos de comunicación"
                ),
                herramienta(
                    icon="shield",
                    witdh=styles.Size.BIG.value,
                    text="SIEMs, WAFs y herramientas de seguridad"
                ),
            margin_top=styles.Size.MEDIUM.value
                )
            )