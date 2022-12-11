from model.contact import Contact
import random
import allure



def test_modify_random_contact(app, db, data_contacts):
    contact = data_contacts
    old_contact_list = db.get_contact_list()
    with allure.step('Проверить, что присутствует хотя бы один контакт, если нет - создать'):
        if len(old_contact_list) == 0:
            app.contact.add_new(Contact())
    contact.id = random.choice(old_contact_list).id

    with allure.step(f'Изменить контакт с id {contact.id}'):
        app.contact.modify_random(contact)

    with allure.step('Проверить изменения'):
        assert len(old_contact_list) == app.contact.count()
        new_contact_list = db.get_contact_list()
        for index, item in enumerate(old_contact_list):
            if item.id == contact.id:
                old_contact_list[index] = contact

        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


