from model.contact import Contact


def test_delete_first_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact()
    if app.contact.count() == 0:
        app.contact.add_new(contact)
    app.contact.delete_first_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(old_contact_list, key=Contact.id_or_max)
