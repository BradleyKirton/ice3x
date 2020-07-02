import pytest


def pytest_collection_modifyitems(config, items):
    """If async dependencies is not available skip async tests."""

    try:
        import treq  # noqa

        skip_async = False
    except ImportError:
        skip_async = True

    skip_slow = pytest.mark.skip(reason="need --runslow option to run")

    for item in items:
        if "requires_async" in item.keywords and skip_async is True:
            item.add_marker(skip_slow)
