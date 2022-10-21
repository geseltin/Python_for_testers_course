


def test_delete_first_contact(app):
    app.contact.delete_first_contact()
    app.open_home_page()