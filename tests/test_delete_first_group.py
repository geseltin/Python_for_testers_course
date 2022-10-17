


def test_delete_first_group(app):
    app.session.login('admin', 'secret')
    app.open_home_page()
    app.group.delete_first()
    app.session.logout()
