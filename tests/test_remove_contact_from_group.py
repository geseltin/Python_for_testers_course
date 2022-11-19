import random



def test_remove_contact_from_group(app, db, orm, data_groups, data_contacts):

    # Предусловия
    if db.get_adress_in_groups_rows_count == 0:
        group = data_groups
        contact = data_contacts
        app.group.create(group)
        app.contact.add_new(contact)
        app.contact.add_contact_to_the_group(contact=contact, group=group)

    # Шаги
    contact_list = orm.get_contact_list()
    contact_for_test = app.contact.get_contact_included_in_group_from_list(contact_list)

    group = random.choice(contact_for_test.included_in_groups)
    app.contact.remove_contact_from_group(contact=contact_for_test, group=group)

    # Проверки
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_for_test not in contacts_in_group
