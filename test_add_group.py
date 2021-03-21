# -*- coding: utf-8 -*-

import pytest

from application import Application
from group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_app_dynamics_job(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(Group("test", "test", "test"))
    app.returns_to_groups_page()
    app.logout()
