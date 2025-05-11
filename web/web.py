import reflex as rx
from web.components.navbar import navbar
from web.views.header.header import header
from web.views.body.body import body
from web.views.links.links import links
import web.components.styles.styles as styles


class State(rx.State):
    pass


def index() -> rx.Component: ### -> Index trabajará con los componentes de reflex.
    return rx.box(
        navbar(),
        header(),
        rx.center(
            rx.vstack(
                body(),
                links(),
                margin_y=styles.Size.BIG.value,
                margin_x="60px"
            )
        )
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
