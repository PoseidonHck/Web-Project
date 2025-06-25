import reflex as rx

## COMUNES

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")

_meta=[
    {"name": "og:type", "content": "website"},
    {"name": "LinkedIn", "content": "https://www.linkedin.com/in/luis-lamus/"},
]


## INDEX

index_tittle = "Luis Lamus Portfolio"
index_description = "Hola, soy Luis Lamus, Técnico de Ciberseguridad y Desarrollador Web. Aquí encontrarás mi portafolio con proyectos y habilidades en ciberseguridad, desarrollo web y más."

index_meta = [
    {"name": "og:title", "content": index_tittle},
    {"name": "og:description", "content": index_description},
]

## APP CONSULTAS URL MALICIOSAS

url_check_tittle = "Verificador de URLs Maliciosas"
url_check_description = "Verifica URLs sospechosas y descubre si son maliciosas o seguras. Utiliza nuestro servicio para protegerte de amenazas en línea.",

url_check_meta = [
    {"name": "og:title", "content": url_check_tittle},
    {"name": "og:description", "content": url_check_description},
]