from model.contact import Contact


def test_edit_first_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(last_name='test_edit_first_contact',
                                   phone_work='8-800-555-00-55',
                                   homepage='www.google.com')
    if app.contact.count() == 0:
        app.contact.add_new(Contact())
    app.contact.edit_first(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(old_contact_list, key=Contact.id_or_max)

