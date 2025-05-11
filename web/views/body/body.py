import reflex as rx

def body() -> rx.Component:
   return rx.box(
    rx.text("Soy un Técnico en Ciberseguridad. Este será un proyecto que usaré para presentarme y mostrar herramientas que desarrollaré para mejorar mis habilidades de programación con Python. Todas estas herramientas estarán enfocadas en la seguridad de la información."),
    rx.text("Este es mi primer proyecto usando Reflex, una herramienta con la que podremos crear páginas web usando solo Python!"),
    spacing="2",
    margin_x="8em"
   )