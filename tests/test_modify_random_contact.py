import random

from model.contact import Contact
import random


def test_modify_random_contact(app, db, data_contacts):
    contact = data_contacts
    old_contact_list = db.get_contact_list()
    if len(old_contact_list) == 0:
        app.contact.add_new(Contact())

    contact.id = random.choice(old_contact_list).id
    app.contact.modify_random(contact)

    assert len(old_contact_list) == app.contact.count()
    new_contact_list = db.get_contact_list()
    for index, item in enumerate(old_contact_list):
        if item.id == contact.id:
            old_contact_list[index] = contact

    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


