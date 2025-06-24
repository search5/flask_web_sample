import pytest
from flask_web.main import app as application

@pytest.fixture()
def app():
    application.config.update({
        "TESTING": True,
    })

    yield application


@pytest.fixture()
def client(app):
    return app.test_client()