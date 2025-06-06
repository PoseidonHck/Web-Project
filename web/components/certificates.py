import reflex as rx
import web.components.styles.styles as styles
from web.components.button_link import button_link_cc_ics2
from web.components.tittle import tittle

def certificates() -> rx.Component:
        return rx.vstack(
                tittle("Certificados"),
                button_link_cc_ics2(
                    "CC - ISC2",
                    "https://www.credly.com/badges/2ab40fdf-97ce-4b3e-b362-44467449fbf5/public_url"
                ),
                width="100%",
                align_items="center",
                padding=styles.Size.TINY.value,
        )

