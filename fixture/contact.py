from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # Открыть страницу нового контакта
        self.open_contact_creation_form()
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.mid_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.phone_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        xpath = f'//input[@name="selected[]"]/../..//a[contains(@href, "edit")]'
        wd.find_element_by_xpath(xpath).click()

        self.fill_contact_form(contact, wd)

        wd.find_element_by_name('update').click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        xpath = f'//input[@name="selected[]"]/../..//a[contains(@href, "edit")]'
        wd.find_element_by_xpath(xpath).click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        length = len(wd.find_elements_by_name("selected[]"))
        return length

    def open_contact_creation_form(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contact_list = []
        for element in wd.find_elements_by_xpath("//*[@name='entry']"):
            last_name = element.find_element_by_xpath("//*[@name='entry']/td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            first_name = element.find_element_by_xpath("//*[@name='entry']/td[3]").text
            contact_list.append(Contact(id=id, last_name=last_name, first_name=first_name))
        return contact_list