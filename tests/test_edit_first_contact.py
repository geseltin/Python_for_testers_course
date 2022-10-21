from model.contact import Contact


def test_edit_first_contact(app):
    contact = Contact(last_name='test_edit_first_contact',
                      phone_work='8-800-555-00-55',
                      homepage='www.google.com')
    app.contact.edit_first(contact)
    app.open_home_page()

