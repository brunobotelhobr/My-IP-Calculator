"""Tests to the net module."""
from app.cmd import net


def test_net_happy() -> None:
    """Test net function, happy path."""
    assert net(address="10.10.10.10") is True
    assert net(address="10.10.10.10/16") is True
    assert net(address="1.2.3.4", mask="8") is True
    assert net(address="1.2.3.4", mask="16") is True
    assert net(address="1.2.3.4", mask="24") is True
    assert net(address="1.2.3.4", mask="32") is True
    assert net(address="1.2.3.4", mask="255.255.255.0") is True
    assert net(address="1.2.3.4", mask="128.0.0.0") is True
    assert net(address="1:2:3:4:5:6:7:8") is True
    assert net(address="1:2:3:4:5:6:7::") is True
    assert net(address="1:2:3:4:5:6:7:8", mask="64") is True
    assert net(address="1:2:3:4:5:6:7:8", mask="128") is True
    assert net(address="1:2:3:4:5:6:7:8", mask="1:2:3::") is True
    assert net(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff::") is True
    assert net(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is True
    assert net(address="12:A:Z::", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is False


def test_net_unhappy() -> None:
    """Test net function, unhappy path."""
    assert net(address="10.10.10") is False
    assert net(address="10.10.10.10.1") is False
    assert net(address="300.0.0.1") is False
    assert net(address="1.2.3.4", mask="33") is False
    assert net(address="1.2.3.4", mask="-1") is False
    assert net(address="1.2.3.4", mask="300.0.0.0") is False
    assert net(address="1.2.3.4", mask="A.B.C.D") is False
    assert net(address="1.2.3.4", mask="1:2:3:4:5:6:7:8") is False
    assert net(address="1.2.3.4", mask="A") is False
    assert net(address="A.B") is False
    assert net(address="1:2:3:4:5:6:7") is False
    assert net(address="1:2:3:4:5:6:7:8:9") is False
    assert net(address="1:2:3:4:5:6:7:::") is False
    assert net(address="1:2::4::6:7::") is False
    assert net(address="1:2:3:4:5:6:7:8", mask="129") is False
    assert net(address="1:2:3:4:5:6:7:8", mask="A") is False
    assert net(address="1:2:3:4:5:6:7:8", mask="1:2:3:::") is False
    assert net(address="1:2:3:4:5:6:7:8", mask="1:2::4::6:7::") is False
    assert net(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is False
    assert net(address="A", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff") is False
    assert net(address="1:2:3:4:5:6:7:8", mask="A") is False
