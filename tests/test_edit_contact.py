from model.contact import Contact



def test_edit_contact(app):
    contact = Contact()
    app.session.login('admin', 'secret')
    app.contact.add_new(contact)
    app.open_home_page()
    app.contact.edit_contact(contact)
    app.open_home_page()

