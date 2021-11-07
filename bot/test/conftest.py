#pylint: disable=W0614
#pylint: disable=W0621
#pylint: disable=W0621
#pylint: disable=W0401
#pylint: disable=C0413
"""
Define fixtures for testing Flask application Bot
"""
import sys
import pytest
from faker import Faker
sys.path.append('../')
if True:
    from main import init_app  # to execute from test folder
    from init_bp import *
fake = Faker()


@pytest.fixture(scope='function')
# @pytest.fixture
def app():
    """
    Launch Flask app with test config
    :return: app Flask app
    """
    app = init_app({
        'TESTING': True,
        'DB_NAME': 'test_contact',
        'SECRET_KEY': b'simple_key',
    })
    yield app

# @pytest.fixture


@pytest.fixture(scope='function')
def client(app):
    """
    Define Flask client
    :param app:
    :return: client
    """
    yield app.test_client()


@pytest.fixture
def runner(app):
    """
    Define cli_runner for Flask app
    :param app:
    :return:
    """
    return app.test_cli_runner()

# c приложения Виталия


class AuthActions:
    def __init__(self, app, client):
        self._app = app
        self._client = client

    def login(self):
        self._app.before_request_funcs[None] = [before_request]
        # self._client.get('/login/register')
        self._client.post('/login/register', data={'User_name': 'test',
                                                   'Login': 'test',
                                                   'Password': 'test'})
        return self._client.post('/login/login', data={'Login': 'test',
                                                       'Password': 'test'})

    def logout(self):
        return self._client.get('/login/logout')


@pytest.fixture(scope='function')
def auth_test(app, client):
    return AuthActions(app, client)
