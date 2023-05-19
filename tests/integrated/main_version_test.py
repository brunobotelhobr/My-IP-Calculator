"""Version test for main module."""
from app.main import version


def test_version() -> None:
    """Test version."""
    assert version() == "0.0.1"
