import random



def test_add_contact_to_the_group(app, db, data_contacts, data_groups):
    # Предусловия, проверяем наличие группы и контакта
    if app.contact.count() == 0:
        contact = data_contacts
        app.contact.add_new(contact)
    if app.group.count() == 0:
        group = data_groups
        app.group.create(group)

    # Шаги
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_the_group(contact, group)

    # Проверки
    contacts_in_group = db.get_contacts_in_group(group)
    assert contact in contacts_in_group


