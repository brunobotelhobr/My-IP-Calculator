"""Tests to the cmd module."""

import typer

from app.cmd import cmd


def test_cmd() -> None:
    """Test cmd object is a typer.Typer instance."""
    assert isinstance(cmd, typer.Typer)
