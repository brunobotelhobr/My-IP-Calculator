"""Tests to the OutputOptions module."""
from app.calc import OutputOptions


def test_output_options_bin() -> None:
    """Test OutputOptions.BIN."""
    assert OutputOptions.BIN == "bin"


def test_output_options_hex() -> None:
    """Test OutputOptions.HEX."""
    assert OutputOptions.HEX == "hex"


def test_output_options_dec() -> None:
    """Test OutputOptions.DEC."""
    assert OutputOptions.DEC == "dec"
