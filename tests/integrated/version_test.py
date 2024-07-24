"""Tests to the version module."""

from app.cmd import version


def test_version() -> None:
    """Test version."""
    assert version() == "1.0.8"
