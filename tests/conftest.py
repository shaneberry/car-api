
"""
Fixture definition for unit test cases
"""

import pytest

from car_api.app import create_app


@pytest.fixture(scope="session")
def app():
    """
    Create and configure a new app instance for each test.
    Sets app config variable ``TESTING`` to ``True``

    :return App for testing
    """
    app = create_app(testing=True)
    yield app


@pytest.fixture
def client(app):
    """
    Return a configured fake client for test purpose
    """
    with app.test_client() as test_client:
        yield test_client
