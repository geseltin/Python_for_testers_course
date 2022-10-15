


def test_delete_first_group(app):
    app.factory.session.login('admin', 'secret')
    app.factory.group.delete_first()
    app.factory.session.logout()