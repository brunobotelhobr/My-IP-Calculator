"""Main module for the app package, it contains the cmd utility."""
from importlib import metadata  # type: ignore

import typer  # type: ignore

from app.calc import Calculator

app = typer.Typer(no_args_is_help=True)
calc = Calculator()


@app.command()
def version():
    """Show version."""
    app_version = metadata.version("app")
    typer.echo(app_version)
    return app_version


@app.command()
def add(a: int, b: int):
    """Add two numbers."""
    result = calc.add(a, b)
    typer.echo(result)
    return result


@app.command()
def subtract(a: int, b: int):
    """Subtract two numbers."""
    result = calc.subtract(a, b)
    typer.echo(result)
    return result


@app.command()
def multiply(a: int, b: int):
    """Multiply two numbers."""
    result = calc.multiply(a, b)
    typer.echo(result)
    return result


@app.command()
def divide(a: int, b: int):
    """Divide two numbers."""
    result = calc.divide(a, b)
    typer.echo(result)
    return result


@app.command()
def power(a: int, b: int):
    """Raise a number to a power."""
    result = calc.power(a, b)
    typer.echo(result)
    return result


@app.command()
def sqrt(a: int):
    """Calculate the square root of a number."""
    result = calc.sqrt(a)
    typer.echo(result)
    return result


if __name__ == "__main__":
    app()  # pragma: no cover
