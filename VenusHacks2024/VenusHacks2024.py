"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from VenusHacks2024.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from VenusHacks2024.pages.tools import tools
from VenusHacks2024.pages.team import team
from VenusHacks2024.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
