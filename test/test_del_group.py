import pytest
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_first_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.del_first_group()
    app.session.logout()
