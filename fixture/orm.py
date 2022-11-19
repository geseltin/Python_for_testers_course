from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class OrmFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: OrmFixture.ORMContact, table="address_in_groups",
                       column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        address = Optional(str, column='address')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        phone_home = Optional(str, column='home')
        phone_mobile = Optional(str, column='mobile')
        phone_work = Optional(str, column='work')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: OrmFixture.ORMGroup, table="address_in_groups",
                     column="group_id", reverse="contacts", lazy=True)




    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host=host, user=user, password=password, database=database)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.first_name, last_name=contact.last_name,
                           address=contact.address, email1=contact.email1, email2=contact.email2, email3=contact.email3,
                           phone_home=contact.phone_home, phone_mobile=contact.phone_mobile,
                           phone_work=contact.phone_work, included_in_groups=self.convert_group_set(contact.groups))
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in OrmFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in OrmFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in OrmFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in OrmFixture.ORMGroup if g.id == group.id))[0]

        return self.convert_contacts_to_model(
            select(c for c in OrmFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_contact_with_groups(self):
        list_orm = list(select(g for g in OrmFixture.ORMGroup))
        def convert(orm):
            return orm.contacts

        return list(map(convert, list_orm))

    @db_session
    def get_contact_included_groups(self):
        contact_list = self.convert_contacts_to_model(select(c for c in OrmFixture.ORMContact if c.deprecated is None))
        group_list = []
        for contact in contact_list:
            for x in contact.included_in_groups:
                group_list.append(x)
        return self.convert_groups_to_model(group_list)

    @db_session
    def convert_group_set(self, group_set):
        group_list = []
        for group in group_set:
            group_list.append(group)
        return self.convert_groups_to_model(group_list)


