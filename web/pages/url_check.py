import reflex as rx
import web.components.styles.styles as styles
import web.utils as utils
from web.rutas import Route as ruta
from web.components.navbar import navbar
from web.views.body import body
from web.views.links import links
from web.components.tittle import tittle
from web.views.tools import tools
from web.components.certificates import certificates

@rx.page(
    route=ruta.LINK_CHECK.value,
    title=utils.url_check_tittle,
    description=utils.url_check_description,
    meta=utils.url_check_meta,
)

def url_check() -> rx.Component: ### -> Index trabajará con los componentes de reflex.
    return rx.box(
        utils.lang(),
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