from model.contact import Contact


def test_check_contact_data_on_home_page_and_db(app, db):
    contacts_data_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    assert len(contacts_data_from_db) == len(contacts_from_home_page)

    for index in range(len(contacts_data_from_db)):
        assert contacts_from_home_page[index].last_name == contacts_data_from_db[index].last_name
        assert contacts_from_home_page[index].first_name == contacts_data_from_db[index].first_name
        assert contacts_from_home_page[index].address == \
               app.contact.delete_spaces_in_address(contacts_data_from_db[index])
        assert contacts_from_home_page[index].all_emails_from_homepage == \
               app.contact.merge_emails_like_on_home_page(contacts_data_from_db[index])
        assert contacts_from_home_page[index].all_phones_from_homepage == \
               app.contact.merge_phones_like_on_home_page(contacts_data_from_db[index])





