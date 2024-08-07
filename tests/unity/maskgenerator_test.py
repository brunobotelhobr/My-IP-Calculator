"""Tests to the MaskGenerator module."""

import pytest

from app.calc import MaskGenerator


def test_generate_v4_mask() -> None:
    """Test generate method."""
    assert MaskGenerator(address="1.2.3.4", version=4).generate() == "255.0.0.0"
    assert MaskGenerator(address="129.0.0.1", version=4).generate() == "255.255.0.0"
    assert MaskGenerator(address="192.168.1.2", version=4).generate() == "255.255.255.0"
    assert MaskGenerator(address="225.168.1.2", version=4).generate() == "255.255.255.0"
    assert MaskGenerator(address="255.168.1.2", version=4).generate() == "255.255.255.0"


def test_generate_v6_mask() -> None:
    """Test generate method."""
    assert MaskGenerator(address="1:2:3:4:5:6:7:8", version=6).generate() == "FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000"
    with pytest.raises(ValueError):
        MaskGenerator(address="1.2.3.4", version=12).generate()
    with pytest.raises(ValueError):
        MaskGenerator(address="300.1.2.3", version=4).generate()
