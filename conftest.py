import os

import jsonpickle
import pytest

from fixture.application import Application
from fixture.config import Config

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    config = Config()
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
        fixture.open_home_page(config.get_url())
        fixture.session.login(config.get_username(), config.get_password())
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\%s.json" % file)) as f:
       return jsonpickle.decode(f.read())
