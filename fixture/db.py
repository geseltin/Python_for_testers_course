import pymysql
from model.group import Group
from model.contact import Contact
from fixture.orm import OrmFixture


class DbFixture:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database=database,
                                          autocommit=True)


    def get_group_list(self):
        group_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        return group_list

    def get_contact_list(self):
        contact_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT id, firstname, lastname, middlename, address, email, email2, email3, home, mobile, work "
                           "FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, address, email, email2, email3, home, mobile, work) = row
                contact_list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, mid_name=middlename,
                                            address=address, email1=email, email2=email2, email3=email3, phone_home=home,
                                            phone_mobile=mobile, phone_work=work))
        return contact_list

    def get_adress_in_groups_rows_count(self):
        with self.connection.cursor() as cursor:
            rows = cursor.execute("SELECT * FROM address_in_groups")
            return rows


    def destroy(self):
        self.connection.close()
