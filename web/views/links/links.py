import reflex as rx
from web.components.button_link import button_link

def links() -> rx.Component:
    return rx.vstack(
        button_link("LinkedIn", "https://linkedin.com/in/luis-lamus"),
        button_link("GitHub", "https://github.com/PoseidonHck")
    )