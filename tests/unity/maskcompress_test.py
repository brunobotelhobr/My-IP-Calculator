"""Tests to the MaskCompress module."""
import pytest

from app.calc import MaskCompress


def test_maskcompress_v4() -> None:
    """Test MaskCompress class for IPv4."""
    assert MaskCompress("255.255.255.255", 4).compress() == 32
    assert MaskCompress("255.255.255.0", 4).compress() == 24
    assert MaskCompress("255.255.0.0", 4).compress() == 16
    assert MaskCompress("255.0.0.0", 4).compress() == 8
    assert MaskCompress("0.0.0.0", 4).compress() == 0
    with pytest.raises(ValueError):
        MaskCompress("0.0.0.0", 5).compress()
    with pytest.raises(ValueError):
        MaskCompress("300.0.0.0", 4).compress()
    with pytest.raises(ValueError):
        MaskCompress("-1.0.0.0", 4).compress()
    with pytest.raises(ValueError):
        MaskCompress("A", 4).compress()


def test_maskcompress_v6() -> None:
    """Test MaskCompress class for IPv6."""
    assert MaskCompress("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", 6).compress() == 128
    assert MaskCompress("ffff:ffff:ffff:ffff::", 6).compress() == 64
    assert MaskCompress("ffff:ffff:ffff::", 6).compress() == 48
    assert MaskCompress("ffff:ffff::", 6).compress() == 32
    assert MaskCompress("ffff::", 6).compress() == 16
    assert MaskCompress("::", 6).compress() == 0
    with pytest.raises(ValueError):
        MaskCompress("::", 7).compress()
    with pytest.raises(ValueError):
        MaskCompress("FFffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", 6).compress()
    with pytest.raises(ValueError):
        MaskCompress("-1:ffff:ffff:ffff:ffff:ffff:ffff:ffff", 6).compress()
    with pytest.raises(ValueError):
        MaskCompress("A", 6).compress()
