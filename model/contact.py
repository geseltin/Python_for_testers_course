import random



class Contact:

    def __init__(self, first_name=None, mid_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, phone_home=None, phone_mobile=None, phone_work=None, phone_fax=None, email1=None,
                 email2=None, email3=None, homepage=None, birth_day=None, birth_month=None, birth_year=None):
        self.first_name = first_name or self.generate_data(),
        self.mid_name = mid_name or self.generate_data(),
        self.last_name = last_name or self.generate_data(),
        self.nickname = nickname or self.generate_data(),
        self.title = title or '',
        self.company = company or '',
        self.address = address or '',
        self.phone_home = phone_home or '',
        self.phone_mobile = phone_mobile or '',
        self.phone_work = phone_work or '',
        self.phone_fax = phone_fax or '',
        self.email1 = email1 or '',
        self.email2 = email2 or '',
        self.email3 = email3 or '',
        self.homepage = homepage or '',
        self.bday = birth_day,
        self.bmonth = birth_month,
        self.byear = birth_year

    def generate_data(self):
        data = ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
        return data

