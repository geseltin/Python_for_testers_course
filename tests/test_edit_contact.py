from model.contact import Contact



def test_edit_contact(app):
    contact = Contact()
    app.factory.session.login('admin', 'secret')
    app.factory.contact.add_new(contact)
    app.open_home_page()
    app.factory.contact.edit_contact(contact)
    app.open_home_page()

