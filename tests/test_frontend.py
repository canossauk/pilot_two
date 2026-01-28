import inspect

import flet as ft

from frontend.utilities.styles import UniversityTheme
from src.frontend.main import main


def test_university_theme_constants():
    """Verify that the theme contains the expected colors."""
    assert UniversityTheme.primary == "#1565C0"
    assert UniversityTheme.secondary == "#FFC107"
    assert UniversityTheme.background == "#F5F5F7"
    assert isinstance(UniversityTheme.theme, ft.Theme)


def test_main_is_async():
    """Verify that the main entry point is an async function."""
    assert inspect.iscoroutinefunction(main)


def test_styles_has_required_attributes():
    """Ensure all required style attributes are present."""
    required = ["primary", "secondary", "background", "surface", "error"]
    for attr in required:
        assert hasattr(UniversityTheme, attr)
