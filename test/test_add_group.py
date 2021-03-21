# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group("test", "test", "test"))
    app.group.returns_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group("test", "", ""))
    app.group.returns_to_groups_page()
    app.session.logout()
