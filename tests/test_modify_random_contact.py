from model.contact import Contact
from random import randrange


def test_modify_random_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(last_name=Contact.generate_data(Contact),
                      first_name=Contact.generate_data(Contact))
    if app.contact.count() == 0:
        app.contact.add_new(Contact())
    index = randrange(len(old_contact_list))
    contact.id = old_contact_list[index].id

    app.contact.edit_by_index(contact, index)
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()

    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

