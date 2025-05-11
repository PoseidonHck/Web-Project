import reflex as rx

def button_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="linkedin"
                ),
                rx.text(text)
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )