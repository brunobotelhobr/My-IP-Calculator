"""Tests to the Network module."""

from app.calc import Network


def test_network_init_v6() -> None:
    """Test Network class, version 6."""
    network = Network(
        version=6,
        network="a:b:c:d:e:f::",
        mask="86",
        broadcast="a:b:c:d:e:f:ffff:ffff",
        hosts="6739986666787659948666753771754907668409286105635143120275902562302",
    )
    assert network.version == 6
    assert network.network == "a:b:c:d:e:f::"
    assert network.mask == "86"
    assert network.broadcast == "a:b:c:d:e:f:ffff:ffff"
    assert network.hosts == "6739986666787659948666753771754907668409286105635143120275902562302"


def test_network_init_v4() -> None:
    """Test Network class, version 4."""
    network = Network(version=4, network="1.2.3.4", mask="24", broadcast="1.2.3.255", hosts="254")
    assert network.version == 4
    assert network.network == "1.2.3.4"
    assert network.mask == "24"
    assert network.broadcast == "1.2.3.255"
    assert network.hosts == "254"
