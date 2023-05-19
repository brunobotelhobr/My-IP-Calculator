"""Tests to the validate module."""
from app.cmd import val


def test_val_happy() -> None:
    """Test val function, happy path."""
    assert val(address="1.2.3.4") is True
    assert val(address="1:2:3:4:5:6:7:8") is True
    assert val(address="1:2:3:4:5::7") is True
    assert val(address="1:2:3:4:5::") is True


def test_val_unhappy() -> None:
    """Test val function, sad path."""
    assert val(address="1.2.3.4.5") is False
    assert val(address="1.2.3") is False
    assert val(address="1:2:3") is False
    assert val(address="1:2:3:4:5:6:7:8:9") is False
    assert val(address="1:2:3:4:5:::8") is False
    assert val(address="1:2:3:4:5::7::9") is False
    assert val(address="A") is False
