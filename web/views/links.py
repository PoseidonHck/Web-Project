import reflex as rx
import web.components.styles.styles as styles
from web.components.button_link import button_link_linkedin, button_link_github
from web.components.tittle import tittle
from web.views.presentation_pic import presentation_pic 


def links() -> rx.Component:
    return rx.box(
        rx.vstack(
        presentation_pic(),
        tittle("Links personales"),
        button_link_linkedin("LinkedIn", 
                             "Mi experiencia laboal",
                             "https://linkedin.com/in/luis-lamus",
                            ),

        button_link_github("GitHub", 
                           "Mis proyectos y aprendizaje!", 
                           "https://github.com/PoseidonHck"
                           ),
        width="100%",
        aling_items="center",
        justify="center"
        ),
    )