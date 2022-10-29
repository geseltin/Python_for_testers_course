from model.contact import Contact
from random import randrange



def test_delete_random_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact()
    if app.contact.count() == 0:
        app.contact.add_new(contact)
    index = randrange(len(old_contact_list))
    app.contact.delete_contact_by_index(index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == app.contact.count()
    old_contact_list[index:index+1] = []
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
