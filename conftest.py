import configparser
import os

import pytest

from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    config = configparser.ConfigParser()
    print(config.read(os.path.abspath('../example.ini')))
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
        fixture.open_home_page(config.get("Settings", "url"))
        fixture.session.login(config.get("Settings", "username"), config.get("Settings", "password"))
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
