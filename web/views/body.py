import reflex as rx
from web.components.styles import styles as styles
from web.components.styles.colors import Color, Text_color

def body() -> rx.Component:
   return rx.box(
      rx.fragment(
         rx.text("Soy un Técnico en Ciberseguridad. Este será un proyecto que usaré para presentarme y mostrar herramientas que desarrollaré para mejorar mis habilidades de programación con Python."),
         rx.text("Todas estas herramientas estarán enfocadas en la seguridad de la información. Este es mi primer proyecto usando Reflex, una herramienta con la que podremos crear páginas web usando solo Python!"),
      ),
    spacing="2",
    width="90%",
    padding=styles.Size.SMALL.value
    )