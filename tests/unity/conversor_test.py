"""Test module for Conversor class."""
import pytest

from app.calc import Conversor


def test_conversor_v4() -> None:
    """Test Conversor class for IPv4."""
    assert Conversor(address="1.2.3.4", in_format="dec", out_format="dec", version=4).convert() == "001.002.003.004"
    assert Conversor(address="11.12.13.14", in_format="dec", out_format="hex", version=4).convert() == "0B.0C.0D.0E"
    assert (
        Conversor(address="10.10.10.10", in_format="dec", out_format="bin", version=4).convert()
        == "00001010.00001010.00001010.00001010"
    )
    assert Conversor(address="0B.0C.0D.0E", in_format="hex", out_format="dec", version=4).convert() == "011.012.013.014"
    assert (
        Conversor(address="0B.0C.0D.0E", in_format="hex", out_format="bin", version=4).convert()
        == "00001011.00001100.00001101.00001110"
    )
    assert Conversor(address="0B.0C.0D.0E", in_format="hex", out_format="hex", version=4).convert() == "0B.0C.0D.0E"
    assert (
        Conversor(address="00001010.00001010.00001010.00001010", in_format="bin", out_format="bin", version=4).convert()
        == "00001010.00001010.00001010.00001010"
    )
    assert (
        Conversor(address="00001010.00001010.00001010.00001010", in_format="bin", out_format="dec", version=4).convert()
        == "010.010.010.010"
    )
    assert (
        Conversor(address="00001010.00001010.00001010.00001010", in_format="bin", out_format="hex", version=4).convert()
        == "0A.0A.0A.0A"
    )
    with pytest.raises(ValueError):
        Conversor(address="1.2.3.4", in_format="dec", out_format="dec", version=5).convert()
    with pytest.raises(ValueError):
        Conversor(address="1.2.3.4", in_format="X", out_format="dec", version=4).convert()
    with pytest.raises(ValueError):
        Conversor(address="1.2.3.4", in_format="dec", out_format="X", version=4).convert()


def test_conversor_v6() -> None:
    """Test Conversor class for IPv6."""
    assert (
        Conversor(address="1:2:3:4:5:6:7:8", in_format="hex", out_format="hex", version=6).convert()
        == "0001:0002:0003:0004:0005:0006:0007:0008"
    )
    assert (
        Conversor(address="1:2:3:4:5:6:7:8", in_format="hex", out_format="bin", version=6).convert()
        == "0000000000000001:0000000000000010:0000000000000011:0000000000000100:"
        + "0000000000000101:0000000000000110:0000000000000111:0000000000001000"
    )
    assert (
        Conversor(address="1:2:3:4:5:6:7:8", in_format="hex", out_format="dec", version=6).convert()
        == "00001:00002:00003:00004:00005:00006:00007:00008"
    )
    assert (
        Conversor(address="1:2:3:4:5:6:7:8", in_format="dec", out_format="dec", version=6).convert()
        == "00001:00002:00003:00004:00005:00006:00007:00008"
    )
    assert (
        Conversor(address="1:2:3:4:5:6:7:8", in_format="dec", out_format="bin", version=6).convert()
        == "0000000000000001:0000000000000010:0000000000000011:0000000000000100:"
        + "0000000000000101:0000000000000110:0000000000000111:0000000000001000"
    )
    assert (
        Conversor(address="1:2:3:4:5:6:7:8", in_format="dec", out_format="hex", version=6).convert()
        == "0001:0002:0003:0004:0005:0006:0007:0008"
    )
    assert (
        Conversor(address="10:10:10:10:10:10:10:10", in_format="bin", out_format="bin", version=6).convert()
        == "0000000000000010:0000000000000010:0000000000000010:0000000000000010:"
        + "0000000000000010:0000000000000010:0000000000000010:0000000000000010"
    )
    assert (
        Conversor(address="10:10:10:10:10:10:10:10", in_format="bin", out_format="dec", version=6).convert()
        == "00002:00002:00002:00002:00002:00002:00002:00002"
    )
    assert (
        Conversor(
            address="1110:1110:1110:1110:1110:1110:1110:1110", in_format="bin", out_format="hex", version=6
        ).convert()
        == "000E:000E:000E:000E:000E:000E:000E:000E"
    )
    with pytest.raises(ValueError):
        Conversor(address="1:2:3:4:5:6:7:8", in_format="hex", out_format="hex", version=7).convert()
    with pytest.raises(ValueError):
        Conversor(address="1:2:3:4:5:6:7:8", in_format="X", out_format="hex", version=6).convert()
    with pytest.raises(ValueError):
        Conversor(address="1:2:3:4:5:6:7:8", in_format="hex", out_format="X", version=6).convert()
