import reflex as rx
import web.components.styles.styles as styles
import web.utils as utils
from web.rutas import Route as ruta
from web.views.urlScanner import urlScanner
from web.components.navbar import navbar

@rx.page(
    route=ruta.LINK_CHECK.value,
    title=utils.url_check_tittle,
    description=utils.url_check_description,
    meta=utils.url_check_meta,
)

def url_scanner() -> rx.Component:
    return rx.box(
        navbar(),
        urlScanner()
    )