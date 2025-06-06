import reflex as rx
import web.components.styles.styles as styles


def button_link_linkedin(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="linkedin",
                    style=styles.icon_button_style,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    width="100%",
                    align_items="center",
                    padding_top=styles.Size.TINY.value,
                ),
            width="100%",
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
    )

def button_link_github(title: str, body: str, url: str) -> rx.Component:
    return rx.link( 
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="github",
                    style=styles.icon_button_style,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    width="100%",
                    align_items="center",
                    padding_top=styles.Size.TINY.value,
                ),
            ),
            width="100%",
        ),
        href=url,
        is_external=True,
        width="100%",
    )

def button_link_cc_ics2(title: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="external-link",
                    ),
                rx.text(title, style=styles.button_title_style),
                    widith="100%",
                    align_items="center",
                    pading_top=styles.Size.TINY.value,
            ),
            width="100%"
        ),
        href=url,
        is_external=True,
        width="100%",
    )