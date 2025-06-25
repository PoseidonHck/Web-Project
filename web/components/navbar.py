import reflex as rx
import web.components.styles.styles as styles
from web.components.styles.styles import Size as Size
from web.rutas import Route as ruta

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text("Luis Lamus", style=styles.navbar_title_style),
                href=ruta.HOME.value,
                is_external=False,
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.text("Apps", style=styles.navbar_title_style),
                    rx.icon("chevron-down"),
                    width="10%",
                    height="50%",
                    background_color="transparent",
                    _hover = {
                        "background_color": "transparent",
                        "color": styles.Text_color.BODY.value,
                    },
                ),
            ),
            rx.menu.content(
                rx.menu.item(
                    rx.link(
                        rx.text("URL Check"),
                        href=ruta.LINK_CHECK.value,
                        is_external=False,
                    )
                ),
            ),
        ),
        position="sticky",
        bg = "linear-gradient(to bottom, #0A0B10, #1A1B29)",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.TINY.value,
        z_index="999",
    )