import pytest

from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser=browser)
        fixture.open_home_page()
        fixture.session.login("admin", "secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.open_home_page()
            fixture.session.login("admin", "secret")
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