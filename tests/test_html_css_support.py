from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.html_css_support import setup
from src.html_css_support.extension import HTMLCSSSupport


class TestHTMLCSSSupportExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = HTMLCSSSupport(app_instance.api)
        ext.parse_css(".btn { color: red; } .btn-primary { background: blue; } #header { font-size: 16px; }")
        sugg = ext.suggest_classes("btn")
        assert "btn" in sugg
        assert "btn-primary" in sugg
