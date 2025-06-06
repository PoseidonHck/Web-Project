import reflex as rx
import web.components.styles.styles as styles

def tittle(text: str) -> rx.Component:
    return rx.heading(
              text, 
              style=styles.title_body_style,
    )
 