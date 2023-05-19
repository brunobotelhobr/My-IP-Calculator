"""Test the main cmd object."""
import typer

from app.main import cmd


def test_cmd() -> None:
    """Test cmd object is a typer.Typer instance."""
    assert isinstance(cmd, typer.Typer)
