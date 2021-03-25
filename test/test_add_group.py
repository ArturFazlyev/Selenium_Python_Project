# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group("test", "ds", "")
    app.group.create(group)
    app.group.returns_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
    app.group.returns_to_groups_page()
