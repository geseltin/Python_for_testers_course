# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(first_name=Contact.generate_data(Contact), last_name=Contact.generate_data(Contact),
                      mid_name=Contact.generate_data(Contact), nickname=Contact.generate_data(Contact))
    app.contact.add_new(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)











