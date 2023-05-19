"""Tests to the NetworkCalculator module."""
import pytest

from app.calc import NetworkCalculator


# Happy path
def test_networkcalculator_net_v4_happy() -> None:
    """Test NetworkCalculator class for IPv4 network."""
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.255.255", version=4).network() == "10.10.10.10"
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.255.0", version=4).network() == "10.10.10.0"
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.0.0", version=4).network() == "10.10.0.0"
    assert NetworkCalculator(address="10.10.10.10", mask="255.0.0.0", version=4).network() == "10.0.0.0"
    assert NetworkCalculator(address="10.10.10.10", mask="0.0.0.0", version=4).network() == "0.0.0.0"


def test_networkcalculator_net_v6_happy() -> None:
    """Test NetworkCalculator class for IPv6 network."""
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF", version=6
        ).network()
        == "1:2:3:4:5:6:7:8"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000", version=6
        ).network()
        == "1:2:3:4:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF:FFFF:0000:0000:0000:0000:0000", version=6
        ).network()
        == "1:2:3:0:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF:0000:0000:0000:0000:0000:0000", version=6
        ).network()
        == "1:2:0:0:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="FFFF:0000:0000:0000:0000:0000:0000:0000", version=6
        ).network()
        == "1:0:0:0:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="0000:0000:0000:0000:0000:0000:0000:0000", version=6
        ).network()
        == "0:0:0:0:0:0:0:0"
    )


def test_networkcalculator_broadcast_v4_happy() -> None:
    """Test NetworkCalculator class for IPv4 broadcast."""
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.255.255", version=4).broadcast() == "10.10.10.10"
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.255.0", version=4).broadcast() == "10.10.10.255"
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.0.0", version=4).broadcast() == "10.10.255.255"
    assert NetworkCalculator(address="10.10.10.10", mask="255.0.0.0", version=4).broadcast() == "10.255.255.255"
    assert NetworkCalculator(address="10.10.10.10", mask="0.0.0.0", version=4).broadcast() == "255.255.255.255"


def test_networkcalculator_broadcast_v6_happy() -> None:
    """Test NetworkCalculator class for IPv6 broadcast."""
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).broadcast()
        == "1:2:3:4:5:6:7:8"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000", version=6
        ).broadcast()
        == "1:2:3:4:ffff:ffff:ffff:ffff"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:0000:0000:0000:0000:0000", version=6
        ).broadcast()
        == "1:2:3:ffff:ffff:ffff:ffff:ffff"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="ffff:ffff:0000:0000:0000:0000:0000:0000", version=6
        ).broadcast()
        == "1:2:ffff:ffff:ffff:ffff:ffff:ffff"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="ffff:0000:0000:0000:0000:0000:0000:0000", version=6
        ).broadcast()
        == "1:ffff:ffff:ffff:ffff:ffff:ffff:ffff"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:8", mask="0000:0000:0000:0000:0000:0000:0000:0000", version=6
        ).broadcast()
        == "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"
    )


def test_networkcalculator_hosts_v4_happy() -> None:
    """Test NetworkCalculator class for IPv4 hosts."""
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.255.255", version=4).hosts() == 0
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.255.0", version=4).hosts() == 254
    assert NetworkCalculator(address="10.10.10.10", mask="255.255.0.0", version=4).hosts() == 65534
    assert NetworkCalculator(address="10.10.10.10", mask="255.0.0.0", version=4).hosts() == 16777214
    assert NetworkCalculator(address="10.10.10.10", mask="0.0.0.0", version=4).hosts() == 4294967294


def test_networkcalculator_hosts_v6_happy() -> None:
    """Test NetworkCalculator class for IPv6 hosts."""
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6).hosts()
        == 0
    )
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000", version=6).hosts()
        == 18446744073709551614
    )
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:0000:0000:0000:0000:0000", version=6).hosts()
        == 1208925819614629174706174
    )
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:0000:0000:0000:0000:0000:0000", version=6).hosts()
        == 79228162514264337593543950334
    )
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="ffff:0000:0000:0000:0000:0000:0000:0000", version=6).hosts()
        == 5192296858534827628530496329220094
    )
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="0000:0000:0000:0000:0000:0000:0000:0000", version=6).hosts()
        == 340282366920938463463374607431768211454
    )


def test_networkcalculator_next_v4_happy() -> None:
    """Test NetworkCalculator class for IPv4 next."""
    assert NetworkCalculator(address="1.2.3.4", mask="255.255.255.255", version=4).next() == "1.2.3.5"
    assert NetworkCalculator(address="1.2.3.255", mask="255.255.255.255", version=4).next() == "1.2.4.0"
    assert NetworkCalculator(address="1.2.255.255", mask="255.255.255", version=4).next() == "1.3.0.0"
    assert NetworkCalculator(address="1.255.255.255", mask="255.255.255.255", version=4).next() == "2.0.0.0"
    assert NetworkCalculator(address="254.255.255.255", mask="255.255.255.255", version=4).next() == "255.0.0.0"
    # Last address
    with pytest.raises(ValueError):
        assert NetworkCalculator(address="255.255.255.255", mask="255.255.255.255", version=4).next()


def test_networkcalculator_next_v6_happy() -> None:
    """Test NetworkCalculator class for IPv6 next."""
    assert (
        NetworkCalculator(address="1:2:3:4:5:6:7:8", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6).next()
        == "1:2:3:4:5:6:7:9"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:7:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "1:2:3:4:5:6:8:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:6:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "1:2:3:4:5:7:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:5:ffff:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "1:2:3:4:6:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:4:ffff:ffff:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "1:2:3:5:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:3:ffff:ffff:ffff:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "1:2:4:0:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:2:ffff:ffff:ffff:ffff:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "1:3:0:0:0:0:0:0"
    )
    assert (
        NetworkCalculator(
            address="1:ffff:ffff:ffff:ffff:ffff:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
        == "2:0:0:0:0:0:0:0"
    )
    with pytest.raises(ValueError):
        assert NetworkCalculator(
            address="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", mask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", version=6
        ).next()
