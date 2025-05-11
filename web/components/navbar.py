import reflex as rx



def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Luis Lamus", 
            height="100%"
        ),
        position="sticky",
        bg="navy",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )