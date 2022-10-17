


def test_modify_first_group(app):

    app.session.login('admin', 'secret')
    app.group.modify_first_group()
    app.session.logout()
