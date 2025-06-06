import reflex as rx
import web.components.styles.styles as styles
from web.components.navbar import navbar
from web.views.header.presentation_pic import presentation_pic
from web.views.body.body import body
from web.views.links.links import links
from web.components.tittle import tittle
from web.views.body.tools import tools
from web.components.certificates import certificates



class State(rx.State):
    pass


def index() -> rx.Component: ### -> Index trabajará con los componentes de reflex.
    return rx.box(
        navbar(),
        rx.desktop_only(
            ## Presentanción para Desktop
            rx.hstack(
                rx.vstack(
                    links(),
                    width="40%",
                ),
                rx.vstack(
                    rx.center(tittle("Mi nombre es Luis Lamus...")),
                    body(),
                    tools(),
                    spacing="1",
                    width="100%",
                    ),
                rx.vstack(
                    certificates(),
                    width="30%",
                    align_items="center",
                ),
                padding=styles.Size.MEDIUM.value,
                align="start",
            )
        ),
        ## Presentación para Mobile
            rx.mobile_only(
                rx.vstack(
                    links(),
                    tittle("Mi nombre es Luis Lamus..."),
                    body(),
                    tools(),
                    certificates(),
                    spacing="2",
                    padding=styles.Size.SMALL.value,
                    align_items="center",
                )   
            )
    )



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index)
