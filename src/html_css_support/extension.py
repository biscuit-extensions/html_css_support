from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


import re

class HTMLCSSSupport(Extension):
    """CSS class and ID completion for HTML, JSX, and template files."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.classes: set[str] = set()
        self.ids: set[str] = set()
        self.api.logger.info("HTML CSS Support extension initialised.")

    def parse_css(self, css_content: str) -> None:
        class_matches = re.findall(r"\.([a-zA-Z0-9_\-]+)", css_content)
        id_matches = re.findall(r"#([a-zA-Z0-9_\-]+)", css_content)
        self.classes.update(class_matches)
        self.ids.update(id_matches)

    def suggest_classes(self, prefix: str = "") -> list[str]:
        return sorted([c for c in self.classes if c.startswith(prefix)])

    def install(self) -> None:
        self.api.logger.info("HTML CSS Support extension installed.")
