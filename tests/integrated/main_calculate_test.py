"""Calculate test module."""
from app.main import calculate


def test_calculate() -> None:
    """Test calculate function."""
    assert calculate(address="10.10.10.10") is True
    assert calculate(address="10.10.10") is False
    assert calculate(address="10.10.10.10.1") is False
    assert calculate(address="300.0.0.1") is False
    assert calculate(address="A.B") is False
    assert calculate(address="1:2:3:4:5:6:7:8") is True
    assert calculate(address="1:2:3:4:5:6:7") is False
    assert calculate(address="1:2:3:4:5:6:7:8:9") is False
    assert calculate(address="1:2:3:4:5:6:7::") is True
    assert calculate(address="1:2:3:4:5:6:7:::") is False
    assert calculate(address="1:2::4::6:7::") is False
    assert calculate(address="1.2.3.4", mask="8") is True
    assert calculate(address="1.2.3.4", mask="16") is True
    assert calculate(address="1.2.3.4", mask="24") is True
    assert calculate(address="1.2.3.4", mask="32") is True
    assert calculate(address="1.2.3.4", mask="33") is False
    assert calculate(address="1.2.3.4", mask="-1") is False
    assert calculate(address="1.2.3.4", mask="255.255.255.0") is True
    assert calculate(address="1.2.3.4", mask="128.0.0.0") is True
    assert calculate(address="1.2.3.4", mask="300.0.0.0") is False
    assert calculate(address="1.2.3.4", mask="A.B.C.D") is False
    assert calculate(address="1.2.3.4", mask="1:2:3:4:5:6:7:8") is False
    assert calculate(address="1.2.3.4", mask="A") is False
    assert calculate(address="1:2:3:4:5:6:7:8", mask="64") is True
    assert calculate(address="1:2:3:4:5:6:7:8", mask="128") is True
    assert calculate(address="1:2:3:4:5:6:7:8", mask="129") is False
    assert calculate(address="1:2:3:4:5:6:7:8", mask="A") is False
    assert calculate(address="1:2:3:4:5:6:7:8", mask="1:2:3::") is True
    assert calculate(address="1:2:3:4:5:6:7:8", mask="1:2:3:::") is False
    assert calculate(address="1:2:3:4:5:6:7:8", mask="1:2::4::6:7::") is False
    assert calculate(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff::") is True
    assert calculate(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is True
    assert calculate(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is False
    assert calculate(address="A", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is False
    assert calculate(address="1:2:3:4:5:6:7:8", mask="A") is False
