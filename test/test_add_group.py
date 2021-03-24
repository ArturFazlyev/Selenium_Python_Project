# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group("test", "test", "test"))
    app.group.returns_to_groups_page()


def test_add_empty_group(app):
    app.group.create(Group("test", "", ""))
    app.group.returns_to_groups_page()
