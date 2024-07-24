"""Tests to the subnet module."""

from app.cmd import subnet


def test_subnet_happy() -> None:
    """Test net function, happy path."""
    assert subnet(address="10.10.10.10", mask="8", parts=2) is True
    assert subnet(address="10.10.10.10", mask="8", parts=8) is True
    assert subnet(address="1:2:3:4:5:6:7:8", mask="64", parts=2) is True
    assert subnet(address="1:2:3:4:5:6:7:8", mask="64", parts=8) is True
    assert subnet(address="1:2:3:4:5:6:7:8", mask="F::", parts=8) is True


def test_net_unhappy() -> None:
    """Test net function, unhappy path."""
    assert subnet(address="10.10.10.10", mask="8", parts=30) is False
    assert subnet(address="10.10.10.10", mask="8", parts=-1) is False
    assert subnet(address="A.B.C.D", mask="8", parts=129) is False
    assert subnet(address="1.2.3.4", mask="80000", parts=4) is False
    assert subnet(address="1.2.3.4", mask="80000", parts=1) is False
    assert subnet(address="1.2.3.4", mask="80000", parts=0) is False
    assert subnet(address="1.2.3.4", mask="16", parts=32) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="64", parts=30) is False
    assert subnet(address="1:2:3:4:5:6:7:8/12", mask="64", parts=30) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="64", parts=-1) is False
    assert subnet(address="1.2.3.4.5.6.7.8", mask="8", parts=129) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="K", parts=2) is False
    assert subnet(address="1:2:3:4:5::7::", mask="9000", parts=2) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="FFFF::FFFF::", parts=2) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="80000", parts=64) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF.0:0:0:0:0:0:99999999", parts=2) is False
    assert subnet(address="1:2:3:4:5:6:7:8", mask="96", parts=64) is False
    assert subnet(address="A", mask="64", parts=129) is False
    assert subnet(address="A", mask="F::", parts=2) is False
    assert subnet(address="A", mask="96", parts=64) is False
