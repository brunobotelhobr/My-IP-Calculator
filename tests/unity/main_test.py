"""Test the main module."""
from importlib import metadata

from typer.testing import CliRunner

from app.main import app

cli = CliRunner()


def test_version():
    """Test the version function."""
    result = cli.invoke(app, ["version"])
    assert result.exit_code == 0
    assert result.stdout == (metadata.version("app") + "\n")


def test_add():
    """Test the add function."""
    result = cli.invoke(app, ["add", "1", "2"])
    assert result.exit_code == 0
    assert result.stdout == "3.0\n"


def test_subtract():
    """Test the subtract function."""
    result = cli.invoke(app, ["subtract", "1", "2"])
    assert result.exit_code == 0
    assert result.stdout == "-1.0\n"


def test_multiply():
    """Test the multiply function."""
    result = cli.invoke(app, ["multiply", "1", "2"])
    assert result.exit_code == 0
    assert result.stdout == "2.0\n"


def test_divide():
    """Test the divide function."""
    result = cli.invoke(app, ["divide", "1", "2"])
    assert result.exit_code == 0
    assert result.stdout == "0.5\n"
    result = cli.invoke(app, ["divide", "1", "0"])
    assert result.exit_code == 1


def test_power():
    """Test the power function."""
    result = cli.invoke(app, ["power", "1", "2"])
    assert result.exit_code == 0
    assert result.stdout == "1.0\n"


def test_sqrt():
    """Test the sqrt function."""
    result = cli.invoke(app, ["sqrt", "1"])
    assert result.exit_code == 0
    assert result.stdout == "1.0\n"
