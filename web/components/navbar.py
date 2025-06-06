import reflex as rx
import web.components.styles.styles as styles
from web.components.styles.styles import Size as Size



def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Luis Lamus",
            style=styles.navbar_title_style,
        ),
        position="sticky",
        bg = "linear-gradient(to bottom, #0A0B10, #1A1B29)",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.TINY.value,
        z_index="999",
    )