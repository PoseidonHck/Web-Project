import reflex as rx
from enum import Enum
from web.components.styles.colors import Color, Text_color
from web.components.styles.fonts import Font, FontSize

### Constants
MAX_WIDTH  = "600px"

### Sytlesheet

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=VT323:wght@300;400&display=swap",
    "https://fonts.googleapis.com/css?family=Share+Tech+Mono:wght@400&display=swap",
    "https://fonts.googleapis.com/css2?family=Doto:wght@400&display=swap",
]

### Sizes
class Size(Enum):
    TINY="0.25em"
    SMALL="0.5em"
    DEFAULT="0.8em"
    MEDIUM="1em"
    LARGE="1.5em"
    BIG="2em"
    SUPREME="3em"

# Styles

BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "variant": "soft",
        "padding": Size.SMALL.value,
        "radius": "large",
        "background_color": Color.CONTENT.value,
        "color": Text_color.BODY.value,
        "white_space": "normal", ## Truncado de los textos en los botones.
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECUNDARY.value,
            "color": Text_color.BODY.value,
            "variant": "solid",
        },
    },
    rx.link: {
        "text_decoration": "none",
        "variant": "soft",
        "_hover": {}
    },
    rx.text: {
        "color": Text_color.BODY.value,
        "font_size": Size.MEDIUM.value,
        "font_family": Font.BODY.value,
        "justify": "center",
        "align": "center",
        },
    rx.icon: {
        "color": Color.ICON.value,
    }
}

title_body_style = dict(
    width="100%",
    aling="center",
    padding=Size.DEFAULT.value,
    color=Color.PRIMARY.value,
    font_family= Font.TITLE.value,
)

button_title_style = dict(
    font_size=Size.MEDIUM.value,
    aling="center",
    color = Text_color.TITTLE.value,

)

button_body_style = dict(
    font_size=Size.DEFAULT.value,
    aling="center",
    color = Text_color.BODY.value,
)

icon_button_style = dict(
    width=Size.SUPREME.value,
    height=Size.SUPREME.value,
    margin=Size.DEFAULT.value,
    color=Color.ICON.value,
    stroke_width=1.5,
)

navbar_title_style = dict(
    font_size=Size.LARGE.value,
    color=Color.PRIMARY.value,
    font_family= Font.NAV_TITLE.value,
    padding=Size.SMALL.value,
)