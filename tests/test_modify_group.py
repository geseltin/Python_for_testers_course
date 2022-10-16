


def test_modify_first_group(app):

    app.factory.session.login('admin', 'secret')
    app.factory.group.modify_first_group()
    app.factory.session.logout()
