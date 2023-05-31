"""Main module for the app package, it contains the cmd utility."""
from math import log2
from typing import Annotated, List, Optional

import typer

from app.calc import (
    Conversor,
    MaskCompress,
    MaskDecompress,
    MaskGenerator,
    Network,
    NetworkCalculator,
    OutputOptions,
    Printer,
    Validator,
    discover_format,
    discover_version,
)

cmd = typer.Typer(no_args_is_help=True)


@cmd.command()
def version() -> str:
    """Show version."""
    app_version: str = "1.0.0"
    typer.echo(app_version)
    return app_version


@cmd.command()
def val(
    address: Annotated[str, typer.Argument(..., help="IP address, it supports IPv4 and IPv6")],
    output: Annotated[
        Optional[OutputOptions],
        typer.Option(
            "-o",
            "--output",
            help="Output format for the network address details of an IP address, it supports bin, hex, dec.",
            case_sensitive=False,
            show_choices=True,
        ),
    ] = None,
) -> bool:
    """Validate an IPv4 ou IPv6 address, output the address in the desired format."""
    # Identify the address type
    address_version: int = discover_version(address=address)
    # Return False if the address is invalid
    if address_version not in [4, 6]:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Set default output format
    if output is None:
        output = discover_format(version=address_version)  # type: ignore
    # Exapand the address if it is IPv6
    if address_version == 6:
        try:
            address = Validator(address=address, version=address_version).expand_v6()
        except ValueError:
            Printer().error(name="address", value=address, message="Invalid address")
            return False
    # Validate the Address
    if Validator(address=address, version=address_version).validate() is False:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    in_format: str = "hex"
    if address_version == 4:
        in_format = "dec"
    # Convert the address to the output format
    address = Conversor(
        address=address, version=address_version, in_format=in_format, out_format=output  # type: ignore
    ).convert()
    # Print the address
    Printer().address(address=address, version=address_version)
    return True


@cmd.command()
def net(
    address: Annotated[str, typer.Argument(..., help="IP address, it supports IPv4 and IPv6.")],
    output: Annotated[
        Optional[OutputOptions],
        typer.Option(
            "-o",
            "--output",
            help="Output format for the network address details of an IP address, it supports bin, hex, dec.",
            case_sensitive=False,
            show_choices=True,
        ),
    ] = None,
    mask: Annotated[
        Optional[str], typer.Argument(help="IP address mask, if not provided an auto generated one will be assigned.")
    ] = None,
) -> bool:
    """Calculate the network address from an IP address and a subnet mask, output the address in the desired format."""
    # Identify the address type
    address_version: int = discover_version(address=address)
    # Return False if the address is invalid
    if address_version not in [4, 6]:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Set default output format
    if output is None:
        output = discover_format(version=address_version)  # type: ignore
    # Exapand the address if it is IPv6
    if address_version == 6:
        try:
            address = Validator(address=address, version=address_version).expand_v6()
        except ValueError:
            Printer().error(name="address", value=address, message="Invalid address")
            return False
    # Validate the Address
    if Validator(address=address, version=address_version).validate() is False:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Validate the Mask
    # If the mask is not provided, generate it
    if mask is None:
        mask = MaskGenerator(address=address, version=address_version).generate()
    # Expand the mask if it is in int format
    if ":" not in mask and "." not in mask:
        try:
            mask = MaskDecompress(mask=mask, version=address_version).decompress()
        except ValueError:
            # If the mask is not an int, it is invalid
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
    # If v6, expand the mask
    if address_version == 6:
        try:
            mask = Validator(address=mask, version=address_version).expand_v6()
        except ValueError:
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
    # Validate the mask
    if Validator(address=mask, version=address_version).validate() is False:
        Printer().error(name="mask", value=mask, message="Invalid mask")
        return False
    # Do the calculation
    in_format: str = "dec"
    if address_version == 6:
        in_format = "hex"
    working_net = NetworkCalculator(address=address, mask=mask, version=address_version)
    broadcast: str = working_net.broadcast()
    network: str = working_net.network()
    hosts: int = working_net.hosts()
    # Convert the address to the output format
    address = Conversor(
        address=address, version=address_version, in_format=in_format, out_format=output  # type: ignore
    ).convert()
    mask = Conversor(
        address=mask, version=address_version, in_format=in_format, out_format=output  # type: ignore
    ).convert()
    broadcast = Conversor(
        address=broadcast, version=address_version, in_format=in_format, out_format=output  # type: ignore
    ).convert()
    network = Conversor(
        address=network, version=address_version, in_format=in_format, out_format=output  # type: ignore
    ).convert()  # type: ignore
    # Print the address
    Printer().network(
        version=address_version, address=address, mask=mask, broadcast=broadcast, network=network, hosts=str(hosts)
    )
    return True


@cmd.command()
def subnet(  # type: ignore
    address: Annotated[str, typer.Argument(..., help="IP address, it supports IPv4 and IPv6.")],
    mask: Annotated[str, typer.Argument(help="IP address mask.")],
    parts: Annotated[int, typer.Argument(help="Split the netork into this parts.")],
    output: Annotated[
        Optional[str],
        typer.Option(
            "-o",
            "--output",
            help="Output format for the network address details of an IP address, it supports bin, hex, dec.",
            case_sensitive=False,
            show_choices=True,
        ),
    ] = None,
) -> bool:
    """Split an IP address into network and host parts, output the address in the desired format."""
    # Identify the address type
    address_version: int = discover_version(address=address)
    # Return False if the address is invalid
    if address_version not in [4, 6]:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Set default output format
    if output is None:
        output = discover_format(version=address_version)  # type: ignore
    # Exapand the address if it is IPv6
    if address_version == 6:
        try:
            address = Validator(address=address, version=address_version).expand_v6()
        except ValueError:
            Printer().error(name="address", value=address, message="Invalid address")
            return False
    # Validate the Address
    if Validator(address=address, version=address_version).validate() is False:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Validate the Mask
    # Expand the mask if it is in int format
    if ":" not in mask and "." not in mask:
        try:
            mask = MaskDecompress(mask=mask, version=address_version).decompress()
        except ValueError:
            # If the mask is not an int, it is invalid
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
    # If v6, expand the mask
    if address_version == 6:
        try:
            mask = Validator(address=mask, version=address_version).expand_v6()
        except ValueError:
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
    # Validate the mask
    if Validator(address=mask, version=address_version).validate() is False:
        Printer().error(name="mask", value=mask, message="Invalid mask")
        return False
    # Validate the split
    # Validate if the parts are base 2
    if parts < 0:
        Printer().error(name="parts", value=str(parts), message="The parts must be greater than 1")
        return False
    if not log2(parts).is_integer():
        Printer().error(name="parts", value=str(parts), message="The parts must be base 2")
        return False
    mask = str(MaskCompress(mask=mask, version=address_version).compress())
    if address_version == 4:
        if int(mask) + parts > 32:
            Printer().error(name="parts", value=str(parts), message="The parts are too big for the mask")
            return False
    if address_version == 6:
        if int(mask) + parts > 128:
            Printer().error(name="parts", value=str(parts), message="The parts are too big for the mask")
            return False
    # Do the calculation
    in_format: str = "dec"
    if address_version == 6:
        in_format = "hex"
    submask: str = MaskDecompress(mask=str(int(mask) + parts), version=address_version).decompress()
    nets: List[Network] = []
    for _ in range(0, parts):
        working_net = NetworkCalculator(address=address, mask=submask, version=address_version)
        broadcast: str = working_net.broadcast()
        network: str = working_net.network()
        hosts: int = working_net.hosts()
        nets.append(
            Network(version=address_version, mask=submask, broadcast=broadcast, network=network, hosts=str(hosts))
        )
        address = NetworkCalculator(address=broadcast, mask=mask, version=address_version).next()
    # Convert the address to the output format
    for item in nets:
        item.network = Conversor(
            address=item.network, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
        item.broadcast = Conversor(
            address=item.broadcast, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
        item.mask = Conversor(
            address=item.mask, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
    Printer().networks(nets=nets)
    return True


if __name__ == "__main__":
    cmd()  # pragma: no cover
