"""IP Calculator."""
from enum import Enum
from typing import List, Optional

from rich.console import Console
from rich.table import Table


class OutputOptions(str, Enum):
    """Output format for network addresses."""

    BIN = "bin"  # type: ignore
    HEX = "hex"  # type: ignore
    DEC = "dec"  # type: ignore


class Network:
    """Network Representation."""

    def __init__(self, version: int, network: str, mask: str, broadcast: str, hosts: str) -> None:
        """Initialize the network."""
        self.version: int = version
        self.network: str = network
        self.mask: str = mask
        self.broadcast: str = broadcast
        self.hosts: str = hosts


class Printer(Table):
    """Print the results."""

    def address(self, version: int, address: str, console: Optional[Console] = None) -> None:
        """Print the address."""
        self.title = "Address"
        self.add_column("Item", no_wrap=True, style="cyan")
        self.add_column("Value", no_wrap=True, style="green")
        self.add_column("Status", no_wrap=True)
        self.add_row("Version", str(version), "✅ OK")
        self.add_row("Address", address, "✅ OK")
        if console is None:
            console = Console()
        console.print(self)

    def network(
        self,
        version: int,
        address: str,
        mask: str,
        network: str,
        broadcast: str,
        hosts: str,
        console: Optional[Console] = None,
    ) -> None:
        """Print a single network."""
        self.title = "Network"
        self.add_column("Item", no_wrap=True, style="cyan")
        self.add_column("Value", no_wrap=True, style="green")
        self.add_column("Status", no_wrap=True)
        self.add_row("Version", str(version), "✅ OK")
        self.add_row("Address", address, "✅ OK")
        self.add_row("Mask", mask, "✅ OK")
        self.add_row("Network", network, "✅ OK")
        self.add_row("Broadcast", broadcast, "✅ OK")
        self.add_row("Hosts (dec)", hosts, "✅ OK")
        if console is None:
            console = Console()
        console.print(self)

    def networks(self, nets: List[Network], console: Optional[Console] = None) -> None:
        """Print a network address list."""
        self.title = "Networks"
        self.add_column("Version", no_wrap=True, style="cyan")
        self.add_column("Network", no_wrap=True, style="green")
        self.add_column("Mask", no_wrap=True, style="green")
        self.add_column("Broadcast", no_wrap=True, style="green")
        self.add_column("Hosts (dec)", no_wrap=True, style="green")
        self.add_column("Status", no_wrap=True)
        for item in nets:
            self.add_row(str(item.version), item.network, item.mask, item.broadcast, item.hosts, "✅ OK")
        if console is None:
            console = Console()
        console.print(self)

    def error(self, name: str, value: str, message: str, console: Optional[Console] = None) -> None:
        """Print errors."""
        self.title = "Errors"
        self.add_column("Item", no_wrap=True, style="cyan")
        self.add_column("Value", no_wrap=True, style="red")
        self.add_column("Message", no_wrap=True, style="red")
        self.add_column("Status", no_wrap=True)
        self.add_row(name, value, message, "⛔ Invalid")
        if console is None:
            console = Console()
        console.print(self)


class Validator:
    """Validate the IP address."""

    def __init__(self, address: str, version: int) -> None:
        """Initialize the address."""
        self.address: str = address
        self.version: int = version

    def validate(self) -> bool:
        """Validate the address."""
        if self.version == 4:
            return self._validate_v4()
        if self.version == 6:
            return self._validate_v6()
        raise ValueError("Invalid version")

    def _validate_v4(self) -> bool:
        """Validate v4 address."""
        # Split the address into octets
        parts: list[str] = self.address.split(".")
        # Check if the address has 4 octets
        if len(parts) != 4:
            return False
        # Check if each octet is between 0 and 255
        try:
            for part in parts:
                if not 0 <= int(part) <= 255:
                    return False
        except ValueError:
            return False
        # Return True if all checks passed
        return True

    def _validate_v6(self) -> bool:
        """Validate v6 address."""
        # Split the address into parts
        if self.address.count("::") > 0 or self.address.count(":") < 7:
            return False
        parts: list[str] = self.address.split(":")
        # Check if the address has 8 parts
        if len(parts) != 8:
            return False
        # Check if each part is between 0 and FFFF
        try:
            for part in parts:
                if not 0 <= int(part, 16) <= int("FFFF", 16):
                    int(part, 16)
                    return False
        except ValueError:
            return False
        # Return True if all checks passed
        return True

    def expand_v6(self) -> str:
        """Expand v6 address with ::."""
        # If not expandable, return as received.
        # self.addres string container :::
        if ":::" in self.address:
            raise ValueError("Invalid IPv6 address.")
        if self.address.count("::") > 1:
            raise ValueError("Invalid IPv6 address.")
        if self.address.count(":") == 0:
            raise ValueError("Invalid IPv6 address.")
        # Split the address into parts
        parts: list[str]
        if "::" in self.address:
            begin: list[str] = self.address.split("::")[0].split(":")
            end: list[str] = self.address.split("::")[1].split(":")
            fill: list[str] = ["0"] * (8 - len(begin) - len(end))
            parts = begin + fill + end
        else:
            parts = self.address.split(":")
        # Convert each part to uppercase and zero-pad it to 4 digits
        if len(parts) != 8:
            raise ValueError("Invalid IPv6 address")
        for counter in range(8):
            parts[counter] = parts[counter].upper().zfill(4)
        # Join the parts with colons
        return ":".join(parts)


class MaskGenerator:  # type: ignore
    """Generate the mask."""

    def __init__(self, address: str, version: int) -> None:
        """Initialize the address."""
        self.address: str = address
        self.version: int = version

    def generate(self) -> str:
        """Generate the mask."""
        if self.version == 4:
            return self._get_mask_v4(self.address)
        if self.version == 6:
            return self._get_mask_v6()
        raise ValueError("Invalid version")

    def _get_mask_v4(self, address: str) -> str:
        """Get the mask of v4 address, by it's class."""
        # Define the masks
        _masks: dict[str, str] = {
            "A": "255.0.0.0",
            "B": "255.255.0.0",
            "C": "255.255.255.0",
            "D": "255.255.255.0",
            "E": "255.255.255.0",
        }
        first_octet = int(address.split(".")[0])
        if 1 <= first_octet <= 126:
            return _masks["A"]
        if 128 <= first_octet <= 191:
            return _masks["B"]
        if 192 <= first_octet <= 223:
            return _masks["C"]
        if 224 <= first_octet <= 239:
            return _masks["D"]
        if 240 <= first_octet <= 255:
            return _masks["E"]
        raise ValueError("Invalid v4 address")

    def _get_mask_v6(self) -> str:
        """Get standart mask of v6 address."""
        # Return the default mask
        return "FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000"


class MaskDecompress:
    """Decompress the mask."""

    def __init__(self, mask: str, version: int) -> None:
        """Initialize the mask."""
        self.mask: str = mask
        self.version: int = version

    def decompress(self) -> str:
        """Decompress the mask."""
        if self.version == 4:
            return self._decompress_mask_v4(self.mask)
        if self.version == 6:
            return self._decompress_mask_v6(self.mask)
        raise ValueError("Invalid version")

    def _decompress_mask_v4(self, mask: str) -> str:
        """Decompress v4 mask: 24 = 255.255.255.0."""
        # Validate the mask
        mask = mask.replace("/", "")
        for octet in mask.split("."):
            if not 0 <= int(octet) <= 32:
                raise ValueError("Invalid mask")
        # Count the number of 1s and 0s
        mask_in_binary: str = "1" * int(mask) + "0" * (32 - int(mask))
        # decompress the mask
        octets: List[str] = []
        for counter in range(0, 32, 8):
            octets.append(str(int(mask_in_binary[counter : counter + 8], 2)))
        return ".".join(octets)

    def _decompress_mask_v6(self, mask: str) -> str:
        """Decompress v6 mask, 64 = "ffff:ffff:ff..."""
        # Validate the mask
        mask = mask.replace("/", "")
        if not 0 <= int(mask) <= 128:
            raise ValueError("Invalid mask")
        # Count the number of 1s and 0s
        mask_bin: str = "1" * int(mask) + "0" * (128 - int(mask))
        octets: List[str] = []
        # Decompress the mask
        for counter in range(0, 128, 16):
            octets.append(str(hex(int(mask_bin[counter : counter + 16], 2))[2:]).upper().zfill(4))
        return ":".join(octets)


class MaskCompress:
    """Compress the mask."""

    def __init__(self, mask: str, version: int) -> None:
        """Initialize the mask."""
        self.mask: str = mask
        self.version: int = version

    def compress(self) -> int:
        """Compress the mask."""
        if self.version == 4:
            return self._compress_mask_v4(self.mask)
        if self.version == 6:
            return self._compress_mask_v6(self.mask)
        raise ValueError("Invalid version")

    def _compress_mask_v4(self, mask: str) -> int:
        """Compress IPv4 mask, 255.255.0.0 = 16."""
        mask = mask.replace("/", "")
        if Validator(mask, 4).validate() is False:
            raise ValueError("Invalid mask")
        counter: int = 0
        lmask: list[str] = mask.split(".")
        for i in range(4):
            counter += int(bin(int(lmask[i])).count("1"))
        return counter

    def _compress_mask_v6(self, mask: str) -> int:
        """Compress ipv6 mask, FFFF:FF... = 64."""
        mask = mask.replace("/", "")
        mask = Validator(mask, 6).expand_v6()
        if Validator(mask, 6).validate() is False:
            raise ValueError("Invalid mask")
        counter: int = 0
        lmask: list[str] = mask.split(":")
        for i in range(8):
            counter += int(bin(int(lmask[i], 16)).count("1"))
        return counter


class NetworkCalculator:
    """Calculate the network."""

    def __init__(self, address: str, mask: str, version: int) -> None:
        """Initialize the calculator."""
        self.address: str = address
        self.mask: str = mask
        self.version: int = version

    def network(self) -> str:
        """Return the fist address of a ip and maskm accepts IPv6 and IPv4."""
        if self.version == 4:
            lv4address: list[str] = self.address.split(".")
            lv4mask: list[str] = self.mask.split(".")
            return ".".join([str(int(lv4address[i]) & int(lv4mask[i])) for i in range(4)])
        # IPv6
        lv6address: list[str] = self.address.split(":")
        lv6mask: list[str] = self.mask.split(":")
        return ":".join([str(hex(int(lv6address[i], 16) & int(lv6mask[i], 16)))[2:] for i in range(8)])

    def broadcast(self) -> str:
        """Return the last address of a ip and mask, accepts v6 and v4."""
        if self.version == 4:
            lv4address: list[str] = self.address.split(".")
            lv4mask: list[str] = self.mask.split(".")
            return ".".join([str(int(lv4address[i]) | (255 - int(lv4mask[i]))) for i in range(4)])
        # IPv6
        lv6address: list[str] = self.address.split(":")
        lv6mask: list[str] = self.mask.split(":")
        return ":".join([str(hex(int(lv6address[i], 16) | (65535 - int(lv6mask[i], 16))))[2:] for i in range(8)])

    def hosts(self) -> int:
        """Return the number of addresses in a mask."""
        if self.version == 4:
            v4counter: int = 32 - MaskCompress(self.mask, 4).compress()
            if int(2**v4counter - 2) > 0:
                return int(2**v4counter - 2)
            return 0
        # IPv6
        v6counter: int = 128 - MaskCompress(self.mask, 6).compress()
        if int(2**v6counter - 2) > 0:
            return int(2**v6counter - 2)
        return 0

    def next(self) -> str:
        """Return the next address of a ip and mask, accepts v6 and v4."""
        if self.version == 4:
            octets_v4: list[str] = self.address.split(".")
            for counter in range(3, -1, -1):
                if int(octets_v4[counter]) < 255:
                    octets_v4[counter] = str(int(octets_v4[counter]) + 1)
                    return ".".join(octets_v4)
                octets_v4[counter] = "0"
        if self.version == 6:
            octets_v6: list[str] = self.address.split(":")
            for counter in range(7, -1, -1):
                if int(octets_v6[counter], 16) < 65535:
                    octets_v6[counter] = str(hex(int(octets_v6[counter], 16) + 1))[2:]
                    return ":".join(octets_v6)
                octets_v6[counter] = "0"
        raise ValueError("Invalid version")


class Conversor:
    """Convert an IP address to another format."""

    def __init__(self, address: str, version: int, in_format: str, out_format: str) -> None:
        """Initialize the conversor."""
        self.address: str = address
        self.in_format: str = in_format
        self.out_format: str = out_format
        self.version: int = version
        if self.in_format not in ["bin", "dec", "hex"]:
            raise ValueError("Invalid format")
        if self.out_format not in ["bin", "dec", "hex"]:
            raise ValueError("Invalid format")
        if self.version not in [4, 6]:
            raise ValueError("Invalid version")

    def convert(self) -> str:
        """Convert v4 or v6 address to another format. It supports the following formats: bin, dec, hex."""
        if self.in_format == "bin":
            return self._zfill(self._from_bin())
        if self.in_format == "dec":
            return self._zfill(self._from_dec())
        return self._zfill(self._from_hex())

    def _split(self) -> list[str]:
        """Split the address into octets."""
        if self.version == 4:
            return self.address.split(".")
        return self.address.split(":")

    def _from_bin(self) -> str:
        """Convert a binary address to another format."""
        octets: list[str] = self._split()
        if self.version == 4:
            loop = 4
        else:
            loop = 8
        if self.out_format == "dec":
            for interaction in range(loop):
                octets[interaction] = str(int(octets[interaction], 2))
        if self.out_format == "hex":
            for interaction in range(loop):
                octets[interaction] = str(hex(int(octets[interaction], 2))[2:]).upper()
        if self.out_format == "bin":
            for interaction in range(loop):
                octets[interaction] = str(bin(int(octets[interaction], 2)))[2:]
        # Join the address
        if loop == 4:
            return ".".join(octets).upper()
        return ":".join(octets).upper()

    def _from_dec(self) -> str:
        """Convert a decimal address to another format."""
        octets: list[str] = self._split()
        if self.version == 4:
            loop = 4
        else:
            loop = 8
        if self.out_format == "bin":
            for interaction in range(loop):
                octets[interaction] = str(bin(int(octets[interaction], 10)))[2:]
        if self.out_format == "hex":
            for interaction in range(loop):
                octets[interaction] = str(hex(int(octets[interaction], 10)))[2:].upper()
        if self.out_format == "dec":
            for interaction in range(loop):
                octets[interaction] = str(int(octets[interaction], 10))
        # Join the address
        if loop == 4:
            return ".".join(octets).upper()
        return ":".join(octets).upper()

    def _from_hex(self) -> str:
        """Convert a hexadecimal address to another format."""
        octets: list[str] = self._split()
        if self.version == 4:
            loop = 4
        else:
            loop = 8
        if self.out_format == "bin":
            for interaction in range(loop):
                octets[interaction] = str(bin(int(octets[interaction], 16)))[2:]
        if self.out_format == "dec":
            for interaction in range(loop):
                octets[interaction] = str(int(octets[interaction], 16))
        if self.out_format == "hex":
            for interaction in range(loop):
                octets[interaction] = octets[interaction].upper()
        # Join the address
        if loop == 4:
            return ".".join(octets).upper()
        return ":".join(octets).upper()

    def _zfill(self, address: str) -> str:
        """Fill the octets with zeros."""
        self.address = address
        octets: list[str] = self._split()
        zeros: int = 0
        if self.version == 4:
            loop = 4
            if self.out_format == "bin":
                zeros = 8
            if self.out_format == "hex":
                zeros = 2
            if self.out_format == "dec":
                zeros = 3
        else:
            loop = 8
            if self.out_format == "bin":
                zeros = 16
            if self.out_format == "hex":
                zeros = 4
            if self.out_format == "dec":
                zeros = 5
        for interaction in range(loop):
            octets[interaction] = octets[interaction].zfill(zeros)
        # Join the address
        if loop == 4:
            return ".".join(octets).upper()
        return ":".join(octets).upper()


def discover_version(address: str) -> int:
    """Discover the version of an IP address."""
    address_version = 0
    if "." in address:
        address_version = 4
    if ":" in address:
        address_version = 6
    return address_version


def discover_format(version: int) -> str:
    """Discover the format of an IP address."""
    if version == 4:
        return "dec"
    return "hex"
