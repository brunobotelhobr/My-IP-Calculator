"""Tests to the MaskDecompress module."""
import pytest

from app.calc import MaskDecompress


def test_decompress_v4_mask() -> None:
    """Test decompress v4 method."""
    assert MaskDecompress(mask="0", version=4).decompress() == "0.0.0.0"
    assert MaskDecompress(mask="8", version=4).decompress() == "255.0.0.0"
    assert MaskDecompress(mask="16", version=4).decompress() == "255.255.0.0"
    assert MaskDecompress(mask="24", version=4).decompress() == "255.255.255.0"
    assert MaskDecompress(mask="32", version=4).decompress() == "255.255.255.255"
    assert MaskDecompress(mask="/32", version=4).decompress() == "255.255.255.255"
    with pytest.raises(ValueError):
        MaskDecompress(mask="255.255.255.0", version=7).decompress()
    with pytest.raises(ValueError):
        MaskDecompress(mask="KKKK", version=4).decompress()
    with pytest.raises(ValueError):
        MaskDecompress(mask="3000.255.255.0", version=4).decompress()
    with pytest.raises(ValueError):
        MaskDecompress(mask="-1.255.255.0", version=4).decompress()


def test_decompress_v6_mask() -> None:
    """Test decompress v6 method."""
    assert MaskDecompress(mask="0", version=6).decompress() == "0000:0000:0000:0000:0000:0000:0000:0000"
    assert MaskDecompress(mask="64", version=6).decompress() == "FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000"
    assert MaskDecompress(mask="96", version=6).decompress() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:0000:0000"
    assert MaskDecompress(mask="128", version=6).decompress() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"
    assert MaskDecompress(mask="/128", version=6).decompress() == "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"
    with pytest.raises(ValueError):
        MaskDecompress(mask="129", version=6).decompress()
    with pytest.raises(ValueError):
        MaskDecompress(mask="-1", version=6).decompress()
    with pytest.raises(ValueError):
        MaskDecompress(mask="KKKK", version=6).decompress()
