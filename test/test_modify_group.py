from model.group import Group


def test_modify_group_name(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(name='test3'))
    app.session.logout()

# def test_modify_group_header(app):
#   app.open_home_page()
#   app.session.login("admin", "secret")
#   app.group.modify_first_group(Group(header='test3'))
#   app.session.logout()
