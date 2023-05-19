"""Validate test for the main module."""
from app.main import validate


def test_validate():
    """Test validate."""
    assert validate(address="1.2.3.4") is True
    assert validate(address="1.2.3.4.5") is False
    assert validate(address="1.2.3") is False
    assert validate(address="1:2:3:4:5:6:7:8") is True
    assert validate(address="1:2:3") is False
    assert validate(address="1:2:3:4:5:6:7:8:9") is False
    assert validate(address="1:2:3:4:5::7") is True
    assert validate(address="1:2:3:4:5:::8") is False
    assert validate(address="1:2:3:4:5::7::9") is False
    assert validate(address="A") is False
