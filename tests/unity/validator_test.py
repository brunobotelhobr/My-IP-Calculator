"""Tests to the Validator module."""
import pytest

from app.calc import Validator


# Happy path
def test_validate_v4_valid_address() -> None:
    """Test validate v4 method."""
    assert Validator("192.168.0.1", 4).validate() is True


def test_validate_v6_valid_address() -> None:
    """Test validate v6 method."""
    assert Validator("2001:0db8:85a3:0000:0000:8a2e:0370:7334", 6).validate() is True
    assert Validator("2001::", 6).validate() is False
    assert Validator("::2001", 6).validate() is False
    assert Validator("::", 6).validate() is False


def test_expand_v6_valid_address() -> None:
    """Test expand v6 method."""
    assert Validator("2001:0db8:85a3::", 6).expand_v6() == "2001:0DB8:85A3:0000:0000:0000:0000:0000"
    assert Validator("2001:0db8:85a3::1", 6).expand_v6() == "2001:0DB8:85A3:0000:0000:0000:0000:0001"
    assert Validator("::1", 6).expand_v6() == "0000:0000:0000:0000:0000:0000:0000:0001"


# Unhappy path
def test_invalid_version() -> None:
    """Test for invalid ip version."""
    with pytest.raises(ValueError):
        Validator("1.2.3.4", 7).validate()


def test_validate_v4_invalid_address() -> None:
    """Test for invalid v4 address."""
    assert Validator("192.168.0.-1", 4).validate() is False
    assert Validator("192.168.0.256", 4).validate() is False
    assert Validator("1921680256", 4).validate() is False
    assert Validator("A", 4).validate() is False
    assert Validator("1000.0.0.1", 4).validate() is False
    assert Validator("-1.1.1.1", 4).validate() is False
    assert Validator("1.2.3.4.5", 4).validate() is False


def test_validate_v6_invalid_address() -> None:
    """Test for invalid v6 address."""
    assert Validator("2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234", 6).validate() is False
    assert Validator("1000000::", 6).validate() is False
    assert Validator("A:::2", 6).validate() is False
    assert Validator("A::B::2", 6).validate() is False
    with pytest.raises(ValueError):
        Validator("1:2:3:4:5:6:7:8:9:10", 6).expand_v6()
    with pytest.raises(ValueError):
        Validator("1:2:3:4:5:6:7:8:9", 6).expand_v6()
    with pytest.raises(ValueError):
        Validator("K", 6).expand_v6()
    with pytest.raises(ValueError):
        Validator("192.168.0.1", 6).expand_v6()


def test_expand_v6_invalid_address() -> None:
    """Test for invalid v6 address."""
    with pytest.raises(ValueError):
        Validator("2001:0db8:85a3::1::1", 6).expand_v6()
    with pytest.raises(ValueError):
        Validator("2001:0db8:85a3:::1", 6).expand_v6()
    with pytest.raises(ValueError):
        Validator("A", 6).expand_v6()
