"""Tests to the version module."""

from app.cmd import inspiration


def test_inspiration() -> None:
    """Test inspiration."""
    assert inspiration() == "Work hard beat talent when talent doesn't work hard"
