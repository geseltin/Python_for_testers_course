from model.contact import Contact
import allure



def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contact_list = db.get_contact_list()

    with allure.step(f'Создать контакт {contact}'):
        app.contact.add_new(contact)

    with allure.step('Проверить, что созданный контакт присутствует в списке'):
        assert len(old_contact_list) + 1 == app.contact.count()
        new_contact_list = db.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)











