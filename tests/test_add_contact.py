from model.contact import Contact
import pytest



test_data = [Contact(first_name=Contact.generate_data(Contact), last_name=Contact.generate_data(Contact),
                     mid_name=Contact.generate_data(Contact), nickname=Contact.generate_data(Contact),
                     phone_mobile=Contact.generate_mobile_phone(Contact), phone_home=Contact.generate_home_phone(Contact),
                     phone_work=Contact.generate_work_phone(Contact), email1=Contact.generate_email(Contact),
                     email2=Contact.generate_email(Contact), email3=Contact.generate_email(Contact),
                     address=Contact.generate_address(Contact)) for i in range(3)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)











