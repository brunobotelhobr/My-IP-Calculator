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
)

cmd = typer.Typer(no_args_is_help=True)


@cmd.command()
def version() -> str:
    """Show version."""
    app_version: str = "0.0.1"
    typer.echo(app_version)
    return app_version


@cmd.command()
def validate(
    address: Annotated[str, typer.Argument(..., help="IP address, it supports IPv4 and IPv6")],
    output: Annotated[
        Optional[OutputOptions],
        typer.Option(
            "-o",
            "--output",
            help="Output format for the network address details of an IP address, it supports bin, hex, dec",
            case_sensitive=False,
            show_choices=True,
        ),
    ] = None,
) -> bool:
    """Validate an IPv4 ou IPv6 address, output the address in the desired format."""
    # Identify the address type
    address_version = 0
    in_format: str = ""
    if "." in address:
        address_version = 4
        # Default input format
        in_format = "dec"
        if output is None:
            # Set default output format
            output = "dec"  # type: ignore
    if ":" in address:
        address_version = 6
        # Default input format
        in_format = "hex"
        # Expand the address
        try:
            address = Validator(address=address, version=6).expand_v6()
        except ValueError:
            # Return False if the address is invalid
            Printer().error(name="address", value=address, message="Invalid address")
            return False
        if output is None:
            # Set default output format
            output = "hex"  # type: ignore
    if address_version not in [4, 6]:
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Validate the address
    if Validator(address=address, version=address_version).validate():
        # Convert the address to the output format
        address = Conversor(
            address=address, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
        # Print the address
        Printer().address(address=address, version=address_version)
        return True
    # Return False if the address is invalid
    Printer().error(name="address", value=address, message="Invalid address v4 address")
    return False


@cmd.command()
def calculate(  # type: ignore
    address: Annotated[str, typer.Argument(..., help="IP address, it supports IPv4 and IPv6")],
    output: Annotated[
        Optional[OutputOptions],
        typer.Option(
            "-o",
            "--output",
            help="Output format for the network address details of an IP address, it supports bin, hex, dec",
            case_sensitive=False,
            show_choices=True,
        ),
    ] = None,
    mask: Annotated[Optional[str], typer.Argument(help="IP address mask")] = None,
) -> bool:
    """Calculate the network address from an IP address and a subnet mask, output the address in the desired format."""
    # Identify the address type
    address_version = 0
    in_format: str = ""
    if "." in address:
        address_version = 4
        # Default input format
        in_format = "dec"
        if output is None:
            # Set default output format
            output = "dec"  # type: ignore
    if ":" in address:
        address_version = 6
        # Default input format
        in_format = "hex"
        # Expand the address
        try:
            address = Validator(address=address, version=6).expand_v6()
        except ValueError:
            # Return False if the address is invalid
            Printer().error(name="address", value=address, message="Invalid address")
            return False
        if output is None:
            # Set default output format
            output = "hex"  # type: ignore
    if address_version not in [4, 6]:
        # Return False if the address is invalid
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
    # If the mask is in int format, convert it to a standard mask
    if ":" not in mask and "." not in mask:
        try:
            int(mask)
        except ValueError:
            # If the mask is not an int, it is invalid
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
        try:
            mask = MaskDecompress(mask=mask, version=address_version).decompress()
        except ValueError:
            # If the mask is not an int, it is invalid
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
    if address_version == 6:
        try:
            mask = Validator(address=mask, version=address_version).expand_v6()
        except ValueError:
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
    if Validator(address=mask, version=address_version).validate() is False:
        Printer().error(name="mask", value=mask, message="Invalid mask")
        return False
    # Do the calculation
    broadcast: str = NetworkCalculator(address=address, mask=mask, version=address_version).broadcast()
    network: str = NetworkCalculator(address=address, mask=mask, version=address_version).network()
    hosts: int = NetworkCalculator(address=address, mask=mask, version=address_version).hosts()
    # Convert the address to the output format
    address = Conversor(address=address, version=address_version, in_format=in_format, out_format=str(output)).convert()
    mask = Conversor(address=mask, version=address_version, in_format=in_format, out_format=str(output)).convert()
    broadcast = Conversor(
        address=broadcast, version=address_version, in_format=in_format, out_format=str(output)
    ).convert()
    network = Conversor(address=network, version=address_version, in_format=in_format, out_format=str(output)).convert()
    # Print the address
    Printer().network(
        version=address_version, address=address, mask=mask, broadcast=broadcast, network=network, hosts=str(hosts)
    )
    return True


@cmd.command()
def subnet(  # type: ignore
    address: Annotated[str, typer.Argument(..., help="IP address, it supports IPv4 and IPv6")],
    mask: Annotated[str, typer.Argument(help="IP address mask")],
    parts: Annotated[int, typer.Argument(help="Split the netork in x parts")],
    output: Annotated[
        Optional[str],
        typer.Option(
            "-o",
            "--output",
            help="Output format for the network address details of an IP address, it supports bin, hex, dec",
            case_sensitive=False,
            show_choices=True,
        ),
    ] = None,
) -> bool:
    """Split an IP address into network and host parts, output the address in the desired format."""
    # Identify the address type
    address_version = 0
    in_format: str = ""
    if "." in address:
        address_version = 4
        # Default input format
        in_format = "dec"
        if output is None:  # type: ignore
            # Set default output format
            output = "dec"
    if ":" in address:
        address_version = 6
        # Default input format
        in_format = "hex"
        # Expand the address
        address = Validator(address=address, version=6).expand_v6()
        if output is None:  # type: ignore
            # Set default output format
            output = "hex"
    if address_version == 0:
        # Return False if the address is invalid
        Printer().error(name="address", value=address, message="Invalid address")
        return False
    # Validate the Mask
    # If the mask is in int format, convert it to a standard mask
    if ":" not in mask and "." not in mask:
        try:
            int(mask)
        except ValueError:
            # If the mask is not an int, it is invalid
            Printer().error(name="mask", value=mask, message="Invalid mask")
            return False
        try:
            mask = MaskDecompress(mask=mask, version=address_version).decompress()
        except ValueError:
            # If the mask is not an int, it is invalid
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
    submask: str = MaskDecompress(mask=str(int(mask) + parts), version=address_version).decompress()
    nets: List[Network] = []
    for _ in range(0, parts):
        network: str = NetworkCalculator(address=address, mask=submask, version=address_version).network()
        hosts: int = NetworkCalculator(address=address, mask=submask, version=address_version).hosts()
        broadcast: str = NetworkCalculator(address=address, mask=submask, version=address_version).broadcast()
        nets.append(
            Network(version=address_version, mask=submask, broadcast=broadcast, network=network, hosts=str(hosts))
        )
        address = NetworkCalculator(address=broadcast, mask=mask, version=address_version).next()
    # Convert the address to the output format
    for net in nets:
        net.network = Conversor(
            address=net.network, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
        net.broadcast = Conversor(
            address=net.broadcast, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
        net.mask = Conversor(
            address=net.mask, version=address_version, in_format=in_format, out_format=str(output)
        ).convert()
    Printer().networks(nets=nets)
    return True


if __name__ == "__main__":
    cmd()  # pragma: no cover
