# -*- coding: utf-8 -*-


def test_add_group(app, json_group):
    group = json_group
    old_groups = app.group.get_group_list()
    app.group.create(group)
    app.group.returns_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
