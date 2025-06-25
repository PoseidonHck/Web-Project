import reflex as rx
import web.components.styles.styles as styles

def presentation_pic() -> rx.Component:
    return rx.center(
            rx.avatar(src="/Foto-perfil.jpg", size="9", radius="full"), # Debemos posicionar a la Izquierda.
            padding_top=styles.Size.LARGE.value,
            margin_bottom=styles.Size.MEDIUM.value,
            justify="center",
            align_items="center",
            width="100%"
        )
