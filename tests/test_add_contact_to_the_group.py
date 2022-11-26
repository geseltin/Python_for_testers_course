import random



def test_add_contact_to_the_group(app, db, orm, data_contacts, data_groups):

    def get_not_full_group(group_list):
        for group in group_list:
            contacts_not_in_group = orm.get_contacts_in_group(group)
            if contacts_not_in_group is not None:
                return group

    # Предусловия, проверяем наличие хотя бы одной группы и контакта
    group = data_groups
    contact = data_contacts
    if app.contact.count() == 0:
        app.contact.add_new(contact)
    if app.group.count() == 0:
        app.group.create(group)


    group_list = orm.get_group_list()
    # Ищем неполную группу, если такой нет - создаём

    group_for_test = get_not_full_group(group_list)
    if group_for_test is None:
        app.group.create(group)
        group_list = orm.get_group_list()
        group_for_test = get_not_full_group(group_list)

    contacts_for_test = orm.get_contacts_not_in_group(group_for_test)
    if contacts_for_test == []:
        app.contact.add_new(contact)
        contact_for_test = orm.get_contacts_not_in_group(group_for_test)[0]
    else:
        contact_for_test = random.choice(contacts_for_test)

    # Шаги
    app.contact.add_contact_to_the_group(contact_for_test, group_for_test)

    # Проверки
    contacts_in_group = orm.get_contacts_in_group(group_for_test)
    assert contact_for_test in contacts_in_group


