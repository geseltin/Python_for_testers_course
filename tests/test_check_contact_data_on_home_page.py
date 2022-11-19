


def test_check_contact_data_on_home_page_and_db(app, db):
    contacts_data_from_db = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()

    for contact_from_db in contacts_data_from_db:
        for contact_from_home_page in contacts_from_home_page:
            if contact_from_db.id == contact_from_home_page.id:
                assert contact_from_home_page.last_name == contact_from_db.last_name
                assert contact_from_home_page.first_name == contact_from_db.first_name
                assert contact_from_home_page.address == app.contact.delete_spaces_in_address(contact_from_db)
                assert contact_from_home_page.all_emails_from_homepage == app.contact.merge_emails_like_on_home_page(
                    contact_from_db)
                assert contact_from_home_page.all_phones_from_homepage == app.contact.merge_phones_like_on_home_page(
                    contact_from_db)
                break



