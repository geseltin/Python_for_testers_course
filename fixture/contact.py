from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # Открыть страницу нового контакта
        self.open_contact_creation_form()
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_list_cache = None

    def fill_contact_form(self, contact, wd):
        if contact.first_name is not None:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.first_name)
        if contact.mid_name is not None:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.mid_name)
        if contact.last_name is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.last_name)
        if contact.nickname is not None:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.title is not None:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company is not None:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.phone_home is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.phone_home)
        if contact.phone_mobile is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        if contact.phone_work is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.phone_work)
        if contact.phone_fax is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.phone_fax)
        if contact.email1 is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email1)
        if contact.email2 is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage is not None:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear is not None:
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)

    def edit_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_index(index)

        self.fill_contact_form(contact, wd)

        wd.find_element_by_name('update').click()
        self.contact_list_cache = None

    def modify_random(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_id(contact.id)
        self.fill_contact_form(contact, wd)
        wd.find_element_by_name('update').click()
        self.contact_list_cache = None


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_index(index)
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()
        self.contact_list_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_id(id)
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()
        self.contact_list_cache = None


    def open_contact_modify_form_by_index(self, index):
        wd = self.app.wd
        xpath = f'//input[@name="selected[]"]/../..//a[contains(@href, "edit")]'
        wd.find_elements_by_xpath(xpath)[index].click()


    def open_contact_modify_form_by_id(self, id):
        wd = self.app.wd
        xpath = f'//a[@href="edit.php?id={id}"]'
        wd.find_element_by_xpath(xpath).click()


    def edit_first(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_index(0)
        self.fill_contact_form(contact, wd)
        wd.find_element_by_name('update').click()
        self.contact_list_cache = None


    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_index()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()
        self.contact_list_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        length = len(wd.find_elements_by_name("selected[]"))
        return length

    def open_contact_creation_form(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    contact_list_cache = None

    def get_contact_list(self):
        if self.contact_list_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_list_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                self.contact_list_cache.append(Contact(id=id, last_name=last_name, first_name=first_name,
                                                       all_phones_from_homepage=all_phones,
                                                       all_emails_from_homepage=all_emails,
                                                       address=address))
        return list(self.contact_list_cache)

    def get_contact_info_by_index_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_modify_form_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        phone_home = wd.find_element_by_name('home').get_attribute('value')
        phone_work = wd.find_element_by_name('work').get_attribute('value')
        phone_mobile = wd.find_element_by_name('mobile').get_attribute('value')
        phone_fax = wd.find_element_by_name('fax').get_attribute('value')
        address = ' '.join(wd.find_element_by_name('address').text.split())
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(id=id, first_name=first_name, last_name=last_name, phone_home=phone_home, phone_work=phone_work,
                       phone_mobile=phone_mobile, phone_fax=phone_fax, address=address,
                       email1=email1, email2=email2, email3=email3)

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        xpath = f'//input[@name="selected[]"]/../..//a[contains(@href, "view")]'
        wd.find_elements_by_xpath(xpath)[index].click()


    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id('content').text
        phone_home = re.search('H: (.*)', text).group(1)
        phone_mobile = re.search('M: (.*)', text).group(1)
        phone_work = re.search('W: (.*)', text).group(1)
        return Contact(phone_home=phone_home, phone_work=phone_work, phone_mobile=phone_mobile)

    def clear(self, string):
        return re.sub("[() -]", "", string)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != '',
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.phone_home, contact.phone_mobile, contact.phone_work]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != '',
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3])))