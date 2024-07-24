"""Tests to the Printer module."""

from app.calc import Network, Printer


# Happy path
def test_address() -> None:
    """Test address method."""
    printer = Printer()
    printer.address(4, "192.168.0.1")


def test_network() -> None:
    """Test network method."""
    printer = Printer()
    printer.network(4, "192.168.0.1", "255.255.255.0", "192.168.0.0", "192.168.0.255", "254")


def test_networks() -> None:
    """Test networks method."""
    printer = Printer()
    nets: list[Network] = []
    nets.append(Network(4, "192.168.0.2", "255.255.255.0", "192.168.0.0", "254"))
    nets.append(Network(4, "192.128.0.1", "255.255.255.0", "192.168.0.0", "254"))
    printer.networks(nets)


def test_error() -> None:
    """Test error method."""
    printer = Printer()
    printer.error(message="Error message", name="Error name", value="Error value")
