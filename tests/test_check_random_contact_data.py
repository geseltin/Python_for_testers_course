from random import randrange


def test_check_random_contact_data_on_home_page_and_edit_form(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_by_index_from_edit_page(index)

    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_homepage == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_homepage == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)

