import reflex as rx
from enum import Enum

### Constants
MAX_WIDTH  = "600px"

### Sizes
class Size(Enum):
    SMALL="0.5em"
    DEFAULT="0.8em"
    MEDIUM="1em"
    BIG="2em"

# Styles

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.DEFAULT.value,
        "radius": Size.MEDIUM.value
    }
}