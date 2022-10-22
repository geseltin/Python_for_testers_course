from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact())
    app.contact.edit_first(Contact(last_name='test_edit_first_contact',
                                   phone_work='8-800-555-00-55',
                                   homepage='www.google.com'))
    app.open_home_page()

