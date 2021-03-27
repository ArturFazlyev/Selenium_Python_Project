# -*- coding: utf-8 -*-

import random
import string

import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "* 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]

]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    app.group.returns_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
