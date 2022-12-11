from model.contact import Contact
import random
import allure



def test_delete_random_contact(app, db):
    old_contact_list = db.get_contact_list()
    contact = Contact()
    with allure.step('Проверить наличие хотя бы одного контакта, если нет - создать'):
        if app.contact.count() == 0:
            app.contact.add_new(contact)

    contact = random.choice(old_contact_list)

    with allure.step(f'Удалить контакт {contact}'):
        app.contact.delete_by_id(contact.id)

    with allure.step(f'Проверить, что контакт {contact} - удалён'):
        new_contact_list = db.get_contact_list()

        assert len(old_contact_list) - 1 == app.contact.count()
        old_contact_list.remove(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
